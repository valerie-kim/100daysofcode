import pandas as pd

data = pd.read_csv("/Users/valerie/Documents/100days_of_Python/06-21/Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = data[data["Primary Fur Color"] == "Gray"].shape[0]
red_count = data[data["Primary Fur Color"] == "Cinnamon"].shape[0]
black_count = data[data["Primary Fur Color"] == "Black"].shape[0]

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_count, red_count, black_count]
}

fur_color_data = pd.DataFrame(data_dict)
fur_color_data.to_csv("fur_color_data.csv")