import os
from PyPDF2 import PdfMerger

def merge_pdfs(folder_path, output_filename):
    merger = PdfMerger()

    #Get only .pdf files in the folder
    try:
        pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    except FileNotFoundError:
        print("Folder not found. Please check the path.")
        return
    except OSError as e:
        print(f"Error reading folder: {e}")
        return

    if not pdf_files:
        print("No PDF files found in the folder.")
        return

    pdf_files.sort() #Alphabetical order

    print("n Merging the following pdfs:n")
    for pdf in pdf_files:
        print(f" - {pdf}")
        merger.append(os.path.join(folder_path, pdf))

    #ensure output filename  ends with .pdf
    if not output_filename.lower().enswith(' .pdf'):
        output_filename += '.pdf'

    output_path = os.path.join(folder_path, output_filename)

    try:
        merger.write(output_path)
        print(f"Merged PDF created : {output_path}")
    except Exception as e:
        print(f"Failed to merge pdf: {e}")
    finally:
        merger.close()

if __name__ == "__main__":
    folder = input("Enter the folder path containing PDFs: ").strip('"').strip()
    output_name = input("Enter the output PDF file name (e.g.,merged.pdf): ").strip()
    merge_pdfs(folder, output_name)