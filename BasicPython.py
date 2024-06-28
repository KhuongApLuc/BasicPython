import os
import math
os.system('cls')
#Câu 1: Ask and answer
x = input("What is your name : ")
y = input("what is your ID : ")
z = input("which class are you in : ")
print("Name :" , x)
print("ID:", y)
print("Class:", z)


#Câu 2: Convert temperature from C => F
x = float(input("How much is the temperature today?"))
y = x*1.8 + 32
print("temperature today is ", y , "degree F")


#Câu 3: Caculate the age of the dog
a = int(input("how long does your dog live ?"))
if (a > 1):
   age = 10.5 * 2 + 4 * (a-2)
   print("your dog is ", age)
if (a == 1):
   print(" your dog's age is 10.5")
if (a == 0):
   print("you don't have any dog")


#Câu 4: print the day in a month
a = input("what month were you born ?")
if (a == 1) :
   print(31)
if (a == 2) :
   print(28 / 29)
if (a == 3) :
   print(31)
if (a == 4) :
   print(30)
if (a == 5) :
   print(31)
if (a == 6) :
   print(30)
if (a == 7) :
   print(31)
if (a == 8) :
   print(31)
if (a == 9) :
   print(30)
if (a == 10) :
   print(31)
if (a == 11) :
   print(30)
if (a == 12) :
   print(31)
else :
   print("no data")


#Câu 5: Check are these 3 edges of a triangles
a = float(input("goc thu nhat la : \n"))
b = float(input("goc thu hai la : \n"))
c = float(input("goc thu ba la : \n"))
if ( a + b + c > 180 ) or (a + b + c < 180 ):
   print("không phải 3 cạnh của tam giác")
if (a == b == c) :
   print( "đây là tam giác đều ")
if (a == b ) or (b == c) or (a == c) :
   print(" đây là tam giác đều")
else :
   print("đây là tam giác thường")


#câu 6: find solution of degree 2 equation
a = float(input(" nhập hệ số a : \n"))
b = float(input(" nhập hệ số b : \n"))
c = float(input(" nhập hệ số c : \n"))
delta = b**2 - 4*a*c
if ( delta < 0 ):
   print("phương trình vô nghiệm")
if ( delta == 0 ):
   x =  - b / 2*a 
   print("phương trình có 1 nghiệm duy nhất là ", x)
else :
   x1 = (- b + (math.sqrt(delta)))/2*a
   x2 = (- b - (math.sqrt(delta)))/2*a
   print ("nghiệm thứ nhất là ", x1)
   print ("nghiệm thứ hai là ", x2)


#Câu 7: print the next month's number of the days
date = int(input("nhập ngày"))
month = int(input("nhập tháng"))
year = int(input("nhập năm"))
if (date == 30) and ((month == 4) or (month == 6) or (month == 9) or (month == 10) or (month == 11)):
   date = 1
   month = month + 1
   print("ngày bạn tìm là ", date,"/",month, "/", year)
if (date == 31) and ((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8)or (month == 10)) :
   date = 1
   month = month + 1
   print("ngày bạn tìm là ", date,"/",month, "/", year)
if (date == 31) and (month == 12):
   date = 1 
   month = 1 
   year = year + 1
   print("ngày bạn tìm là ", date,"/",month, "/", year)
if (date == 28) and (month == 2):
   if (year % 4 == 0) :
       date = 29 
       print("ngày bạn tìm là ", date,"/",month, "/", year)
   else:
       date = 1
       month = month + 1
       print("ngày bạn tìm là ", date,"/",month, "/", year)
else:
   date = date + 1
   print("ngày bạn tìm là ", date,"/",month, "/", year)


#Câu 8: Calculate the area of ​​an equilateral triangle
n = int(input("nhập số cạnh của đa giác đều: \n"))
a = float(input("độ dài 1 cạnh của đa giác đều: \n"))
S = ((n * (a**2))/4)*(1/(math.tan(180/n)))
print("diện tích đa giác đều là", S)

#Câu 9: Operation
import fractions
a = fractions(input(" nhập phân số thứ nhất "))
b = fractions(input(" nhập phân số thứ hai "))
m = a + b
n = a - b
p = a*b
q = a/b
print (m)
print (n)
print (p)
print (q)