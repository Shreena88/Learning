import PyPDF2

# List of PDFs to merge
pdf_files = ["SL (1).pdf", "SL (2).pdf"]

# Create merger object
merger = PyPDF2.PdfMerger()

# Append each PDF to the merger
for filename in pdf_files:
    with open(filename, 'rb') as file:
        merger.append(file)

# Write the merged output
with open("Merged.pdf", "wb") as output_file:
    merger.write(output_file)

print("PDFs merged successfully into 'Merged.pdf'")
