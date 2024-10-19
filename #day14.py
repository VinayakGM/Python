import random
from art import logo
from gamedata import data
print(logo)


vs='''

            
 __   _____ 
 \ \ / / __|
  \ V /\__ \
   \_/ |___/
            

'''
# print(data)

# first  generate random index
n=len(data)
index1=random.randint(0,n-1)
index2=random.randint(0,n-1)

if index1==index2:
    index2=random.randint(0,n-1)

A=data[index1]
B=data[index2]
# print(values)
print(f"Compare A : {A['name']} from {A['place']}")
print(vs)
print(f"Compare B : {B['name']} from {B['place']}")

final_score=cur_score=0
guess_answer=input("who has more followers ? type 'A' or 'B'")

answer="A" if A["followers"]>B["followers"] else "B"

while guess_answer==answer:
    cur_score+=1
    if answer=="B":
        A=B
    B=data[random.randint(0,n-1)]
    print(f"your current score : {cur_score}")
    print(f"Compare A : {A['name']} from {A['place']}")
    print(vs)
    print(f"Compare B : {B['name']} from {B['place']}")
    final_score=cur_score
    guess_answer=input("who has more followers ? type 'A' or 'B'")
    answer="A" if A["followers"]>B["followers"] else "B"

print(f"you lost it ,your final score : {final_score}")






