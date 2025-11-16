import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))           ## DataFrame
# print(type(data["temp"]))   ## Series

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# average = sum(temp_list) / len(temp_list)
# print(average)

# print(data["temp"].mean())          ## same as above two lines
# print(data["temp"].max())

#Getting data in columns

# print(data["condition"])
# print(data.condition)

#Getting data in rows

# print(data[data.day =="Monday"])
# max_temp = (data.temp.max())
# print(data[data.temp == max_temp])

## Converting monday temp to farhenheit

# monday = data[data.day =="Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 +32
# print(monday_temp_f)

# Creating a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")