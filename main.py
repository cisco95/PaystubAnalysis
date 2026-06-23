import paystubTools
import user_interface

def printPDFContentsToText(storage, outputFileName):
        with open(f"{outputFileName}.txt", "w") as file:
                for row in storage:
                        file.write(f"{row}\n")

        print("Done!")


if __name__ == "__main__":
        user_interface.test()
        filename = user_interface.promptUser()
        PDFTableItemsList = paystubTools.pdfProcessor(filename)
        printPDFContentsToText(PDFTableItemsList, "testOutputs")






