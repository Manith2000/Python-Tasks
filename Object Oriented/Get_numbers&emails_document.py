#This script reads phone numbers, email addresses from a document (copied into clipboard)


import re, pyperclip #pyperclip to read text off clipboard


phone = re.compile(r'''(
(+\d\d)? #+44 country code maybe present
(\d)? #0 before 77 maybe present
(\d\d) #77 present
(\d\d\d\d) #the two 4 digit phone number
(\d\d\d\d)) ''', re.VERBOSE)

email = re.compile(r'''
[a-zA-Z0-9_.+]+  #this is the name part such as tom.Henderson
@
[a-zA-Z0-9_.+]+  #the email eg: gmail
''', re.VERBOSE)


text = pyperclip.paste() #text from clipboard

extractphone = phone.findall(text)
extractemail= email.findall(text)

phonenumbers = []
for i in extractphone:
    phonenumbers += [extractphone[i][0]] #this is because only the first part of the tuple received is full phone number

