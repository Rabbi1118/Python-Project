import PyPDF2

# Open the PDF files that you want to merge
pdf1 = open('Input_location', 'rb')
pdf2 = open('Input_location', 'rb')

# Create a PDF merger object
pdf_merger = PyPDF2.PdfMerger()

# Add the PDF files to the merger object
pdf_merger.append(pdf1)
pdf_merger.append(pdf2)

# Write the merged PDF to a new file
merged_pdf = open('Output_location', 'wb')
pdf_merger.write(merged_pdf)

# Close the PDF files
pdf1.close()
pdf2.close()
merged_pdf.close()
