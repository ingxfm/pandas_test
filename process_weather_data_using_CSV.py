import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    print(data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
   
