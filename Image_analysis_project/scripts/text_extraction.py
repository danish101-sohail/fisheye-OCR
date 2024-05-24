import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

def extract_text(image_path):
    image = Image.open(image_path)
    
    # Preprocess the image: convert to grayscale, enhance contrast, apply filters
    image = image.convert('L')  # Convert to grayscale
    image = ImageEnhance.Contrast(image).enhance(2)  # Enhance contrast
    image = image.filter(ImageFilter.SHARPEN)  # Apply sharpen filter
    
    text = pytesseract.image_to_string(image)
    return text
