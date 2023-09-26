"""
    Squirrel count by color (csv)
"""
import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data_for_new_csv = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": []
}
for color in data_for_new_csv["Fur Color"]:
    data_for_new_csv["Count"].append(len(data[data["Primary Fur Color"] == color]))

data_frame = pandas.DataFrame(data_for_new_csv)
data_frame.to_csv("squirrel_count.csv")
