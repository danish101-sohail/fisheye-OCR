import cv2
import os

def segment_image(image_path):
    # Clear previous image segments
    output_dir = "app/static/images"
    if os.path.exists(output_dir):
        for file in os.listdir(output_dir):
            file_path = os.path.join(output_dir, file)
            os.remove(file_path)

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply adaptive thresholding
    thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    
    # Perform morphological operations to reduce noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)

    # Find contours
    contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    segmented_images = []
    base_filename = os.path.splitext(os.path.basename(image_path))[0]
    output_dir = "app/static/images"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        segmented_image = image[y:y+h, x:x+w]
        segmented_image_path = os.path.join(output_dir, f"{base_filename}_segment_{i}.png")
        cv2.imwrite(segmented_image_path, segmented_image)
        segmented_images.append(segmented_image_path)

    return segmented_images
