# PDF File Size Reducer

A Python program that significantly reduces PDF file sizes by compressing images, removing metadata, and optimizing content streams. Perfect for reducing large PDFs (like 18MB) down to much smaller sizes (like 2MB).

## Features

- **Image Compression**: Compresses embedded images with adjustable quality
- **Metadata Removal**: Removes document metadata to save space
- **Content Stream Optimization**: Compresses PDF content streams
- **Batch Processing**: Easy command-line interface
- **Progress Feedback**: Shows compression progress and results

## Installation

1. Make sure you have Python 3.7+ installed
2. Install required packages:
   ```bash
   pip install PyPDF2 reportlab Pillow pikepdf
   ```

## Usage

### Basic Usage

```bash
python pdf_compressor.py input_file.pdf
```

### Specify Output File

```bash
python pdf_compressor.py input_file.pdf -o compressed_file.pdf
```

### Adjust Image Quality (1-100, lower = smaller file)

```bash
python pdf_compressor.py input_file.pdf -q 20
```

### Limit Image Dimensions

```bash
python pdf_compressor.py input_file.pdf --max-width 800 --max-height 800
```

### Full Example

```bash
python pdf_compressor.py large_document.pdf -o small_document.pdf -q 25 --max-width 1000 --max-height 1000
```

## Parameters

- `input_path`: Path to the PDF file you want to compress (required)
- `-o, --output`: Output file path (optional, defaults to `filename_compressed.pdf`)
- `-q, --quality`: Image quality from 1-100 (default: 30, lower = smaller file)
- `--max-width`: Maximum image width in pixels (default: 1200)
- `--max-height`: Maximum image height in pixels (default: 1200)

## How It Works

1. **Image Compression**: Finds all embedded images and recompresses them as JPEG with specified quality
2. **Image Resizing**: Reduces oversized images to specified maximum dimensions
3. **Metadata Removal**: Strips out document metadata and XMP data
4. **Stream Compression**: Applies compression to PDF content streams
5. **Object Optimization**: Uses efficient object stream encoding

## Expected Results

- **Text-heavy PDFs**: 20-50% size reduction
- **Image-heavy PDFs**: 70-90% size reduction
- **Mixed content PDFs**: 50-80% size reduction

For an 18MB PDF with images, you can typically expect:

- Quality 30: ~2-4MB (recommended balance)
- Quality 20: ~1-2MB (higher compression)
- Quality 50: ~4-6MB (better quality)

## Tips for Best Results

1. **For maximum compression**: Use quality 15-25
2. **For good balance**: Use quality 25-35 (default: 30)
3. **For minimal quality loss**: Use quality 40-60
4. **Reduce image dimensions** for PDFs with very large images
5. **Test different settings** to find the best balance for your needs

## Troubleshooting

- **"Permission denied"**: Make sure the PDF is not open in another application
- **"Corrupted PDF"**: Try a different PDF or check if the original file is damaged
- **"Not enough compression"**: Try lower quality settings or smaller image dimensions
- **"Images look poor"**: Increase quality setting or image dimensions

## Example Output

```
Opening PDF: large_document.pdf
Original size: 18.45 MB
Processing images...
Processed 25 images
Removing metadata...
Saving compressed PDF to: large_document_compressed.pdf
Compression complete!
New size: 2.13 MB
Size reduction: 88.4%

Success! Compressed PDF saved to: large_document_compressed.pdf
File size reduced from 18.45 MB to 2.13 MB (88.4% reduction)
```
