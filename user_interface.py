import tkinter as tk
from tkinter import filedialog

def test():
        print("Test Successful")

def promptUser():
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(
        title = "Select a File",
        filetypes=[("PDF Files", "*.pdf")]
        )

        if file_path:
                return file_path

        return None