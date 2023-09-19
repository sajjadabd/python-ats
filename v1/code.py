import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
from colorama import Fore, init
import os  # Import the os module

# Initialize colorama for colored output
init(autoreset=True)

# Function to check keywords in the PDF file
def check_keywords(pdf_file, keywords_file):
    try:
        pdf = PdfReader(pdf_file)
        with open(keywords_file, 'r') as keyword_file:
            keywords = keyword_file.read().splitlines()

        keyword_existence = {}
        for keyword in keywords:
            found = False
            for page in pdf.pages:
                text = page.extract_text()
                if keyword in text:
                    found = True
                    break
            keyword_existence[keyword] = found

        return keyword_existence

    except Exception as e:
        print("An error occurred:", e)
        return {}


def find_pdf_file():
    current_directory = os.getcwd()
    pdf_files = [file for file in os.listdir(current_directory) if file.endswith(".pdf")]
    
    if pdf_files:
        pdf_file_path = os.path.join(current_directory, pdf_files[0])
        return pdf_file_path
    else:
        return None




def find_txt_file():
    current_directory = os.getcwd()
    txt_files = [file for file in os.listdir(current_directory) if file.endswith(".txt")]
    
    if txt_files:
        txt_file_path = os.path.join(current_directory, txt_files[0])
        return txt_file_path
    else:
        return None


# Function to browse for files and display results in the command prompt
def browse_files():
    # Get the current directory
    current_directory = os.getcwd()
    

    # Construct file paths for PDF and keywords text file in the current directory
    pdf_file_path = os.path.join(find_pdf_file())
    keywords_file_path = os.path.join(find_txt_file())

    # Check if the files exist in the current directory
    if os.path.isfile(pdf_file_path) and os.path.isfile(keywords_file_path):
        keyword_existence = check_keywords(pdf_file_path, keywords_file_path)

        print("Keyword Existence Report:")
        for keyword, exists in keyword_existence.items():
            if exists:
                print(Fore.GREEN + f"✓ {keyword}")
            else:
                print(Fore.RED + f"✗ {keyword}")
    else:
        print("PDF file (example.pdf) or keywords file (keywords.txt) not found in the current directory.")


browse_files()



input()
"""
# Create the tkinter window
window = tk.Tk()
window.title("PDF Keyword Checker")

# Set the window size
window.geometry("500x300")  # Width x Height

# Create a "Check Keywords" button
browse_button = tk.Button(window, text="Check Keywords", command=browse_files)
browse_button.pack(padx=20, pady=20)

# Start the tkinter main loop
window.mainloop()

"""