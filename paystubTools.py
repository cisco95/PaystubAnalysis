import pdfplumber #pip install pdfplumber
import pandas as pd

def pdfProcessor(file_path):
        storage = []
        fullTables = []
        with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                        for table in page.extract_tables():
                                clean_table = [row for row in table if any(cell is not None and cell.strip() != "" for cell in row)]
                                clean_table = [[cell if cell is not None else "" for cell in row] for row in table]
                                fullTables.append(table)
                                for row in clean_table:
                                        temp = []
                                        for item in row:
                                                if item:
                                                        temp.append(item)
                                        storage.append(temp)
                                        temp = []
        return fullTables



def makeTables(scrapedData):
        listOfTables = []
        scrapedData.pop(0)
        for row in scrapedData:
                tableName = row[0][0]
                tableHeaders = row[2][:-1]
                tableData = [r[:-1] for r in row[3:]]

                # print(f"Table Name: {tableName}")
                # print(f"Table Headers: {tableHeaders}")
                # print(f"Table Data: {tableData}")

                df = pd.DataFrame(tableData, columns=[header for header in tableHeaders])
                listOfTables.append((tableName, df))

        return listOfTables



                

