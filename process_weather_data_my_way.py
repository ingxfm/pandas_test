with open("./weather_data.csv") as data_file:
    lines_list = data_file.readlines()

print(lines_list)

for line in lines_list:
    stripped_line = line.strip("\n")
    separated_word = stripped_line.split(",")
    print(separated_word)
    
