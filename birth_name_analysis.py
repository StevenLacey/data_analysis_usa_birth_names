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
