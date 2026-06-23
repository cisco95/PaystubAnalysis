import pdfplumber #pip install pdfplumber

def pdfProcessor(file_path):
        storage = []
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
        return storage