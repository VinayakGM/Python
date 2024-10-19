#tip calculator
print("welcome to tip calculator")
bill=int(input("how much is totla bill: \n"))
tip=int(input("how much tip you want to give 10,12,15?\n"))
Total_Person=int(input("How many to split: "))
pay=(bill+tip)/Total_Person
print(f"Each person to pay the amount {pay}")