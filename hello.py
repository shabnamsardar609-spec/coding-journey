print("Hello GitHub!")

name="shabnam"
age=20
price=68.99

print("my name is:",name) #my name is:shabnam
print("my age is:",age) #my age is:20
print("my price is:",price) #my price is:68.99

print(type(name)) #str
print(type(age)) #int
print(type(price)) #float

age=20
old=True
a=None
print(type(old)) #bool
print(type(a)) #Nonetype

#arithmatic operators
a=4
b=2
sum=a+b
print(sum) #6
print(a+b) #6
print(a-b) #2
print(a*b) #8
print(a/b) #2.0
print(a%b) #rem 0
print(a**b) #16

#relational operators
print(a==b) #False
print(a!=b) #True
print(a>=b) #True
print(a>b) #True
print(a<=b) #False
print(a<b) #False

#assignment operators
num=10
num+=10
print(num) #20

num=10
num-=10
print(num) #0

num=10
num*=10
print(num) #100

num=10
num/=10
print(num) #1.0

num=10
num%=10
print(num) #0

num=10
num**=10
print(num) #10000000000

#logistic operators
a=4
b=2
print(not False) #True
print(not (a>b)) #False
val1=True
val2=False
print("and operators:",val1 and val2) #False
print("or operators:",val1 or val2) #True
print("or operators:",a==b or a>b) #True

#type conversation
a=2
b=4.99
sum=a+b 
print(sum) #6.99
