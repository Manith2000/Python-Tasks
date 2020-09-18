import re

#   $ and ^ and +
beginsandendswith = re.compile(r'^\d+$')
m = beginsandendswith.search('9274017') #this is a match since the entire string begins & end swith a number (\d)
#+ means one of more of the numeric digits 
#
print(m)

# . character
regex = re.compile(r'.{1,2}at') #anything followed by at
match = regex.findall('The cat sat on the flat mat')
print(match)
# {1,2} means 1 OR 2 chracters present. eg: FLat or Cat
#. mathces any character except for new lines
#Find chracter
s = 'First Name: M Last Name: Adikari'
print(s[(s.find(':')+4):]) #This is to find the Last name (present after first colon)

#Dot Star Character (match any set of characters)
reg = re.compile(r'First Name: (.*) Last Name: (.*)')
print(reg.findall(s))
#.* means find anything after the characters written

#re.DOTALL ensures . works for new lines
#re.I = ignores casetype for characters


#sub argument allows chracters to be replaced with another

#Verbose format ensures that whatever spaces you type arent part of the patter. improves readability

