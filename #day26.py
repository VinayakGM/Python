# list comprehension
list=[1,2,3,4]
# new_list=[new_item for item in list]
new_list=[n+1 for n in list]
print(new_list)

str="Vinayak"
new_str=[char for char in str]
print(new_str)

# conditional list comprehneioning
# new_list=[new_item for item in list if test]
new_list=[n+1 for n in list if n>2]
print(new_list)

# dictionary comprehension
# new_dictionary={new_key:new_value for item in list}
# new_dict={new_key:new_value for (key,val) in dict.items()}

import random
ls=["A","B","C","D"]
student_dict={ item:random.randint(1,100) for item in ls}
print(student_dict)

passed_dict={key:val for (key,val) in student_dict.items() if val>50}

print(passed_dict)

# iterate over dataframe
stu_dict={
          "Name":["A","B","C"],
          "Marks":[50,60,70]
     }

import pandas
df=pandas.DataFrame(stu_dict)
# print(df)
# for (key,value) in df.items():
#     print(key)
#     print(value)
# using iterrow method

for (index,row) in df.iterrows():
    print( index, row.Name, row.Marks)
