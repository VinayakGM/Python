# with open("weather_data.csv") as datafile:
#     data=datafile.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as datafile:
#     data=csv.reader(datafile)
#     temp=[]
#     for row in data:
#         if row[1]!="temp":
#             temp.append(int(row[1]))
#     print(temp)

import pandas
# data=pandas.read_csv("weather_data.csv")
# print(data)
# print(data['temp'])
# type(data)

# data_dict=data.to_dict()
# print(data_dict)
# temp=data['temp'].to_list()
# print(sum(temp)/len(temp))

# print(data['temp'].mean())
# print(data['temp'].max())


# get data in column
# print(data.condition)
# print(data['condition'])

# # get data in rows
# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])

# monday=data[data.day=="Monday"]
# monday_temp=monday['temp']
# print(monday_temp*(9/5)+32)

data=pandas.read_csv("Squirrel_data.csv")
grey_squirrel_count=len(data[data["Primary Fur Color"]=="Gray"])
red_squirrel_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrel_count=len(data[data["Primary Fur Color"]=="Black"])

print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict={
    "Primary Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_squirrel_count,red_squirrel_count,black_squirrel_count]
}

data_frame=pandas.DataFrame(data_dict)
print(data_frame)
data_frame.to_csv("squirrel_count.csv")