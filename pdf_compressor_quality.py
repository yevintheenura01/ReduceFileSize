#!/usr/bin/env python3
"""
Quality-Preserving PDF Compressor - Better color and quality handling
"""

import os
from pathlib import Path
import pikepdf
from PIL import Image
import io


class QualityPreservingCompressor:
    """PDF compressor that preserves image quality and colors better."""
    
    def __init__(self, quality=40, grayscale_quality=50):
        self.quality = quality
        self.grayscale_quality = grayscale_quality
    
    def get_file_size_mb(self, file_path):
        """Get file size in MB."""
        return os.path.getsize(file_path) / (1024 * 1024)
    
    def smart_image_extraction(self, image_obj):
        """Smart image extraction with multiple fallback methods."""
        try:
            width = int(image_obj.get('/Width', 0))
            height = int(image_obj.get('/Height', 0))
            colorspace = image_obj.get('/ColorSpace', pikepdf.Name.DeviceRGB)
            
            print(f"     📐 Dimensions: {width}x{height}")
            print(f"     🎨 Colorspace: {colorspace}")
            
            # Method 1: Try pikepdf's built-in image extraction first (most reliable)
            try:
                img = image_obj.as_pil_image()
                if img:
                    print(f"     ✅ Built-in extraction successful ({img.mode})")
                    return img
            except Exception as e:
                print(f"     ⚠ Built-in extraction failed: {e}")
            
            # Method 2: Manual extraction as fallback
            image_data = image_obj.read_bytes()
            colorspace_str = str(colorspace)
            
            # Determine mode based on colorspace
            if '/DeviceRGB' in colorspace_str:
                mode, channels = 'RGB', 3
            elif '/DeviceGray' in colorspace_str:
                mode, channels = 'L', 1
            elif '/DeviceCMYK' in colorspace_str:
                mode, channels = 'CMYK', 4
            else:
                mode, channels = 'RGB', 3  # Default
            
            expected_size = width * height * channels
            
            if len(image_data) >= expected_size:
                try:
                    img = Image.frombytes(mode, (width, height), image_data[:expected_size])
                    print(f"     ✅ Manual extraction successful ({mode})")
                    return img
                except Exception as e:
                    print(f"     ⚠ Manual extraction failed: {e}")
            
            # Method 3: Try RGB as fallback
            if len(image_data) >= width * height * 3:
                try:
                    img = Image.frombytes('RGB', (width, height), image_data[:width * height * 3])
                    print(f"     ✅ RGB fallback successful")
                    return img
                except:
                    pass
            
            print(f"     ❌ All extraction methods failed")
            return None
            
        except Exception as e:
            print(f"     ❌ Extraction error: {e}")
            return None
    
    def compress_image_smart(self, img):
        """Smart image compression with quality preservation."""
        original_mode = img.mode
        
        # Resize only if extremely large
        if img.width > 1500 or img.height > 1500:
            original_size = img.size
            img.thumbnail((1500, 1500), Image.Resampling.LANCZOS)
            print(f"     📏 Resized {original_size} → {img.size}")
        
        # Smart quality and format selection
        if original_mode == 'L':
            # Grayscale images - preserve as grayscale with higher quality
            print(f"     🖤 Preserving grayscale (Q{self.grayscale_quality})")
            output = io.BytesIO()
            img.save(output, format='JPEG', quality=self.grayscale_quality, optimize=True)
            return output.getvalue()
            
        elif original_mode in ('RGB', 'CMYK'):
            # Color images
            if original_mode == 'CMYK':
                img = img.convert('RGB')
                print(f"     🎨 CMYK → RGB conversion")
            
            print(f"     🌈 Color compression (Q{self.quality})")
            output = io.BytesIO()
            img.save(output, format='JPEG', quality=self.quality, optimize=True)
            return output.getvalue()
            
        elif original_mode == 'RGBA':
            # Handle transparency by creating white background
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[-1])
            img = background
            print(f"     🎨 RGBA → RGB (white background)")
            
            output = io.BytesIO()
            img.save(output, format='JPEG', quality=self.quality, optimize=True)
            return output.getvalue()
            
        else:
            # Other modes - convert to RGB
            img = img.convert('RGB')
            print(f"     🎨 {original_mode} → RGB conversion")
            
            output = io.BytesIO()
            img.save(output, format='JPEG', quality=self.quality, optimize=True)
            return output.getvalue()
    
    def process_pdf_images(self, pdf):
        """Process PDF images with quality preservation."""
        images_processed = 0
        total_savings = 0
        
        for page_num, page in enumerate(pdf.pages):
            try:
                if '/Resources' not in page or '/XObject' not in page['/Resources']:
                    continue
                
                xobjects = page['/Resources']['/XObject']
                
                for name, obj in list(xobjects.items()):
                    try:
                        if (hasattr(obj, 'Subtype') and 
                            str(obj.Subtype) == '/Image' and
                            '/Filter' in obj and
                            str(obj['/Filter']) == '/FlateDecode'):
                            
                            print(f"   🖼️ Processing image on page {page_num + 1}...")
                            
                            # Get original size
                            original_data = obj.read_bytes()
                            original_size_kb = len(original_data) // 1024
                            
                            # Extract image
                            img = self.smart_image_extraction(obj)
                            
                            if img:
                                # Compress with quality preservation
                                compressed_data = self.compress_image_smart(img)
                                compressed_size_kb = len(compressed_data) // 1024
                                
                                # Only replace if compression is significant
                                compression_ratio = (1 - len(compressed_data) / len(original_data)) * 100
                                
                                if compression_ratio > 10:  # Only if >10% savings
                                    # Update the PDF object
                                    obj.write(compressed_data, filter=pikepdf.Name.DCTDecode)
                                    obj['/Width'] = img.width
                                    obj['/Height'] = img.height
                                    obj['/BitsPerComponent'] = 8
                                    
                                    # Set appropriate colorspace
                                    if img.mode == 'L':
                                        obj['/ColorSpace'] = pikepdf.Name.DeviceGray
                                    else:
                                        obj['/ColorSpace'] = pikepdf.Name.DeviceRGB
                                    
                                    savings_kb = original_size_kb - compressed_size_kb
                                    total_savings += savings_kb
                                    images_processed += 1
                                    
                                    print(f"     💾 {original_size_kb} KB → {compressed_size_kb} KB ({compression_ratio:.1f}% reduction)")
                                else:
                                    print(f"     ⏭️ Skipped (only {compression_ratio:.1f}% savings)")
                            else:
                                print(f"     ❌ Could not extract image")
                                
                    except Exception as e:
                        print(f"     ⚠ Error processing image: {e}")
                        continue
                        
            except Exception as e:
                continue
        
        print(f"   ✅ Processed {images_processed} images")
        print(f"   💾 Total image savings: {total_savings} KB ({total_savings/1024:.1f} MB)")
        
        return images_processed
    
    def compress_pdf_quality(self, input_path, output_path=None):
        """Compress PDF with quality preservation."""
        input_path = Path(input_path)
        
        if not input_path.exists():
            return False, None, 0, 0, "Input file does not exist"
        
        if output_path is None:
            output_path = input_path.parent / f"{input_path.stem}_compressed_quality{input_path.suffix}"
        else:
            output_path = Path(output_path)
        
        original_size = self.get_file_size_mb(input_path)
        
        try:
            print(f"📄 Processing: {input_path.name}")
            print(f"📏 Original size: {original_size:.2f} MB")
            print(f"🎛️ Color quality: {self.quality}, Grayscale quality: {self.grayscale_quality}")
            print()
            
            with pikepdf.open(input_path) as pdf:
                print("🔄 Processing images with quality preservation...")
                images_processed = self.process_pdf_images(pdf)
                
                print("\n🧹 Cleaning metadata...")
                try:
                    if pdf.docinfo:
                        for key in list(pdf.docinfo.keys()):
                            try:
                                del pdf.docinfo[key]
                            except:
                                pass
                    print("   ✅ Metadata cleaned")
                except Exception as e:
                    print(f"   ⚠ Warning: {e}")
                
                print("\n💾 Saving optimized PDF...")
                pdf.save(output_path, compress_streams=True)
            
            new_size = self.get_file_size_mb(output_path)
            compression_ratio = (1 - new_size / original_size) * 100 if original_size > 0 else 0
            savings_mb = original_size - new_size
            
            print("="*60)
            print("📊 Compression Results:")
            print(f"   Original: {original_size:.2f} MB")
            print(f"   New size: {new_size:.2f} MB")
            print(f"   Saved: {savings_mb:.2f} MB ({compression_ratio:.1f}% reduction)")
            
            return True, str(output_path), original_size, new_size, None
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            print(f"❌ {error_msg}")
            return False, None, original_size, 0, error_msg


def main():
    """Main function with quality-focused options."""
    print("=== Quality-Preserving PDF Compressor ===")
    print("Better color handling and quality preservation!")
    print()
    
    # Get input file
    while True:
        input_path = input("📁 Enter PDF file path: ").strip().strip('"').strip("'")
        if input_path and Path(input_path).exists():
            break
        print("❌ File not found. Please try again.")
    
    # Get quality settings
    print("\n🎨 Choose quality level:")
    print("1. High quality (Color: 60, Grayscale: 70) - Larger file, best quality")
    print("2. Balanced quality (Color: 45, Grayscale: 55) - Good balance [Recommended]")
    print("3. Compact (Color: 30, Grayscale: 40) - Smaller file, lower quality")
    
    quality_settings = {
        "1": (60, 70),
        "2": (45, 55),
        "3": (30, 40)
    }
    
    while True:
        choice = input("Enter choice (1-3) or press Enter for balanced [2]: ").strip()
        if choice in quality_settings:
            color_quality, gray_quality = quality_settings[choice]
            break
        elif choice == "":
            color_quality, gray_quality = quality_settings["2"]
            break
        else:
            print("❌ Please enter 1, 2, or 3.")
    
    print(f"\n🚀 Starting compression...")
    print(f"Settings: Color Q{color_quality}, Grayscale Q{gray_quality}")
    print("="*60)
    
    # Process the PDF
    compressor = QualityPreservingCompressor(
        quality=color_quality, 
        grayscale_quality=gray_quality
    )
    
    success, output_file, original_size, new_size, error = compressor.compress_pdf_quality(input_path)
    
    if success:
        print("🎉 SUCCESS!")
        print(f"📁 Quality-preserved PDF: {output_file}")
        
        if new_size < original_size * 0.3:
            print("🏆 Excellent compression with quality preservation!")
        elif new_size < original_size * 0.6:
            print("✅ Good compression while maintaining quality!")
        
        print("\n💡 Quality Notes:")
        print("   • Grayscale images preserved as grayscale")
        print("   • Color images maintain better color fidelity")
        print("   • Minimal resizing to preserve details")
        
    else:
        print(f"❌ Failed: {error}")


if __name__ == "__main__":
    main()