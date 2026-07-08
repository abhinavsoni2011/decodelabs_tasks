"""
=========================================================
Artificial Intelligence Project 4
Title : Image Text Recognition Using OCR
Author : Abhinav Soni
Internship : DecodeLabs AI Internship
=========================================================
"""

import cv2
import pytesseract

# Load Image
image = cv2.imread("dataset/sample_image.png")

# Check Image
if image is None:
    print("Error: Image not found!")
    exit()

# Convert to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Threshold
threshold = cv2.threshold(
    gray,
    150,
    255,
    cv2.THRESH_BINARY
)[1]

# Extract Text
text = pytesseract.image_to_string(threshold)

print("=" * 60)
print("EXTRACTED TEXT")
print("=" * 60)
print(text)

# Save Extracted Text
with open("output/extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

# Save Processed Image
cv2.imwrite("output/output_image.png", threshold)

print("\nProject Completed Successfully.")
