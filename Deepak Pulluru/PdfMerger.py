import PyPDF2
import os
def merge_pdfs(pdf_list, output_path):
    pdf_writer = PyPDF2.PdfFileWriter()
    
    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfFileReader(pdf)
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)
    
    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
    
    print(f"Merged {len(pdf_list)} PDFs into {output_path}")
def split_pdf(pdf_path, output_dir, split_at_page):
    pdf_reader = PyPDF2.PdfFileReader(pdf_path)
    
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    pdf_writer1 = PyPDF2.PdfFileWriter()
    pdf_writer2 = PyPDF2.PdfFileWriter()
    
    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        if page_num < split_at_page:
            pdf_writer1.addPage(page)
        else:
            pdf_writer2.addPage(page)
    
    output_path1 = os.path.join(output_dir, f"{base_name}_part1.pdf")
    output_path2 = os.path.join(output_dir, f"{base_name}_part2.pdf")
    
    with open(output_path1, 'wb') as output_pdf1:
        pdf_writer1.write(output_pdf1)
    
    with open(output_path2, 'wb') as output_pdf2:
        pdf_writer2.write(output_pdf2)
    
    print(f"Split {pdf_path} into {output_path1} and {output_path2}")
if __name__ == "__main__":
    pdfs_to_merge = ['file1.pdf', 'file2.pdf', 'file3.pdf']  
    merged_output = 'merged.pdf'
    merge_pdfs(pdfs_to_merge, merged_output)
    pdf_to_split = 'example.pdf'  
    output_directory = '.'
    split_page_number = 5  
    split_pdf(pdf_to_split, output_directory, split_page_number)

