import re
import pdfplumber
# import tabula

# creating object for the file
file = './Invoices/default.pdf'
# get regex for getting data 


with pdfplumber.open(file) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()
    # print(text.lower())
    invoice_regex = "(?:(tax.*:\s*\d+-\d+)|(tax.*\d+))"
    date_regex = "(?:(\d{1,2}\/\d{1,2}\/\d{2,4})|(\d{1,2}−[a-zA-Z]{3,9}−\d{2,4}))"

    # for line in text:
    result_invoice =  re.findall(invoice_regex,text.lower())[-1]
    result_date = re.findall(date_regex,text.lower())[-1]

    if result_invoice[-1] != "":
        print('yes')
        # result_invoice = 
    else:
        print('No')
        
    print(result_invoice[-1],result_date[-1])

    import tabula

    df = tabula.read_pdf(file,output_format="json")
    df.head()

    # tabula.convert_into("offense.pdf", "offense_testing.xlsx", output_format="xlsx")