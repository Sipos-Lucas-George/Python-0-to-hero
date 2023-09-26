"""
    Working with CSV
"""
# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = [int(row[1]) for row in data if row[1] != "temp"]
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(sum(temp_list)/len(temp_list))
print(data["temp"].mean())
print(data["temp"].max())

print(data["condition"])
print(data.condition)

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.temp[0] * 9/5 + 32)

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_csv")

