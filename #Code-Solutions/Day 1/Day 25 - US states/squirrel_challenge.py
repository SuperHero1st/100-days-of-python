import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_.csv")


count = [0,0,0]
for item in data["Primary Fur Color"]:
    if item == "Gray":
        count[0]+=1
    elif item == "Cinnamon":
        count[1]+=1
    elif item == "Black":
        count[2] +=1
colors = ["grey", "red", "black"]

new_data_dict = {
    "Fur Color": colors,
    "Count": count
}

data = pandas.DataFrame(new_data_dict)
data.to_csv("squirrel_count.csv")
