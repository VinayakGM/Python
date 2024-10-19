# dictionary={
#     "bug":"The problem which stops the program from executing",
#     "Function":"The piece of code which could be run multiple times"
# }

# print(dictionary["bug"])
# print(dictionary)

import os

# Clearing the Scre
from art import logo
print(logo)

dict={}
print("Welcome to bidding project")

bidding=True
while bidding:
    name=input("Enter your name :")
    val=int(input("Enter your bid amount : $"))
    dict[name]=val
    choice=input("type 'yes ' or 'no' if there are other bidders").lower()
    os.system('cls')
    if choice=="no":
        bidding=False

max_bid=0
for name in dict:
    if dict[name]>max_bid:
        max_bid=dict[name]

print(f"Highest bidding amount was ${max_bid}")
