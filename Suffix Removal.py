pip install python-docx

import re
from docx import Document

def find_root_form(word):
    # Regular expressions to match different suffixes
    suffixes = ['s', 'es', 'ies', 'ed', 'ied', 'ing']
    for suffix in suffixes:
        if word.endswith(suffix):
            root_form = word[:-len(suffix)]
            return root_form
    return word

def main():
    file_path = input("Enter the path to the Word document: ")
    
    # Read the Word document
    try:
        document = Document(file_path)
    except Exception as e:
        print("Error: Unable to read the Word document.")
        return
    
    words_list = []
    
    # Loop through paragraphs in the document
    for paragraph in document.paragraphs:
        words = re.findall(r'\b\w+\b', paragraph.text)
        for word in words:
            root_form = find_root_form(word)
            words_list.append(root_form)
    
    # Print the list of words with simple root forms
    print("List of words with simple root forms:")
    print(words_list)

if __name__ == "__main__":
    main()
