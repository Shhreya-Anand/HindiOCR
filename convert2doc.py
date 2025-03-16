import os
from docx import Document

def convert_txt_to_docx(input_folder, output_folder):
    try:
        # Check if the output folder exists, if not, create it
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Iterate over each file in the input folder
        for text_file in os.listdir(input_folder):
            # Only process .txt files
            if text_file.endswith('.txt'):
                file_path = os.path.join(input_folder, text_file)
                
                # Create a new Document for each .txt file
                doc = Document()
                
                # Open the .txt file and read its content
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Add a title to the document (file name)
                    doc.add_paragraph(f"--- Start of {text_file} ---\n")
                    
                    # Add the content of the .txt file to the document
                    doc.add_paragraph(file.read())
                    
                    # Save the document as a .docx file with the same name
                    output_file = os.path.join(output_folder, f"{text_file[:-4]}.docx")
                    doc.save(output_file)
                    print(f"Created {output_file}")
    
    except Exception as e:
        print(f"Error: {e}")

# Define the folder containing your individual .txt files
input_folder = "/Users/shhreya/hindi-ocr/outputtext"  # Change this to your input text files folder

# Define the folder where you want the .docx files to be saved
output_folder = "/Users/shhreya/hindi-ocr/output_docs"  # Change this to your desired output folder

# Call the function to convert the text files to .docx files
convert_txt_to_docx(input_folder, output_folder)
