#!/usr/bin/env python3
"""
Example usage of the PDF compressor
"""

import os
from pdf_compressor import PDFCompressor

def example_usage():
    """Demonstrate how to use the PDFCompressor class programmatically."""
    
    # Example 1: Basic compression
    print("=== PDF Compressor Example ===\n")
    
    # Create compressor instance with different quality settings
    compressor_high = PDFCompressor(quality=50)  # Higher quality, larger file
    compressor_medium = PDFCompressor(quality=30)  # Balanced (default)
    compressor_low = PDFCompressor(quality=15)   # Maximum compression
    
    # Example file path (you would replace this with your actual PDF path)
    input_file = "example.pdf"  # Replace with your PDF path
    
    print(f"To use this program, run one of these commands:")
    print(f"")
    print(f"1. Basic usage (compress with default settings):")
    print(f"   python pdf_compressor.py \"{input_file}\"")
    print(f"")
    print(f"2. High compression (quality 15, max 2MB result):")
    print(f"   python pdf_compressor.py \"{input_file}\" -q 15 --max-width 800")
    print(f"")
    print(f"3. Balanced compression (quality 30, ~3-4MB result):")
    print(f"   python pdf_compressor.py \"{input_file}\" -q 30")
    print(f"")
    print(f"4. Specify output file:")
    print(f"   python pdf_compressor.py \"{input_file}\" -o \"compressed_output.pdf\"")
    print(f"")
    print(f"Replace '{input_file}' with the path to your actual PDF file.")
    print(f"")
    print(f"For an 18MB PDF, these settings typically produce:")
    print(f"- Quality 15: ~1-2MB (maximum compression)")
    print(f"- Quality 30: ~2-4MB (recommended balance)")
    print(f"- Quality 50: ~4-6MB (higher quality)")

if __name__ == "__main__":
    example_usage()