names_file = open("names.txt", "r")

#create dicts of buys and girls names
dict_of_boys_names = {}
dict_of_girls_names = {}
for name in names_file:
    temp_list = name.split(",")
    if temp_list[2] == "Boy\n":
        if temp_list[0] not in dict_of_boys_names:
            dict_of_boys_names[temp_list[0]] = {"count" : int(temp_list[1]), "gender" : temp_list[2].strip()}
    if temp_list[2] == "Girl\n":
        if temp_list[0] not in dict_of_girls_names:
            dict_of_girls_names[temp_list[0]] = {"count" : int(temp_list[1]), "gender" : temp_list[2].strip()}
#total names
count_of_names = 0
for key in dict_of_boys_names:
    count_of_names += 1
for key in dict_of_girls_names:
    count_of_names += 1
print("total names: ", count_of_names)

#total births
sum_of_births = 0
for key, value in dict_of_boys_names.items():
    sum_of_births += dict_of_boys_names[key]["count"]
for key, value in dict_of_girls_names.items():
    sum_of_births += dict_of_girls_names[key]["count"]
print("total births: ", sum_of_births)

# count of boys names starting with z
count_of_z_names = 0
for key in dict_of_boys_names:
    if key[0] == "Z":
        count_of_z_names += 1
print("count of boys names starting with Z: ", count_of_z_names)

# Most common girls name starting with Q
most_frequent_Q_girl = 0
most_frequent_Q_girl_name = ""

for key, value in dict_of_girls_names.items():
    if key[0] == "Q":
        if dict_of_girls_names[key]["count"] > most_frequent_Q_girl:
            most_frequent_Q_girl = dict_of_girls_names[key]["count"]
            most_frequent_Q_girl_name = key
print("Most frequent girls name starting with Q: ", most_frequent_Q_girl_name, most_frequent_Q_girl)
