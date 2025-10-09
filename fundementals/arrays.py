import copy
age = [20, 25, 30]
names = ["Caleb", "Enver", "Jack"]
my_favorite_things =["Book", 7, ["youtube", "Amazon prime"]]

print(age)
print(names)
print(my_favorite_things)
my_favorite_things[2][1]="Hulu"
print(my_favorite_things)
other= copy.deepcopy(my_favorite_things)
other[0]="AI"
other[2][1]="Disney"
print(my_favorite_things[2][1])
print(my_favorite_things)
print(other)
print()


# adding two array
good =["Leghmen", "Polo", "Kavap"]
bad = ["Lengpung", "Teyyar Chop", "Shaklat"]
balance = good + bad
print(balance) # ['Leghmen', 'Polo', 'Kavap', 'Lengpung', 'Teyyar Chop', 'Shaklat']
# or 
good += bad
print(good) #['Leghmen', 'Polo', 'Kavap', 'Lengpung', 'Teyyar Chop', 'Shaklat']

good.extend(bad)
print(good)

# pop. remove
remove=good.pop(-1)
print(remove, good) # Shaklat ['Leghmen', 'Polo', 'Kavap', 'Lengpung', 'Teyyar Chop', 'Shaklat', 'Lengpung', 'Teyyar Chop']

good.append("Suyukash")
print(good) # ['Leghmen', 'Polo', 'Kavap', 'Lengpung', 'Teyyar Chop', 'Shaklat', 'Lengpung', 'Teyyar Chop', 'Suyukash']