# Sending emails with HTML content and PDF attachment
To split multi-pages pdf into individual page and send each pdf to respective recipients from excel listing.


## Description
The program is able to split pdf file into individual file by page with [PyPDF2](https://pythonhosted.org/PyPDF2/) library and send the file to recipients by email based on the excel listing.
Basically, the first page in pdf will send to first row recipient in the excel file.

## High level plan
1. Split the pdf source into individual file by page.
2. Get the excel listing.
3. Send the email to recipients based on the logic.

## Getting started
1. Amend the following input to meet your needs:
- Input your original pdf file that needed to split
- Input the location to store the individual file
- Input the excel listing location
- Input the email address and password (This information should store in environment variables)
- Amend the email content
2. Once 


# Further improvement
1. Send the email with multiple attachment at once if the email address is the same.
