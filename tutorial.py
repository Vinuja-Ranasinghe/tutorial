# name = input("name : ")
# print("Hi", name)

# p_val = int(input("Principal input : "))
# i_rate = int(input("Intrest rate as a percentage : "))
# time = int(input("Time period : "))

# intrest = p_val*time*(i_rate/100)
# print(intrest)

# rain = input("Is it raining (Yes/No) : ")
# if (rain == "yes"):
#     print("Don't go out")
# else:
#     print("Do what ever you want")

# a= list(range(100,105,2))
# print(a)

# file = open("demo.txt", "r")
# content = file.read()
# print(content)
# file.close()

# sq_numbers = [x**2 for x in range(0,10) if x%2==0]
# print(sq_numbers)

# //String formating
# numbers= [12,12,2016]
# Date = "Date:{0}/{1}/{2}".format(numbers[0], numbers[1], numbers[2])
# print(Date)

# Date = "Date:{x}/{y}/{z}".format(x=27, y=10, z=1999)
# print(Date)

# a,b,c=27,10,1999
# Date = "Date:{x}/{y}/{z}".format(x=a, y=b, z=c)
# print(Date)


# def add(x):
#     return x+12

# def twice(func,arg):
#     return func(func(arg))

# print(twice(add,2))
# nums =[x for x in range(10)]
# nums=list(range(10))
# newNums = list(map(add,nums))
# print(newNums)

# nums=list(range(10))
# newNums = list(map(lambda x:x+2,nums))
# print(newNums)


# nums=list(range(10))
# newNums = list(filter(lambda x:x%2 == 0,nums))
# print(newNums)


# Object oriented programming - classes with methods

# class students:
#     #define properties of the class
#     #initializing the objects of a class
#     def __init__(self,name,contact):
#         self.name = name
#         self.contact = contact

#     def getData(self):
#         print("accepting data")
#         self.name = input("Enter name : ")
#         self.contact = input("Enter contact : ")

#     def putData(self):
#         print("The name is "+self.name, "and the contact number is "+self.contact)

# class Science_student(students):
#     def __init__(self,age):
#         self.age = age

#     def science(self):
#         print("I am a science student")
# Vinuja = Science_student(20)
# Vinuja.getData()
# Vinuja.putData()



# def factorial(x):
#     if x == 0:
#         return 1
#     else:
#         return x*factorial(x-1)
    
# print(factorial(5))

# seta={1,2,3,4}
# setb= {x for x in range(10)}
# print(set("asasasas"))


# from itertools import accumulate

# triangular_numbers = list(accumulate(range(10)))
# print(triangular_numbers)


#Data handling

# class Myclass:
#     __hiddenvariable = 0 #two underscore lines makes the variable hidden

# import re

# pattern = r"[A-Z][A-Z][0-9]"
# if re.search(pattern,"AA2"):
#     print("Bye")


