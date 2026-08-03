# Image or Text Recognition System
## Project Description
The Image or Text Recognition System is a Python-based Optical Character Recognition (OCR) project that extracts readable text from an image.
The project uses image preprocessing techniques to improve text recognition accuracy. 
The input image is converted to grayscale, enlarged internally, blurred, and processed using Otsu thresholding before the text is extracted using Tesseract OCR.

## Features
- Loads an image using OpenCV
- Converts the image to grayscale
- Selects the text paragraph for OCR
- Enlarges the selected text region internally
- Applies Gaussian blur to reduce image noise
- Uses Otsu thresholding for clearer text
- Extracts text using Tesseract OCR
- Displays the original image and processed image
- Prints the extracted text in the terminal

## Technologies Used
- Python
- OpenCV
- Pytesseract
- Tesseract OCR

Installation
Install the required Python libraries:
pip install opencv-python pytesseract

How to Run:
Open the terminal inside the project folder and run:
python recognition.py

## Project Files
```text
Image or Text Recognition/
├── recognition.py
├── sample_image.png
└── README.md
