# list = []
# with open("weather_data.csv") as file:
#     list = file.readlines()
#     for i in range(len(list)):
#         list[i] = list[i].replace("\n", " ")
#         list[i] = list[i].strip()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# average_temp = 0
# for temp in temp_list:
#     average_temp += temp
# average_temp /= len(temp_list)
# print(average_temp)

print(data["temp"].mean())
print(max(data["temp"]))

print(data.condition)

# Get data in Row
monday = data[data.day == "Monday"]
print(monday.condition)
print((1.8 * monday.temp[0]) + 32)
print(data[data.temp == max(data["temp"])])

#Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

#Primary Fur Color
squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

fur_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}
df = pandas.DataFrame(fur_dict)
df.to_csv("squirrel_count.csv")