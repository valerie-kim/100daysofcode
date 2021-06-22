"""
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
"""
    
"""
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file) 
    temperature = []
    for row in data:
        if row[1] != "temp":
            type(row[1]) == int
            temperature.append(int(row[1]))

    print(temperature)
"""

import pandas as pd

data = pd.read_csv("weather_data.csv")
# avg_temp_data = data['temp'].mean()
# max_temp_data = data['temp'].max()
# # print(f"Average Temperature: {round(avg_temp_data)}")
# # print(f"Maximum Temperature: {max_temp_data}")

# # Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data['temp'].max()])

# monday = data[data.day == "Monday"]
# monday_temp_f = monday.temp * (9/5) + 32
# print(monday_temp_f)

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Mike"],
    "scores": [76,23,89]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")