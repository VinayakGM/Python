# str="hi"
# print(str.title())

# def format_name(f_name,l_name):
#     """return title case of f_name and l_name"""
#     return f"result: {f_name.title()} {l_name.title()}"

# print(format_name("hi","hello"))

# Calculator project
from art import logo
print(logo)

# operations=["*","+","/","-","%"]

# def calculate(first,second,op):
#     if op=="+":
#         return first+second
#     elif op=="-":
#         return first-second
#     elif op=="*":
#         return first*second
#     elif op=="/":
#         return first/second
#     elif op=="%":
#         return first%second
#     else:
#         return f"invalid operation"

# first=int(input("Enter your first number:"))
# for op in operations:
#     print(op+"\n")
# op=input("pick one operation:")
# second=int(input("Enter your second number: "))
# function(first,second,op)
def add(n1, n2):
    return n1+n2
def substract (n1, n2):
    return n1-n2
def multply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2

operations={
    '+':add,
    '-':substract,
    '*':multply,
    '/':divide
}
num1=int(input("Enter your first number: "))
for op in operations:
    print(op)
operator=input("pick your operation:")
num2=int(input("Enter your second number: "))
res=operations[operator](num1,num2)
print(f"{num1}{operator}{num2}={res}")
choice=input(f"type 'y' to continue to do operations with {res} or type 'n' to stop operations")
while choice=='y':
    num1=res
    for op in operations:
        print(op)
    operator=input("pick your operation:")
    num2=int(input("Enter your second number: "))
    res=operations[operator](num1,num2)
    print(f"{num1}{operator}{num2}={res}")
    choice=input(f"type 'y' to continue to do operations with {res} or type 'n' to stop operations")  





    



