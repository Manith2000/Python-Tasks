import re

#Pipes
text = 'Batman rode his Batmobile through the city'

batreg = re.compile(r'Bat(man|mobile|cycle|copter)') #use pipes |
match = batreg.findall(text)
print(match) #finds groups that start with bat


#Question Mark  ??????
phoneregex = re.compile(r'(\d\d)? \d\d \d\d\d\d \d\d\d\d') 
#this allows country code to be optional if used on phone number
#can also be used to match for objects with/without the bracketed bits as an alternative to pipes

#Star character *********
#used same way as ? but allows it to appear 0 or more times not just once

#Plus character +++++++++
# used same way as ? but allows it to appear 1 or more times not just once

#Curly Brackets
#appear exactly x number of times
wowreg = re.compile(r'(wo){3}') #exactly thrice

#{3,7} means at least thrice but at most seven times
#Greedy Match (matches the max): DEFAULT shown above
#Ungreedy match (matches the min): {3,7}?
#{3,} means at least thrice


#findall() note
#for output to be unseperated do
#re.compile(r'((group1)(group2))') Brackets around ENTIRE thing will out put the whole, group1, group 2 output

#Character Classes
#\d is digit chracter class 0-9
#make own class by doing r'[enter here]'
#eg: [aeiou], [aeiou]{2} is double vowels, [a-f] is a to f only
#negative character class ^
#[^aeiou] means consonants







