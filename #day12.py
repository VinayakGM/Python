var=10

def fun():
   global var
   var=2
   print(var)

print(var)
fun()
print(var)
# Number guessing Game
# import random

# print("welcome to number guessing game")
# res=random.randint(0,100)
# # print(res)
# option=input("choose the game level : type 'easy' or 'hard' : ")
# choice=10
# if option=="hard":
#    choice=5
 
# is_gameover=True

# while choice>0:
#    guess_number=int(input("guess the number:"))
#    if guess_number==res:
#       print("thats correct,you won!!")
#       is_gameover==False
#       break
#    elif guess_number<res:
#       print("too low")
#       print("guess again")
#       print(f"you have {choice-1} choices left!")
#    elif guess_number>res:
#       print("too high")
#       print("guess again")
#       print(f"you have {choice-1} choices left!")
#    choice=choice-1

# if  is_gameover:
#    print("you lost")
      

