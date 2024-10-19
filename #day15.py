#coffe maachine project
logo ='''☕'''


def report(machine):
    print(f" water : {machine['water']} ml")
    print(f" milk  : {machine['milk']} ml")
    print(f" coffe : {machine['coffe']} gm")
    print(f" money : {machine['money']} $")
    
machine={
    "water":300,
    "milk":200,
    "coffe":100,
    "money":0
}

data={
     "latte":{
    "water":200,
    "milk":150,
    "coffe":24,
    "money":1.2
    },
    "expresso":{
    "water":100,
    "milk":50,
    "coffe":6,
    "money":1.4
    },
    "capaccunio":{
    "water":250,
    "milk":100,
    "coffe":24,
    "money":2
    }
}
def is_resource(user_input):
    user_res=data[user_input]
    if machine['water']>user_res['water'] and machine['milk']>user_res['milk'] and machine['coffe']>user_res['coffe']:
        return True
    print("Sorry we dont have that much of resource!!")
    return False

def check_money(user_money,user_input):
    if user_money>data[user_input]["money"]:
        machine["money"]+=data[user_input]["money"]
        change=user_money-data[user_input]["money"]
        print(f"Here is your change : {change}")
        print("please have your drink")
        report(machine)
    else:
        print("you dont have enought money!")



user_input=input("what you would like to have ? 'latte' / 'espresso' / 'capaccuino' ")

if user_input=="report":
    report(machine)
elif is_resource(user_input):
    print("please insert coins!")
    quarters=int(input("How many quarters ? : "))
    dimes=int(input("How many dimes ? : "))
    nickles=int(input("How many quarters ? : "))
    pennies=int(input("How many quarters ? : "))
    user_amount=quarters+dimes*0.2+nickles*0.05+pennies*0.01
    check_money(user_amount,user_input)