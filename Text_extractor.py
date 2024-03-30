# importing modules

from PyPDF2 import PdfReader

def extract_text(page_number, filename):

    if not filename:
        print("Please enter a file name.")
        return

# creating a pdf reader object
    reader = PdfReader(filename)

# printing number of pages in pdf file

    total_page = str(len(reader.pages))
    print("The number of page is " + total_page + ".")

# getting a specific page from the pdf file
    try:
        page = reader.pages[int(page_number) - 1]
    except IndexError:
        print("Oops! please check the number of pages")
    else:
    # extracting text from page

        text = page.extract_text()
        print(text)
        
        f = open('output.txt', 'w')
        print(text, file=f)


