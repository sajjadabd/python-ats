import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
from colorama import Fore, init
import os  # Import the os module
import re 

# Initialize colorama for colored output
init(autoreset=True)

#keywords = []


def is_substring(string, substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            return True
    return False

# Function to check keywords in the PDF file
def check_keywords(pdf_file, keywords_file):
    #global keywords
    try:
        pdf = PdfReader(pdf_file)
        with open(keywords_file, 'r') as keyword_file:
            keywords = keyword_file.read().splitlines()
           
        
        keyword_existence = {}
        #print(keywords)
        for keyword in keywords:
            target = keyword#.lower()
            found = False
            longest_substring = ""
            for page in pdf.pages:
                text = page.extract_text()
                for i in range(len(target)+1) :
                    if target[0:i] in text :
                    #if keyword.lower() in text.lower():
                    #if text.lower().__contains__(keyword.lower()):
                    #if is_substring(text.lower(),keyword.lower()) :
                        longest_substring = target[0:i]
                        found = True
                    else :
                        break
            keyword_existence[keyword] = {
                'found' : found ,
                'substring' : longest_substring
            }

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
        
        counter = 0
        trueCounter = 0
        falseCounter = 0
        
        print("Keyword Existence Report:")
        
        """
        print(len(keyword_existence))
        counter = 0
        while counter < len(keyword_existence) :
            print(keyword_existence[counter])
            counter+=1;
        """
        
        
        counter = 0
        matched_words = 0
        unmatched_words = 0
        total_words = 0
        
        for keyword in keyword_existence:
            counter += 1
            
            matched_words += len(keyword_existence[keyword]['substring'])
            unmatched_words += len(keyword) - len(keyword_existence[keyword]['substring'])
            total_words += len(keyword)
            
            if len(keyword) == len(keyword_existence[keyword]['substring']) :
                #print(keyword_existence[keyword])
                print(keyword , end='\r')
                print(Fore.GREEN + keyword[0:len(keyword_existence[keyword]['substring'])] , end='\n')
                #print(Fore.GREEN + keyword_existence[keyword]['substring'] , end='\n')
        
        for keyword in keyword_existence:
            
            if len(keyword) != len(keyword_existence[keyword]['substring']) :
                #print(keyword_existence[keyword])
                print(keyword , end='\r')
                print(Fore.GREEN + keyword[0:len(keyword_existence[keyword]['substring'])] , end='\n')
        
        
        """
        for keyword, exists in keyword_existence.items():
            if exists:
                counter += 1
                trueCounter += 1
                print(Fore.GREEN + f"✓ {keyword}")
            else:
                pass
                
                
        for keyword, exists in keyword_existence.items():
            if exists:
                pass
            else:
                counter += 1
                falseCounter += 1
                print(Fore.RED + f"✗ {keyword}")
        """
    else:
        print("PDF file (example.pdf) or keywords file (keywords.txt) not found in the current directory.")

    # Initialize counters for true and false keywords
    #total_keywords = len(keyword_existence)
    #true_keywords = sum(keyword_existence.values())
    #false_keywords = total_keywords - true_keywords

    # Calculate percentages
    #true_percentage = (true_keywords / total_keywords) * 100
    #false_percentage = (false_keywords / total_keywords) * 100
    
    #true_percentage = (trueCounter / counter) * 100
    #false_percentage = (falseCounter / counter) * 100
    
    true_percentage = ( matched_words / total_words ) * 100
    false_percentage = ( unmatched_words / total_words ) * 100

    # Print the table
    print("\nKeyword Occurrence Percentages:")
    print("+-----------------+----------------------+")
    print("     Keyword      |       Percentage     ")
    print("+-----------------+----------------------+")
    print(f"       True       |        {true_percentage:.2f}%        ")
    print(f"       False      |        {false_percentage:.2f}%        ")
    print("+-----------------+----------------------+")
    
    
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