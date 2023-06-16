import csv
from pdfminer.high_level import extract_text
import pytesseract
from PIL import Image


def extract_text(img, output):
    conf = r"--psm 6 --oem 3"

    #Extract text from Image
    text = pytesseract.image_to_string(Image.open("sample1.png"), config=conf)

    #write extracted text into .csv file
    with open(output, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Extracted Text"])
        writer.writerow([text])

    print("Saved into CSV")



def extract_pdf_to_csv(pdf_file, csv_file):
    # extract text from pdf
    text = extract_text(pdf_file)
    # splits the extracted text into individual lines 
    lines = text.split('\n')
    headers = []
    rows = []
    header_found = False

    for line in lines:
        if line.strip() != '':
            if not header_found:
                headers.append(line)
                if len(headers) > 1:
                    header_found = True
            else:
                rows.append(line.split())

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)


#Extract Text from Image
img = "sample2.png"
output = "output1.csv"
extract_text(img, output)



# Extract Text from PDF
pdf_file = "sample1.pdf"
csv_file = "output1.csv"
extract_pdf_to_csv(pdf_file, csv_file)
print("Text extracted and saved to", csv_file)
