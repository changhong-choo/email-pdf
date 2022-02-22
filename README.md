# Sending emails with HTML content and PDF attachment
To split multi-pages pdf into individual page and send each pdf to respective recipients from excel listing.

## Description
The program is able to split pdf file into individual file by page and send the file to recipients by email based on the excel listing.
Basically, the first page in pdf will send to first row recipient in the excel file. Files in the data folder is the sample pdf file and excel listing.

## High level plan
1. Split the pdf source into individual file by page.
2. Get the excel listing.
3. Send the email to recipients based on the logic.

## Python Packages Used
1. [os](https://docs.python.org/3/library/os.html) - to get environment variables email address & password, and the path of file location
2. [pandas](https://pandas.pydata.org/) - to work with excel data
3. [PyPDF2](https://pythonhosted.org/PyPDF2/) - to split pdf by page, to get page number
4. [smtplib](https://docs.python.org/3/library/smtplib.html) - to connect to gmail server
5. [email](https://docs.python.org/3/library/email.html) - to make the email parameter and content more neatly

## Getting started
1. Amend the following input to meet your needs:
    - Input your original pdf file that needed to split
    - Input the location to store the individual file
    - Input the excel listing location that consists of recipients' email address
    - Input the email address and password (This information should store in environment variables)
    - Amend the email content
2. Once set, you can run the .py file.
3. Email with pdf attachment will be send out.

## Further improvement
1. Send the email with multiple attachment at once if the email address is the same.
