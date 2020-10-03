#Underscores for readibility of larger numbers
num1 = 10_000_000
num2 = 100_000_000
total = num1 + num2
print(f'{total:,}')


#Context managers
#Manages resources. No need for file.close ,etc..

# with open('test.txt','r') as f:
#     file_contents = f.read()



#Enumerate Function
names = ['John','George','Paul','Ringo']
instruments = ['Rhythm','Lead','Bass','Drums']
for index,name in enumerate(names,start=0):
    print(f'{name} plays {instruments[index]}')

#OR even easier....



#Zip function
for name,instrument in zip(names,instruments):
    print(f'{name} plays {instrument}')
#this stops when shortest array is run out of value
#alternatively use zip long so it runs out when longest array


#Unpacking
a, _,*c,d = (1,2,3,4,5,6) #underscore tells that we arent using that value
print(a,c,d) #the *c tells that whatever is left is equal to d


#Setattr & Getattr

#useful when the input attribute is same variable name as the class attribute name
class Person():
    pass
person = Person()
first_key = 'first'
first_val = 'Tom'
setattr(person,first_key,first_val)
first = getattr(person,first_key)
print(first)


#Getpass - for sensitive info
from getpass import getpass
un = input('Username: ')
pw = getpass('Password: ')


#dash m (-m)
#this runs the module following -m and treats anything afterwards as attributes
#eg: instead of py -m test.py do py -m test


#Help/Dir
#help(module_name)
#dir(datetime) this gives you the attributes on that specific object 

