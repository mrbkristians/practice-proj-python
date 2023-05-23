from PyPDF4 import PdfFileMerger
import os

#var = os.getcwd() For extracting current working directory
merger = PdfFileMerger()

for items in os.listdir():
    if items.endswith(".pdf"):
        merger.append(items)

merger.write("final-project.pdf")
merger.close()

for items in os.listdir():
    if items != ("final-project.pdf") and items.endswith(".pdf"):
        os.remove(items)
