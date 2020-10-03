import requests

res = requests.get('http://www.google.com')
print(len(res.text)) #length of text on webpage
print(res.status_code) #this prints 200 if successful
#or easier to use res.raise_for_status()

newfile = open('newfile.txt', 'wb')
#wb opens in binary mode. need to write binary data instead to maintain unicode encoding
for part in res.iter_content(10000):
    newfile.write(part)

#this method is only useful if you can access content
#from webpage directly (eg: not logging in)
