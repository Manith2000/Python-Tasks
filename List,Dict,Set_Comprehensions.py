num = [-1,2,-3,4,-5,6,7,8,9,10]

#New list
mylist = [n for n in num]
print(mylist)

#Add numbers
mylist = [n+n for n in num]
print(mylist)

#Print even numbers of num
even = [n for n in num if not n%2]
print(even)


#Dictionary Comprehensions
names = ['John', 'Paul','George','Ringo','Pete']
instruments = ['Rhythm','Bass','Lead','Drums','Drums']

Beatles ={name: instrument for name, instrument in zip(names,instruments) if name != 'Pete'}
print(Beatles)


#Set Comprehension

my_set = {n for n in num} #sets can be made using set function or with this {}
print(sorted(my_set, key=abs, reverse= True)) #the key can be used for objects with class attributes to be sorted
#can use attrgetter or simply make a func, etc.
#Sorted can be used for many types unlike list.sort()

#Ternary Conditionals
condition = True

x = 1 if condition else 0

print(x)