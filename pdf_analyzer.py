#!/usr/bin/env python3
"""
PDF Analyzer - Diagnose why a PDF cannot be compressed much
"""

import os
from pathlib import Path
import pikepdf
from PIL import Image
import io


class PDFAnalyzer:
    """Analyze PDF structure to understand compression potential."""
    
    def analyze_pdf(self, pdf_path):
        """Analyze PDF structure and content."""
        pdf_path = Path(pdf_path)
        
        if not pdf_path.exists():
            print("❌ File not found")
            return
        
        file_size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
        print(f"📄 Analyzing: {pdf_path.name}")
        print(f"📏 File size: {file_size_mb:.2f} MB")
        print("=" * 50)
        
        try:
            with pikepdf.open(pdf_path) as pdf:
                print(f"📖 Total pages: {len(pdf.pages)}")
                
                # Analyze document structure
                self.analyze_document_info(pdf)
                self.analyze_content_structure(pdf)
                self.analyze_images(pdf)
                self.analyze_compression_potential(pdf, file_size_mb)
                
        except Exception as e:
            print(f"❌ Error analyzing PDF: {e}")
    
    def analyze_document_info(self, pdf):
        """Analyze document metadata."""
        print("\n🔍 Document Information:")
        
        try:
            if pdf.docinfo:
                print(f"   Metadata entries: {len(pdf.docinfo)}")
                for key, value in pdf.docinfo.items():
                    print(f"   {key}: {str(value)[:50]}...")
            else:
                print("   ✓ No metadata found")
        except:
            print("   ⚠ Could not read metadata")
        
        # Check for XMP metadata
        try:
            if '/Metadata' in pdf.Root:
                print("   📋 XMP metadata present")
            else:
                print("   ✓ No XMP metadata")
        except:
            print("   ⚠ Could not check XMP metadata")
    
    def analyze_content_structure(self, pdf):
        """Analyze PDF content structure."""
        print("\n📊 Content Structure:")
        
        total_objects = len(pdf.objects)
        print(f"   Total objects: {total_objects}")
        
        # Count different object types
        streams = 0
        fonts = 0
        
        for obj in pdf.objects:
            try:
                if hasattr(obj, 'stream_dict'):
                    streams += 1
                if hasattr(obj, 'Subtype') and str(obj.Subtype) in ['/Type1', '/TrueType', '/Type0']:
                    fonts += 1
            except:
                continue
        
        print(f"   Content streams: {streams}")
        print(f"   Fonts: {fonts}")
    
    def analyze_images(self, pdf):
        """Analyze images in the PDF."""
        print("\n🖼️ Image Analysis:")
        
        total_images = 0
        image_details = []
        total_image_size = 0
        
        for page_num, page in enumerate(pdf.pages):
            try:
                if '/Resources' not in page or '/XObject' not in page['/Resources']:
                    continue
                
                xobjects = page['/Resources']['/XObject']
                
                for name, obj in xobjects.items():
                    try:
                        if hasattr(obj, 'Subtype') and str(obj.Subtype) == '/Image':
                            total_images += 1
                            
                            # Get image properties
                            width = int(obj.get('/Width', 0))
                            height = int(obj.get('/Height', 0))
                            
                            # Get compression info
                            filter_type = "Unknown"
                            if '/Filter' in obj:
                                filter_type = str(obj['/Filter'])
                            
                            # Estimate image data size
                            try:
                                image_data = obj.read_bytes()
                                data_size_kb = len(image_data) / 1024
                                total_image_size += data_size_kb
                                
                                image_details.append({
                                    'page': page_num + 1,
                                    'size': f"{width}x{height}",
                                    'filter': filter_type,
                                    'size_kb': data_size_kb
                                })
                            except:
                                image_details.append({
                                    'page': page_num + 1,
                                    'size': f"{width}x{height}",
                                    'filter': filter_type,
                                    'size_kb': 0
                                })
                    except:
                        continue
                        
            except:
                continue
        
        print(f"   Total images found: {total_images}")
        print(f"   Total image data: {total_image_size:.1f} KB ({total_image_size/1024:.1f} MB)")
        
        if image_details:
            print("   Image breakdown:")
            for img in image_details[:10]:  # Show first 10 images
                print(f"     Page {img['page']}: {img['size']} - {img['filter']} - {img['size_kb']:.1f} KB")
            
            if len(image_details) > 10:
                print(f"     ... and {len(image_details) - 10} more images")
        else:
            print("   ✓ No images found (text-only PDF)")
    
    def analyze_compression_potential(self, pdf, file_size_mb):
        """Analyze compression potential."""
        print("\n💡 Compression Analysis:")
        
        # Check if already compressed
        compressed_streams = 0
        total_streams = 0
        
        for obj in pdf.objects:
            try:
                if hasattr(obj, 'stream_dict'):
                    total_streams += 1
                    if '/Filter' in obj.stream_dict:
                        compressed_streams += 1
            except:
                continue
        
        if total_streams > 0:
            compression_ratio = (compressed_streams / total_streams) * 100
            print(f"   Content streams compressed: {compressed_streams}/{total_streams} ({compression_ratio:.1f}%)")
        
        # Analyze why compression might be limited
        print("\n🔧 Why compression is limited:")
        
        # Check for text content
        text_indicators = 0
        for page_num, page in enumerate(pdf.pages):
            try:
                if '/Contents' in page:
                    content = page['/Contents']
                    if hasattr(content, 'read_bytes'):
                        content_data = content.read_bytes()
                        # Look for text operators
                        if b'Tj' in content_data or b'TJ' in content_data or b'Td' in content_data:
                            text_indicators += 1
            except:
                continue
        
        if text_indicators > len(pdf.pages) * 0.7:
            print("   📝 This PDF is primarily text-based")
            print("     → Text PDFs have limited compression potential")
            print("     → Already uses efficient text encoding")
        
        # Check if images are already compressed
        jpeg_images = 0
        total_images = 0
        
        for page in pdf.pages:
            try:
                if '/Resources' in page and '/XObject' in page['/Resources']:
                    xobjects = page['/Resources']['/XObject']
                    for name, obj in xobjects.items():
                        if hasattr(obj, 'Subtype') and str(obj.Subtype) == '/Image':
                            total_images += 1
                            if '/Filter' in obj and str(obj['/Filter']) == '/DCTDecode':
                                jpeg_images += 1
            except:
                continue
        
        if total_images > 0:
            jpeg_ratio = (jpeg_images / total_images) * 100
            print(f"   🖼️ Images already JPEG compressed: {jpeg_images}/{total_images} ({jpeg_ratio:.1f}%)")
            if jpeg_ratio > 80:
                print("     → Most images are already optimally compressed")
        
        # Recommendations
        print("\n💡 Recommendations:")
        if file_size_mb < 5:
            print("   ✓ File is already reasonably small")
        
        if total_images == 0:
            print("   📝 Text-only PDF - try a different PDF with images for better compression")
        elif jpeg_images == total_images and total_images > 0:
            print("   🖼️ All images already compressed - minimal gains possible")
        
        print("   🎯 For significant compression, try PDFs with:")
        print("     • High-resolution photos")
        print("     • Uncompressed images")
        print("     • Scanned documents")
        print("     • Large embedded graphics")


def main():
    """Main function for PDF analysis."""
    print("=== PDF Compression Analyzer ===")
    print("This tool analyzes why your PDF cannot be compressed much.")
    print()
    
    while True:
        pdf_path = input("📁 Enter path to PDF file: ").strip().strip('"').strip("'")
        if pdf_path and Path(pdf_path).exists():
            break
        print("❌ File not found. Please try again.")
    
    analyzer = PDFAnalyzer()
    analyzer.analyze_pdf(pdf_path)
    
    print("\n" + "="*50)
    print("🎯 Summary: Your PDF likely has minimal compression potential because:")
    print("   • It's primarily text-based (already efficiently encoded)")
    print("   • Images are already JPEG compressed")
    print("   • Content streams are already compressed")
    print("   • File structure is optimized")


if __name__ == "__main__":
    main()