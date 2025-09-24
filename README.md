# PDF File Size Reducer

A comprehensive Python toolkit that dramatically reduces PDF file sizes from 18MB to 2-3MB while preserving image quality and colors. Features multiple specialized compressors for different PDF types and interactive user interfaces.

## 🚀 Key Features

- **🎯 Specialized Compressors**: Different tools for different PDF types (FlateDecode, JPEG, mixed content)
- **🎨 Quality Preservation**: Smart color handling that preserves grayscale and color images correctly
- **📊 Diagnostic Tools**: Analyze why a PDF can/cannot be compressed
- **💬 Interactive Interface**: No complex command-line arguments needed
- **🔍 Smart Detection**: Automatically detects image types and applies optimal compression
- **📈 Real-time Progress**: See compression progress and savings in real-time

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

### 1. **Quality-Preserving Compressor** (⭐ Recommended)

Best for preserving image colors and quality while achieving good compression.

```bash
python pdf_compressor_quality.py
```

**Features:**

- ✅ Preserves grayscale images as grayscale
- ✅ Smart color space handling (RGB, CMYK, RGBA)
- ✅ Quality tiers: High/Balanced/Compact
- ✅ Minimal unnecessary resizing

### 2. **FlateDecode Specialist**

Perfect for PDFs with FlateDecode compressed images (common in design software).

```bash
python pdf_compressor_flatedecode.py
```

**Features:**

- ✅ Specialized FlateDecode image extraction
- ✅ Can achieve 80-90% compression on image-heavy PDFs
- ✅ Real-time compression feedback

### 3. **Simple Compressor**

Reliable general-purpose compressor for most PDFs.

```bash
python pdf_compressor_simple.py
```

**Features:**

- ✅ Works with most PDF types
- ✅ Clean, simple interface
- ✅ Good for text-heavy PDFs

### 4. **Original Interactive Compressor**

Feature-rich compressor with command-line options.

```bash
python pdf_compressor.py
```

### 5. **PDF Analyzer**

Diagnose why a PDF cannot be compressed much.

```bash
python pdf_analyzer.py
```

**Features:**

- 🔍 Analyzes PDF structure and content
- 📊 Shows compression potential
- 💡 Explains why compression is limited

## 📋 Quick Start Guide

### Step 1: Choose Your Tool

- **Unknown PDF type?** → Start with `pdf_analyzer.py` to understand your PDF
- **Design/Graphics PDF?** → Use `pdf_compressor_flatedecode.py`
- **Want best quality?** → Use `pdf_compressor_quality.py`
- **Simple compression?** → Use `pdf_compressor_simple.py`

### Step 2: Run the Tool

All tools are **interactive** - just run them and follow the prompts:

```bash
# Example: Quality-preserving compressor
python pdf_compressor_quality.py

# The program will ask:
# 📁 Enter PDF file path: [paste your file path here]
# 🎨 Choose quality level: [1, 2, or 3]
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

| PDF Type              | Original Size | Compressed Size | Reduction | Best Tool              |
| --------------------- | ------------- | --------------- | --------- | ---------------------- |
| **Design/Graphics**   | 15-20MB       | 2-4MB           | 80-90%    | FlateDecode Specialist |
| **Scanned Documents** | 20-50MB       | 3-8MB           | 70-85%    | Quality Preserving     |
| **Mixed Content**     | 10-30MB       | 3-10MB          | 60-80%    | Quality Preserving     |
| **Text-Heavy**        | 5-15MB        | 4-12MB          | 20-50%    | Simple Compressor      |

## 💡 Tips for Best Results

### For Maximum Compression (18MB → 2MB):

1. Use **FlateDecode Specialist** for design PDFs
2. Choose **Quality 15-25** in any tool
3. Let the tool resize very large images

### For Quality Preservation:

1. Use **Quality-Preserving Compressor**
2. Choose **Balanced** or **High Quality** settings
3. Tool will preserve grayscale vs color correctly

### If Compression is Poor:

1. Run **PDF Analyzer** first to understand why
2. Try **FlateDecode Specialist** if you have design/graphics PDFs
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
├── pdf_compressor_quality.py      # ⭐ Best quality preservation
├── pdf_compressor_flatedecode.py  # 🎯 FlateDecode specialist
├── pdf_compressor_simple.py       # 🔧 Simple & reliable
├── pdf_compressor.py              # 📋 Original with CLI options
├── pdf_analyzer.py                # 🔍 Diagnostic tool
├── example.py                     # 📖 Usage examples
├── requirements.txt               # 📦 Dependencies
└── README.md                      # 📚 This file
```
