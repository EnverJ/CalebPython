backpack = ["Pizza", "Frozen custard", "Apple crisp", "Kale chips"]
healthy= ["Kale chips", "Broccoli"]
# 2
# healthy_backpack=[]
# for item in backpack:
#     if item in healthy:
#         healthy_backpack.append(item)
# print(healthy_backpack) # ['Kale chips']

# or 3

# healthy_backpack = [item for item in backpack if item  in healthy]
# print(healthy_backpack) # ['Kale chips']

# or 4
unique = set(backpack)
print(unique) # {'Frozen custard', 'Pizza', 'Kale chips', 'Apple crisp'}
for item in unique:
    print(backpack.count(item), end =" ") # 1 1 1 1 
counts = [[backpack.count(item), item] for item in unique ]
print(counts) # [[1, 'Apple crisp'], [1, 'Kale chips'], [1, 'Pizza'], [1, 'Frozen custard']]

# 1
# # Inclusion checking
# if "Pizza" in backpack:
#     print("I am so excited") # I am so excited
# # Checking where this element is
#     print(backpack.index("Pizza")) # 0

# # search
#     num =backpack.count("Pizza")
#     print(num) # 1

#############################

# squares = [i*i for i in range(10)]
# print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# square_event = [i*i for i in range(10) if i % 2 == 0]
# print(square_event) # [0, 4, 16, 36, 64]


