from paystubTools import *;
import tkinter as tk
from tkinter import filedialog
import pdfplumber #pip install pdfplumber

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title = "Select a File",
    filetypes=[("PDF Files", "*.pdf")]
)

if file_path:
        print(f"Selected file: {file_path}")

storage = []

# pdf = pdfplumber.open(file_path)
# page = pdf.pages[0]
# im = page.to_image(resolution=150)
# im.reset().debug_tablefinder()
# im.save("debug.png")

with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
                for table in page.extract_tables():
                        clean_table = [row for row in table if any(cell is not None and cell.strip() != "" for cell in row)]
                        clean_table = [[cell if cell is not None else "" for cell in row] for row in table]
                        
                        for row in clean_table:
                                temp = []
                                for item in row:
                                        if item:
                                                temp.append(item)
                                storage.append(temp)
                                temp = []

with open("output.txt", "w") as file:
        for row in storage:
                file.write(f"{row}\n")