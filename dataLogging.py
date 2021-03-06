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
    client.debug = False # feel free to toggle this if you want debug messages
    client.email = email #the email address that you specified above
    client.password = password #the password you entered earlier
    client.source = 'My Datalogger' #not really necessary, but so we know were it's coming from 
    client.ProgrammaticLogin() #the actual command to log in now that it has information
    return client #return the resulting object to the thing that called it

def spreadsheetWriter(value):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S %p')
    client = authenticate() #call the function to log in to Google Apps
    #get the number of rows in the worksheet
    worksheetsFeed = client.GetWorksheetsFeed(key=spreadsheetKey)
    rowCount = worksheetsFeed.entry[0].row_count.text
    rowNumber = int(rowCount) + 1
    print 'We will write to row number', rowNumber
    row = {} #column headings are in the first row, capitals and spaces disregarded
    row['timestamp'] = timestamp
    row['value'] = value
    client.InsertRow(row, spreadsheetKey, worksheetId) #write the new row to spreadsheet
    return value #send the value back to whatever called this function

value = 'test' #this can be a string or some type of number, from wherever you're getting it
print spreadsheetWriter(value) #this will call the function and then print what it returns
