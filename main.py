from paystubTools import *
import user_interface

def printPDFContentsToText(storage, outputFileName):
        with open(f"{outputFileName}.txt", "w") as file:
                for row in storage:
                        file.write(f"{row}\n")

        print("Done!")


if __name__ == "__main__":
        user_interface.test()
        filename = user_interface.promptUser()
        PDFTableItemsList = pdfProcessor(filename)
        printPDFContentsToText(PDFTableItemsList, "testOutputs")
        listOfTables = makeTables(PDFTableItemsList)
        # printPDFContentsToText(listOfTables, "testOutputs")
        for item in listOfTables:
                print(f"Table Name: {item[0]}")
                print(f"Table Data:\n {item[1]}")
        





