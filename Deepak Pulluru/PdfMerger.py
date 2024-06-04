def merge_pdfs(pdf_files, output_file):
    # Open the output file in binary write mode
    with open(output_file, 'wb') as out_file:
        for pdf_file in pdf_files:
            # Open each input PDF file in binary read mode
            with open(pdf_file, 'rb') as in_file:
                # Read the content of the input PDF file
                pdf_content = in_file.read()
                # Write the content to the output PDF file
                out_file.write(pdf_content)

# List of PDF files to merge
pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']

# Output file name for the merged PDF
output_file = 'merged_file.pdf'

# Call the merge_pdfs function
merge_pdfs(pdf_files, output_file)

print("PDFs merged successfully!")
