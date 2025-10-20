work_days=["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday"]
 # inserting data
# work_days.append("Sunday") # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# work_days.insert(2, "Wednesday") # ['Monday', 'Tuesday', 'Wednesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# work_days.remove("Wednesday") # ['Monday', 'Tuesday', 'Thursday', 'Friday', 'Saturday']
# del work_days[-2] # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday']

del work_days[-3:] # ['Monday', 'Tuesday', 'Wednesday']
print(work_days)

# 
backpack = ["Pizza", "Frozen custard", "Apple crisp", "Kale chips","Pizza slice", "Frozen custard", "Apple crisp", "Kale chips"]
while "Pizza slice" in backpack:
    backpack.remove("Pizza slice")
print(backpack) # ['Pizza', 'Frozen custard', 'Apple crisp', 'Kale chips', 'Frozen custard', 'Apple crisp', 'Kale chips']

backpack = [item for item in backpack if item != "Pizza slice"]
print(backpack) # ['Pizza', 'Frozen custard', 'Apple crisp', 'Kale chips', 'Frozen custard', 'Apple crisp', 'Kale chips']

for item in backpack:
    if item =="Pizza slice":
        backpack.remove(item)
print(backpack) # ['Pizza', 'Frozen custard', 'Apple crisp', 'Kale chips', 'Frozen custard', 'Apple crisp', 'Kale chips']

for i in range(len(backpack)):
    if backpack[i] == "Pizza Slice":
        backpack.pop(i)
print(backpack) # ['Pizza', 'Frozen custard', 'Apple crisp', 'Kale chips', 'Frozen custard', 'Apple crisp', 'Kale chips']

# coping backpack
for item in backpack[:]:
    if item == "Pizza slice":
        backpack.remove(item)
print(backpack) # ['Pizza', 'Frozen custard', 'Apple crisp', 'Kale chips', 'Frozen custard', 'Apple crisp', 'Kale chips']

for i in range(len(backpack)-1, -1,-1):
    print(i)
    if backpack[i] =="Pizza slice":
        backpack.pop(i)
print(backpack)
"""
6
5
4
3
2
1
0
['Pizza', 'Frozen custard', 'Apple crisp', 'Kale chips', 'Frozen custard', 'Apple crisp', 'Kale chips']
"""

# reverse a list
print(backpack) # ['Pizza', 'Frozen custard', 'Apple crisp', 'Kale chips', 'Frozen custard', 'Apple crisp', 'Kale chips']
backpack.reverse()
print(backpack) # ['Kale chips', 'Apple crisp', 'Frozen custard', 'Kale chips', 'Apple crisp', 'Frozen custard', 'Pizza']

print(backpack[::-1]) # ['Pizza', 'Frozen custard', 'Apple crisp', 'Kale chips', 'Frozen custard', 'Apple crisp', 'Kale chips']
# reverse function
for item in reversed(backpack):
    print(item, end=", ") # Pizza, Frozen custard, Apple crisp, Kale chips, Frozen custard, Apple crisp, Kale chips, 
print("-------------------")

myseason=["Spring", "Summer", "Fall", "Winter"]
myseason.reverse()
print(myseason)


for i , seasons in enumerate(myseason):
    print(i, seasons)
    if i == 0:
        print(i)
    

