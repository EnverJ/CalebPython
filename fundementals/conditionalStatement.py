happy = True
print(happy)

print(3<5)

me="Nerd"
you = "Nerd"
print(me == you)

my_grade = [100, 99, 98]
your_grade = [100, 99, 98]
print(my_grade == your_grade) # True

print(my_grade is your_grade) # False
print(id(my_grade), id(your_grade)) #4368386304 4368388160
print(id(my_grade) == id(your_grade))  # False

print("ABC" < "ACD") # True

print("A" == "B") # False
print(not "A" == "B")  # True


enver_is_cool = False
if enver_is_cool:
    print("Let us be friends")
else:
    print("Eww")


# name = input("What is your name")
# age = input("What is your age")
name = "Enver"

if name == "Enver":
    print(f"Welcome, {name}")
print(f"How are you, {name}")


thunder = True
lighting = True
if thunder and lighting:
    print("Do not go to swimming") #Do not go to swimming
elif not thunder or not lighting:
    print("Stay home is better")
else:
    print("Absolutely!!!")
