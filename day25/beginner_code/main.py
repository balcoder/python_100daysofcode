''' read a csv file and transform it to list obj '''
import pandas

# data = pandas.read_csv('day25/weather_data.csv')
# temp_list = data['temp'].to_list()
# num_of_temps = len(temp_list)
# total = 0
# for temp in temp_list:
#     total += temp
# print(total/num_of_temps)

# print(data['temp'].mean())
# print(data[data.temp == data['temp'].max()])

# monday = data[data.temp == data['temp'] =='Monday']
# print(monday)

# temp_series = data['temp']
# print(temp_series)
# day = temp_series.get(4)
# print(day)

# monday = data[data.day == 'Monday']
# print(monday.temp * 1.8 + 32)

data = pandas.read_csv("day25/2018_Squirrel_Data.csv")
num_of_gray = len(data[data["Primary Fur Color"] == "Gray"])
num_of_red = len(data[data["Primary Fur Color"] == "Cinnamon"])
num_of_black = len(data[data["Primary Fur Color"] == "Black"])

squirrel_count = pandas.DataFrame({
    "Fur Color": ["gray", "red", "black"],
    "Count": [num_of_gray, num_of_red, num_of_black]
})

print(squirrel_count)

squirrel_count.to_csv("day25/squirrel_count.csv")