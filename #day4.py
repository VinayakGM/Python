import random

# rand_int=random.randint(1,10)
# print(rand_int)

# rand_float=random.random()
# print(rand_float)

# love_score=random.randint(1,100)
# print(f"your love score is {love_score}")

print("Finance Game!")
#enter the names
names=input("Enter the names \n")
ls=names.split(",")
print(ls)

#find the perosn whose card is picked up
rand_int=random.randint(0,len(ls)-1)
print(f"person who is going to pay the bill {ls[rand_int]}")

print(random.choice(ls))

#rock -papet -scissors game

