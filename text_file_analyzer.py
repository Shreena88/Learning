import string
from collections import Counter
from docx import Document

def clean_text(text):
    """Remove punctuation and convert text to lowercase"""
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator).lower()

def read_docx(file_path):
    """Extract text from a DOCX file"""
    doc = Document(file_path)
    full_text = [para.text for para in doc.paragraphs]
    return 'n'.join(full_text)

def analyze_text_file(file_path):
    try:
        #Read content based on file extension
        if file_path.endswith('.docx'):
            content = read_docx(file_path)
        elif file_path.endswith('.txt'):
            with open(file_path, 'r',encoding='utf-8') as file:
                content = file.read()
        else:
            print("Unsupported file format.Please use .txt or .docx")
            return

        lines = content.splitlines()
        words = content.split()
        cleaned_words = clean_text(content).split()

        total_chars = len(content)
        total_chars_no_spaces = len(content.replace(" ","").replace("n",""))

        word_freq = Counter(cleaned_words)

        #output the results
        print("File Analysis Result:")
        print(f"Total Lines: {len(lines)}")
        print(f"Total Words: {len(words)}")
        print(f"Total Characters(with space): {total_chars}")
        print(f"Total Characters(no space): {total_chars_no_spaces}")
        print("Top 10 Most common words:")
        for words,freq in word_freq.most_common(10):
            print(f"{words}: {freq} times")

    except FileNotFoundError:
        print("File not found.Please check the path")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    path = input("Enter the file path to the .txt or .docx file: ")
    analyze_text_file(path)