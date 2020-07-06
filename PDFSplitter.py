
import sys
import os
import PyPDF2
from pathlib import Path

# Getting PDF file information
name = input("Input the exact name of the PDF file to be split: ")
downloadFolder = str(os.path.join(Path.home(), "Downloads"))
os.chdir(downloadFolder)
filePath = os.path.abspath(name)

# Making sure path exists
if not os.path.exists(filePath):
    print("File not found")
    sys.exit()

# Setting up variables for PDF file
pdfFile = open(filePath, "rb")
reader = PyPDF2.PdfFileReader(pdfFile)
pages = reader.numPages

# How many times to split
times = int(input("How many times do you want to split the PDF? "))
print()

# Looping through and making new PDFs
for i in range(times):
    writer = PyPDF2.PdfFileWriter()
    print("Split \#" + str(i + 1))
    start = int(input("Start page: ")) - 1
    if start < 0 or start > pages - 1:
        sys.exit()
    end = int(input("End page: ")) - 1
    if end < 0 or end > pages - 1 or end < start:
        sys.exit()
    for n in range(start, end + 1):
        page = reader.getPage(n)
        writer.addPage(page)
    fileName = name[:len(name) - 4] + "_" + str(start + 1) + "_" + str(end + 1) + ".pdf"
    outputFile = open(fileName, "wb")
    writer.write(outputFile)
    outputFile.close()
pdfFile.close()
