# import csv

# with open("weather_data.csv", "r") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# data_list = data.to_dict()
# temp_data = data["temp"].to_list()

# print(temp_data)

# total = sum(temp_data)
# average = total / len(temp_data)

# print("The Average is: ", average)

# print(data[data.temp == data.temp.max()])

import pandas
