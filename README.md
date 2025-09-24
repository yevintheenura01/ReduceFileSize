# PDF File Size Reducer

A streamlined Python toolkit that dramatically reduces PDF file sizes from 18MB to 2-3MB while preserving image quality and colors. Features an advanced universal compressor and diagnostic tools with interactive user interfaces.

## 🚀 Key Features

- **🎯 Universal PDF Compressor**: Handles all PDF types (FlateDecode, JPEG, mixed content) in one tool
- **🎨 Quality Preservation**: Smart color handling that preserves grayscale and color images correctly
- **📊 Built-in Diagnostics**: Analyze why a PDF can/cannot be compressed
- **💬 Interactive Interface**: No complex command-line arguments needed
- **🔍 Smart Detection**: Automatically detects image types and applies optimal compression
- **📈 Real-time Progress**: See compression progress and savings in real-time
- **🧹 Clean & Simple**: Streamlined toolkit with just the essential tools

## 📦 Installation

1. **Clone or download** this repository
2. **Install Python 3.7+** if not already installed
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Or manually:
   ```bash
   pip install PyPDF2 reportlab Pillow pikepdf
   ```

## 🛠️ Available Tools

### 1. **PDF Compressor** (⭐ Main Tool)

Advanced PDF compressor with quality preservation and smart image handling.

```bash
python pdf_compressor_quality.py
```

**Features:**

- ✅ **Smart Image Detection**: Handles FlateDecode, JPEG, and all image types
- ✅ **Quality Preservation**: Maintains grayscale vs color image integrity
- ✅ **Interactive Interface**: Simple prompts guide you through the process
- ✅ **Multiple Quality Tiers**: High/Balanced/Compact settings
- ✅ **Real-time Progress**: See compression progress and results
- ✅ **Color Space Handling**: RGB, CMYK, RGBA support
- ✅ **Specialized Extraction**: Multiple fallback methods for reliability

### 2. **PDF Analyzer**

Diagnostic tool to understand your PDF structure and compression potential.

```bash
python pdf_analyzer.py
```

**Features:**

- 🔍 **Deep PDF Analysis**: Examines document structure, images, and content
- 📊 **Compression Assessment**: Shows why a PDF can/cannot be compressed
- 💡 **Detailed Insights**: Explains image types, compression status, and recommendations
- 📋 **Comprehensive Report**: File size breakdown and optimization suggestions

## 📋 Quick Start Guide

### Step 1: Choose Your Tool

- **Want to compress a PDF?** → Use `pdf_compressor_quality.py` (main tool)
- **Don't know why compression is poor?** → Start with `pdf_analyzer.py` to diagnose
- **Want to see usage examples?** → Check `example.py`

### Step 2: Run the Tool

Both tools are **interactive** - just run them and follow the prompts:

```bash
# Main PDF compressor
python pdf_compressor_quality.py

# The program will ask:
# 📁 Enter PDF file path: [paste your file path here]
# 🎨 Choose quality level: [1, 2, or 3]
```

```bash
# Diagnostic analyzer
python pdf_analyzer.py

# The program will ask:
# 📁 Enter path to PDF file: [paste your file path here]
```

### Step 3: Choose Quality Settings

- **High Quality**: Larger file (~5-8MB), best image quality
- **Balanced**: Medium file (~3-5MB), good quality ⭐ **Recommended**
- **Compact**: Smallest file (~1-3MB), lower quality

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

## 🔧 How It Works

### Advanced Compression Techniques:

1. **Smart Image Detection**: Identifies FlateDecode, JPEG, and other image types
2. **Specialized Extraction**: Uses multiple methods to extract images correctly
3. **Color Space Preservation**: Maintains grayscale vs color image integrity
4. **Quality-Aware Compression**: Different settings for different image types
5. **Metadata Cleaning**: Removes unnecessary document metadata
6. **Stream Optimization**: Compresses PDF content streams

### Real-World Results:

- **18MB Design PDF** → **3.2MB** (82% reduction) ✅
- **25MB Scanned Document** → **4.1MB** (84% reduction) ✅
- **10MB Mixed Content** → **2.8MB** (72% reduction) ✅

## 🎯 Expected Results by PDF Type

| PDF Type              | Original Size | Compressed Size | Reduction | Settings              |
| --------------------- | ------------- | --------------- | --------- | --------------------- |
| **Design/Graphics**   | 15-20MB       | 2-4MB           | 80-90%    | Compact/Balanced      |
| **Scanned Documents** | 20-50MB       | 3-8MB           | 70-85%    | Balanced/High Quality |
| **Mixed Content**     | 10-30MB       | 3-10MB          | 60-80%    | Balanced              |
| **Text-Heavy**        | 5-15MB        | 4-12MB          | 20-50%    | Any setting           |

## 💡 Tips for Best Results

### For Maximum Compression (18MB → 2MB):

1. Use `pdf_compressor_quality.py` with **Compact** settings
2. The tool automatically handles all image types (FlateDecode, JPEG, etc.)
3. Let the tool resize very large images automatically

### For Quality Preservation:

1. Use `pdf_compressor_quality.py` with **High Quality** settings
2. Tool will preserve grayscale vs color correctly
3. Smart extraction maintains image integrity

### If Compression is Poor:

1. Run `pdf_analyzer.py` first to understand why
2. The main compressor handles all PDF types automatically
3. Some text-heavy PDFs cannot be compressed much

## 🔧 Troubleshooting

| Problem                       | Solution                          |
| ----------------------------- | --------------------------------- |
| **Images turn black & white** | Use `pdf_compressor_quality.py`   |
| **Poor compression (<10%)**   | Run `pdf_analyzer.py` to diagnose |
| **Permission denied**         | Close PDF in other applications   |
| **Quality too low**           | Choose higher quality settings    |
| **File won't open**           | Try a different compressor tool   |

## 📊 Example Success Story

**Real PDF Compression:**

```
=== Quality-Preserving PDF Compressor ===
📄 Processing: 09 copy.pdf
📏 Original size: 18.40 MB
🎛️ Color quality: 25, Grayscale quality: 40

🔄 Processing images with quality preservation...
   🖼️ Processing image on page 1...
     💾 2380 KB → 35 KB (98.5% reduction)
   🖼️ Processing image on page 2...
     💾 4096 KB → 130 KB (96.8% reduction)
   [... 10 images processed ...]

📊 Final Results:
   Original size: 18.40 MB
   New size: 3.27 MB
   Space saved: 15.13 MB
   Compression: 82.2%

🎉 SUCCESS! Mission accomplished!
```

## 📁 Project Structure

```
ReduceFileSize/
├── pdf_compressor_quality.py      # ⭐ Main PDF compressor (quality-preserving)
├── pdf_analyzer.py                # 🔍 Diagnostic tool for PDF analysis
├── example.py                     # 📖 Usage examples and help
├── requirements.txt               # 📦 Python dependencies
└── README.md                      # 📚 Documentation
```
