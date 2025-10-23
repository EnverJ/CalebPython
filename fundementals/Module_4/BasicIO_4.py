#input abd output
msg = "pay attention to each word that i say"
words = msg.split()
print(words) # ['pay', 'attention', 'to', 'each', 'word', 'that', 'i', 'say']

msg = "my, name, is, Enver"
print(msg.split(",")) # ['my', ' name', ' is', ' Enver']

msg = """
In 1921, 
due to human intervention, the terminal lake shifted its position back to Lop Nur. 
The lake measured 2400 km2 in area in 1930–1931. In 1934,
 Sven Hedin[15] went down the new Kuruk Darya ("Dry River") in a canoe. 
He found the delta to be a maze of channels and the new lake so shallow 
that it was difficult to navigate even in a canoe. He had previously walked 
the dry Kuruk Darya in a caravan in 1900.

"""
words= msg.split("\n")
print(words)
 # ['', 'In 1921, ', 'due to human intervention, the terminal lake shifted its position back to Lop Nur. ', 'The lake measured 2400 km2 in area in 1930–1931. In 1934,', ' Sven Hedin[15] went down the new Kuruk Darya ("Dry River") in a canoe. ', 'He found the delta to be a maze of channels and the new lake so shallow ', 'that it was difficult to navigate even in a canoe. He had previously walked ', 'the dry Kuruk Darya in a caravan in 1900.', '', '']

####
print("--------------------")
print('List out your favorite foods separated by ","')
print('Example input: ')
print("Nan, sutchay, horma, meghiz")
foods = [food.strip() for food in input().split(",")]
# foods = input().split(', ')
for food in foods:
    print(food)

# 
print("++++++++++++++++++")
print("List your favorite foods one line at time")
fav_foods = []
while True:
    fav = input("Enter a food, Q to quit: ")
    if fav.lower() =='q':
        break
    fav_foods.append(fav)
print(fav_foods)
    