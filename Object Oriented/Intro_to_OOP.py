class Student:
    def __init__(self,first: str,last:str,grade:int):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@b.com'
        self.grade = grade
    @property
    def fullname(self):
        return '%s %s' %(self.first,self.last)


st1 = Student('Paul', 'M', 72) #two instances of class student
st2 = Student('John', 'L', 56)

print(st1.grade)


#Alternative and quicker method:

from dataclasses import dataclass

@dataclass
class student2:
    first_name: str
    last_name: str
    grade: int

st3 = student2('George', 'H', 84)
st4 = student2('Ringo', 'S',64)

print(st3.grade)