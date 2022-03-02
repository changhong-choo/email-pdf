
# 1. Split the pdf source by page and save in the directory as individual file.
    
from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("file_name - Sample.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("document-page%s.pdf" % (i+1), "wb") as outputStream:
        output.write(outputStream)


# 2. Get the recipients' from email listing
import pandas as pd

df = pd.read_csv(r'Excel Listing - Sample.csv')

# 3. Send email to receipients with pdf attachment
import smtplib
import os
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
directory = r'your_file_directory'


for row in df.index:
    
    receivers = df['EMAIL'][row]

    msg = EmailMessage()
    msg['Subject'] = 'Email Subject'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = receivers
    
    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <p>Hi,</p>
            <p>Attached the copy of PDF file.</p>
        </body>
    </html>
    """, subtype='html')
    
    file = "document-page{}.pdf".format(row+1)
    f = os.path.join(directory, file)
    
    with open(f, 'rb') as f:
        file_data = f.read()
        file_name = 'filename.pdf'
        
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    
    try:
        # Connect to gmail server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:   
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
            smtp.send_message(msg)
    except:
        pass
