#!/usr/bin/env python
#code and images are released into the public domain, see unlicense.org
#lines that begin with a pound sign are comments

import gdata.spreadsheet.service #from https://code.google.com/p/gdata-python-client/
import time #for the timestamp
import getpass #to hide the password when it is typed in

#Google Spreadsheet stuff
email = '' #put your email address between the quotes
password = getpass.getpass()
spreadsheetKey = '' #fill in the spreadsheet key
worksheetId = 'od6' #the first worksheet, where the chore data will be logged

def authenticate():
    client = gdata.spreadsheet.service.SpreadsheetsService() 
    client.debug = False # feel free to toggle this 
    client.email = email 
    client.password = password 
    client.source = 'Hay Family Chore Chart' 
    client.ProgrammaticLogin()
    return client #return the resulting object to the thing that called it

def spreadsheetWriter(kid, choreNumber):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S %p')
    client = authenticate()
    #get the number of rows in the worksheet
    worksheetsFeed = client.GetWorksheetsFeed(key=spreadsheetKey)
    rowCount = worksheetsFeed.entry[0].row_count.text
    rowNumber = int(rowCount) + 1
    print 'We will write to row number', rowNumber
    row = {} #column headings are in the first row, capitals and spaces disregarded
    row['timestamp'] = timestamp
    row['value'] = value
    client.InsertRow(row, spreadsheetKey, worksheetId) #write the new row to spreadsheet

client = authenticate() #log in to Google Apps

