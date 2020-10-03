#SMTP is the protocol used in Pyhton
import smtplib

conn = smtplib.SMTP('smtp.gmail.com',587) #connection object
print(type(conn)) #this connects to server
conn.ehlo() #start conenction
conn.starttls() #TLS encryption
conn.login('Email address login','Enter Password')
conn.sendmail('From Email','TO Email','Subject: Mkmasda...\n\n This is a test email\n\nMLA')
#SMTP server domain names can be checked online to login
conn.quit()

#Use a google app specific password for external uses 


#To check email IMAP protocol can be used
#Though imaplib is not that user friendly

import imapclient #check what the imap server domain name is for the email
conn = imapclient.IMAPClient('imap.gmail.com',ssl=True)
conn.login('Login email','Password')
conn.select_folder('INBOX',readonly = True) 
UIDs = conn.search(['SINCE 20-Aug-2015']) #Imap has its own syntax to search
#this returns UIDs for all emails
rawmessage = conn.fetch([EnterUID],['BODY[]','FLAGS'])

#this outputs a rawmesssage with tons of \n,etc. so use pyzmail module
import pyzmail
message = pyzmail.Pyzmessage.factory(rawmessage[EnterUID][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('bcc')

#you can also check it this email only had text parts or it had HTML parts(eg: images,etc.)
message.html_part == None #returns True or False
message.text_part #'' ''
message.text_part.get_payload().decode('UTF-8') #get the text part of the message
