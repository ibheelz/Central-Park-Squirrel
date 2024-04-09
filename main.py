# import csv
# import pandas

# with open("weather_data.csv", "r") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# data = pandas.read_csv("weather_data.csv")
# data_list = data.to_dict()
# temp_data = data["temp"].to_list()

# print(temp_data)

# total = sum(temp_data)
# average = total / len(temp_data)

# print("The Average is: ", average)

# print(data[data.temp == data.temp.max()])

# data = pandas.read_csv("weather_data.csv")
# print(data)

#Get Data in Columns

# data_col = data.temp
# print(data_col)

#Get Data in Rows

# data_row = data[data.day == "Monday"]
# print(data_row)

#Calculate the average of temperatures

# data_avg = data.temp.mean()
# print(data_avg)

#Calculate the max temperature value

# data_max = data.temp.max()
# print(data_max)

#Assign attribute directly

# monday = data[data.day == "Monday"]
# print(monday.condition)

#Create a dataframe from scratch

# grades = {
#     "Names" : ["Abby", "Felipe", "Joseca", "Pedro", "Carlos", "Regi", "Jorge"],
#     "Scores" : [48, 56, 85, 24, 53, 99, 12]
# }

# grades_data = pandas.DataFrame(grades)
# print(grades_data)

# grades_data.to_csv("grades.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")
# print(data)

# print(squirrel_data)

colors = data["Primary Fur Color"]
colors_counts = colors.value_counts()
colors_dict = colors_counts.to_dict()
print(colors_dict)
