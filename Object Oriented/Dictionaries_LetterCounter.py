def count(letter,message):
    count = {}
    for character in message.upper():
        count.setdefault(character,0)
        count[character] += 1
    return(count.get(letter,'Not present'))
print(count('F','The Fox jumped over the fence'))

#Note: function works given that input is uppercase since
#message was converted to uppercase so lowercase and 
#uppercase letters are not seperated within the dictionary









