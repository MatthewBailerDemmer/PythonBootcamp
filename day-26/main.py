# On Python console


#List Comprehension
# list = [1, 2, 3,]
# new_list = [n + 1 for n in list]
# name = "Angela"
# new_list = [letter for letter in name]
# list = range(1, 5)
# list = [n + 1 for n in range(1, 5)]
# list = [n * 2 for n in range(1, 5)]
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5 ]
# upper_case_names = [name.upper() for name in names]
# upper_case_names = [name.upper() for name in names if len(name) > 5]


#Dictionary Comprehension
# import random
# student_scores = {name:random.radint(0,100) for name in names}
# student_scores = {name:random.randint(0,100) for name in names}
# passed_students = {name:score for (name,score) in student_scores.items() if score > 70}


#Pandas Comprehension

student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

#Loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)