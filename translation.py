import os
from transformers import MarianMTModel, MarianTokenizer

# Translation Function
def translate_hindi_to_english(hindi_text):
    """Translates Hindi text to English."""
    model_name = 'Helsinki-NLP/opus-mt-hi-en'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Tokenize and translate
    tokens = tokenizer(hindi_text, return_tensors='pt', padding=True, truncation=True)
    translated = model.generate(**tokens)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    return translated_text

# Processing Files
def process_folder(input_folder, output_folder):
    """Processes all files in the input folder and saves the translated files to output folder."""
    
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    for subfolder in os.listdir(input_folder):
        subfolder_path = os.path.join(input_folder, subfolder)
        
        if os.path.isdir(subfolder_path):
            # Create matching subfolder in the translated directory
            translated_subfolder = os.path.join(output_folder, subfolder)
            os.makedirs(translated_subfolder, exist_ok=True)

            # Iterate through each file in the subfolder
            for filename in os.listdir(subfolder_path):
                if filename.endswith('.txt'):
                    input_file_path = os.path.join(subfolder_path, filename)
                    output_file_path = os.path.join(translated_subfolder, filename.replace('.txt', '_translated.txt'))

                    with open(input_file_path, 'r', encoding='utf-8') as file:
                        hindi_text = file.read()

                    # Translate the text
                    translated_text = translate_hindi_to_english(hindi_text)

                    # Save the translated text
                    with open(output_file_path, 'w', encoding='utf-8') as out_file:
                        out_file.write(translated_text)

                    print(f"Translated: {input_file_path} → {output_file_path}")

# Main Execution
if __name__ == "__main__":
    input_dir = "outputtext"      # Your source directory with Hindi text
    output_dir = "translated"     # Destination folder for translated text

    process_folder(input_dir, output_dir)

    print("\n✅ Translation completed successfully!")
