import cv2
import pytesseract

# Path to Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"D:\DecodeLabs\tesseract.exe"

# Image file name
image_path = "sample_image.png"

# Load image
image = cv2.imread(image_path)

# Check image
if image is None:
    print("Error: Image file not found.")

else:

    # ==================================================
    # 1. CREATE FULL PROCESSED IMAGE FOR DISPLAY
    # ==================================================

    # Convert COMPLETE image to grayscale
    gray_full = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Reduce noise
    blurred_full = cv2.GaussianBlur(
        gray_full,
        (3, 3),
        0
    )

    # Convert COMPLETE image to black and white
    _, processed_full = cv2.threshold(
        blurred_full,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )


    # ==================================================
    # 2. CREATE SEPARATE IMAGE ONLY FOR OCR
    # ==================================================

    # Copy grayscale image for OCR
    ocr_image = gray_full.copy()

    # Enlarge internally for better OCR
    ocr_image = cv2.resize(
        ocr_image,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_CUBIC
    )

    # Get enlarged image dimensions
    height, width = ocr_image.shape

    # Start OCR below the cartoon and include the full paragraph
    start_y = int(height * 0.48)

    paragraph_image = ocr_image[
    start_y:height,
    0:width
    ]

    # Reduce noise
    paragraph_blurred = cv2.GaussianBlur(
        paragraph_image,
        (3, 3),
        0
    )

    # Threshold paragraph for OCR
    _, paragraph_processed = cv2.threshold(
        paragraph_blurred,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )


    # ==================================================
    # 3. EXTRACT TEXT
    # ==================================================

    extracted_text = pytesseract.image_to_string(
        paragraph_processed,
        config="--psm 6"
    )


    # ==================================================
    # 4. PRINT OUTPUT
    # ==================================================

    print("\n" + "=" * 55)
    print("          IMAGE TEXT RECOGNITION SYSTEM")
    print("=" * 55)

    print("\n[ IMAGE PREPROCESSING ]")
    print("-" * 30)

    print("✓ Image loaded successfully")
    print("✓ Grayscale conversion completed")
    print("✓ Complete image processed for display")
    print("✓ Paragraph selected for OCR")
    print("✓ Image enlarged internally for OCR accuracy")
    print("✓ Gaussian blur applied")
    print("✓ Otsu thresholding completed")
    print("✓ OCR page segmentation mode applied")

    print("\n[ EXTRACTED TEXT ]")
    print("-" * 30)

    if extracted_text.strip():
        print(extracted_text.strip())
    else:
        print("No readable text was detected.")

    print("\n" + "=" * 55)


    # ==================================================
    # 5. RESIZE COMPLETE IMAGES FOR DISPLAY
    # ==================================================

    # Both images will fit completely inside their windows
    display_original = cv2.resize(
        image,
        (400, 600),
        interpolation=cv2.INTER_AREA
    )

    display_processed = cv2.resize(
        processed_full,
        (400, 600),
        interpolation=cv2.INTER_AREA
    )


    # ==================================================
    # 6. CREATE TWO SEPARATE WINDOWS
    # ==================================================

    cv2.namedWindow(
        "Original Image",
        cv2.WINDOW_NORMAL
    )

    cv2.namedWindow(
        "Processed Image",
        cv2.WINDOW_NORMAL
    )

    # Set both window sizes
    cv2.resizeWindow(
        "Original Image",
        400,
        600
    )

    cv2.resizeWindow(
        "Processed Image",
        400,
        600
    )

    # Place windows separately
    cv2.moveWindow(
        "Original Image",
        50,
        50
    )

    cv2.moveWindow(
        "Processed Image",
        500,
        50
    )

    # Show complete images
    cv2.imshow(
        "Original Image",
        display_original
    )

    cv2.imshow(
        "Processed Image",
        display_processed
    )

    # Keep windows open
    cv2.waitKey(0)

    # Close windows
    cv2.destroyAllWindows()