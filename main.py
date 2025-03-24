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
    # Path to your images
    base_input_path = "/Users/shhreya/hindi-ocr/inputtext/part1:4"
    base_output_path = "/Users/shhreya/hindi-ocr/outputtext/part1:4"

    # Ensure the base output directory exists
    os.makedirs(base_output_path, exist_ok=True)

    # Walk through the entire input directory- use os.walk
    for root, _, files in os.walk(base_input_path):
        for image_name in files:
            if not image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.heic')):  # Handle image formats, but fin fact heic doesnt work
                continue

            input_path = os.path.join(root, image_name)

            # Get the relative path of the image (e.g., part1/4)
            relative_path = os.path.relpath(root, base_input_path)

            # Create the corresponding output folder
            output_folder = os.path.join(base_output_path, relative_path)
            os.makedirs(output_folder, exist_ok=True)

            try:
                # Preprocess the image
                img = preprocess_image(input_path)

                # Perform OCR
                text = pt.image_to_string(img, lang="hin")

                # Save the output text
                image_name_without_ext = os.path.splitext(image_name)[0]  # Remove the file extension
                output_file_path = os.path.join(output_folder, f"{image_name_without_ext}.txt")

                with open(output_file_path, "w", encoding='utf-8') as file:
                    file.write(text)

                print(f"Text extracted from {image_name} and saved to {output_file_path}")

            except Exception as e:
                print(f"Error processing {image_name}: {e}")

if __name__ == '__main__':
    main()
