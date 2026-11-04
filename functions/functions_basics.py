#Defining a Function
def myFunc():
    print('Hello world')
    
#Calling the function
myFunc()

#Return Statement:- when it reaches return it stops the execution and sends value back
def myFunc1():
    return 'Hello Niranjan'

print(myFunc1())

#Parameters vs arguments

def stu_details(name,age): #name and age are parameters
    return f"Students's name is {name} and age is {age}"

print(stu_details('Niranjan',22)) #niranjan and 22 are arguments

#Default parameters or default arguments

def details(name='friend'):
    return f"Hello {name}"

print(details())

#Keyword arguments

def dog_details(name,animal):
    return f"Animal is {animal} and it's name is {name}"

print(dog_details(name='roy',animal='Dog'))

#You can send any values as arguments ex:- dictionary

def dDetails(details):
    print(f"Name : {details['name']}")
    print(f"age : {details['age']}")
    
details1={'name':'Niranjan','age':22}
dDetails(details1)

#Arbitrary arguments *args

def names1(*names):
    print(names)   #*args will store all the arguments in a tuple
    for i in names:
        print(i)
        
names1('Arjun','Kabir','Devdas')

#Arbitrary keyword arguments **kwargs

def names2(**name):
    print(name['fname'])
    print(name['LastName'])
    
names2(fname='Niranjan',LastName='Tangirala') #Keyword arguments
    