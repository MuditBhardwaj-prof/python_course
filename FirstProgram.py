#arithmetic operators
a = 5
b = 2

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a ** b)

#relational operators
a = 50
b = 20
# print(a == b)#False
# print(a != b)#True
# print(a >= b)#True
# print(a > b)#True
# print(a <= b)#False
# print(a < b)#False

#assignment operators
# num = 10
# # num = num + 10 #10+10 => 20
# num += 10
# print(num)

#logical operators
# print(not False)
# print(not True)
# a = 50
# b = 60
# print(not (a > b))

# val1 = True
# val2 = False
# # print("and operator:", val1 and val2) #False
# print("OR operator:", val1 or val2)

#Type conversion
# a = int("2")
# b = 4.25

# sum = a + b
# print(sum)

# name = input("Please enter your name: ")
# print("Welcome ", name)

# val = float(input("please enter some value: "))
# print(type(val), val)

# num1 = int(input("Please enter first number: "))
# num2 = int(input("Please enter second number: "))
# sum = num1 + num2
# print("The sum is: ", sum)

# A = int(input("Please enter first number: "))
# B = int(input("Please enter second number: "))
# print(A >= B)

# age = int(input("Please enter your age: "))
# if age >= 18:
#     print("You can apply for a driving license.")
# elif age < 18:
#     print("You cannot apply for a driving license.")

# Light = "blue"

# if(Light == "red"):
#     print("Stop")
# elif(Light == "yellow"):
#     print("Get ready")
# elif(Light == "Green"):
#     print("Go")
# else:
#     print("Invalid traffic light color")
# print("END OF CODE")

# marks = int(input("Please enter your marks: "))

# if marks >= 90:
#     print("Grade of the student is: A")
# elif(marks >= 80 and marks < 90):
#     print("Grade of the student is: B")
# elif(marks >= 70 and marks < 80):
#     print("Grade of the student is: C")
# elif(marks >= 60 and marks < 70):
#     print("Grade of the student is: D")
# else:
#     print("Grade of the student is: F")

# num = 1

# rem = num % 2

# if rem == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")
a = 10
b = 20  
c = 5
# if a > b and a > c:
#     print("a is the greatest number.")
# elif b > a and b > c:
#     print("b is the greatest number.")
# else:
#     print("c is the greatest number.")

num = 49

# if num % 7 == 0:
#     print("The number is divisible by 7.")
# else:
#     print("The number is not divisible by 7.")

#APPEND METHOD
list= [1,4,3,0,2]
# list.append(5)
# print(list)
# print(list.sort(reverse=True))
# print(list)
# movies = []
# mov1 = movies.append (input("Please enter the name of first movie: "))
# mov2 = movies.append (input("Please enter the name of second movie: "))
# mov3 = movies.append (input("Please enter the name of third movie: "))

# print(movies)

# Distnertionary = {"Table" : ["a piece of furniture", "list of facts & figures"],
#                   "cat" : "a small animal"
#                 }
# print(Distnertionary)
# subject = {
#     "python", "java", "c++", "javascript", "java", "python",
#     "java", "c++", "c"
#     }
# print(len(subject))
marks = {}

x = int(input("enter phy:"))
marks.update({"phy": x})
y =int(input("enter chem:"))
marks.update({"chem": y})
z = int(input("enter math:"))
marks.update({"math": z})
print(marks)