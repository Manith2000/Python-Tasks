
# Method 1: Regular Expression [less code]
import re #regular expression module

text = 'My name is Manith and my phone number is +44 77 5324 5694. My office number is +44 77 2425 3452. If you want to contact me at home please reach +44 77 3451 2512'

phonereg = re.compile(r'(\d\d) (\d\d \d\d\d\d \d\d\d\d)') #the brackets seperate groups within number
match= phonereg.search(text)
print('Method One [Regular Expressions]:')
print('Country Code: +' + str(match.group(1))) #the first group is the country code 
print('0'+str(match.group(2)) + '\n') #attribute findall used to find phone no. within text


# Method 2: Standard Python Functions
def isphone(text): #checks if it is a phone no.
     number = text.replace(" ", "",3) #removes space 
     if number[0] != '+' or (len(number) != 13) or (not number[1:].isdecimal()): #phone no. length & is a number after +
         return False
     return True
    
    
def checkphone(text): #checks within text for a phone number
    found = False
    for i in range(len(text)):
        if isphone(text[i:i+16]): #looks for a 15 length string incl. space 
            found = True
            print('Phone number found:' + text[i:i+16])
    if found == False:
        return 'Could not find any phone numbers'
    else:
         return'The aforementioned phone numbers were found'

print(checkphone('My name is Manith and my phone number is +44 77 5324 5694. My office number is +44 77 2425 3452. If you want to contact me at home please reach +44 77 3451 2512'))


