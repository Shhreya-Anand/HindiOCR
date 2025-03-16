from PIL import Image, ImageEnhance
import pytesseract as pt
import os

def preprocess_image(input_path):
    img = Image.open(input_path)
    # Convert to grayscale
    img = img.convert("L")

    # Optionally apply enhancement to improve contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)  # Adjust the contrast factor as needed

    # Apply thresholding to get a binary image (black & white)
    img = img.point(lambda p: p > 128 and 255)  # Adjust the threshold value as needed
    return img

def main():
    # path to your images
    path = "/Users/shhreya/hindi-ocr/inputtext/introduction"
    tempPath = "/Users/shhreya/hindi-ocr/outputtext"

    if not os.path.exists(tempPath):
        os.makedirs(tempPath)

    for image_name in os.listdir(path):
        input_path = os.path.join(path, image_name)
        
        if not image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.HEIC')):
            continue

        try:
            # Preprocess the image
            img = preprocess_image(input_path)

            # Perform OCR
            text = pt.image_to_string(img, lang="hin")
            
            # Save the output text
            image_name_without_ext = image_name[0:-4]  # Remove the file extension
            output_file_path = os.path.join(tempPath, image_name_without_ext + ".txt")

            with open(output_file_path, "w", encoding='utf-8') as file:
                file.write(text)

            print(f"Text extracted from {image_name} and saved to {output_file_path}")
        
        except Exception as e:
            print(f"Error processing {image_name}: {e}")

if __name__ == '__main__':
    main()
