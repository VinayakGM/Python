#password generator
import random
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","Z"]
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=["$","@","&","*","!"]

print("Welcome to pseudo password generator!")
nr_lettes=int(input("Enter the no of letters in password\n"))
nr_numbers=int(input("Enter the no of numbers in password\n"))
nr_symbols=int(input("Enter the no of symbols in the password\n"))

#Easy Level
# password=""

# for char in range(1,nr_lettes+1):
#      char=random.choice(letters)
#      password+=char

# for char in range(1,nr_symbols+1):
#      char=random.choice(symbols)
#      password+=char
    
# for num in range(1,nr_numbers+1):
#       num=random.choice(numbers)
#       password+=num

# print("your password is : "+password+"\n")

#hard level
password=[]

for char in range(1,nr_lettes+1):
     char=random.choice(letters)
     password.append(char)

for char in range(1,nr_symbols+1):
     char=random.choice(symbols)
     password.append(char)
    
for num in range(1,nr_numbers+1):
      num=random.choice(numbers)
      password.append(num)

random.shuffle(password)
str=""
for char in password:
     str+=char

print(str)