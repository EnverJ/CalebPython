# print("List your favorite foods one line at time")
# fav_foods = []
# while True:
#     fav = input("Enter a food, Q to quit, R to Remove: ")
#     if fav.lower() == 'q':
#         break
#     if fav.lower() == 'r':
#         print(f"Popped off: {fav_foods.pop()}")
#         print(f"favorites food now: {fav_foods}")
#         continue
#     fav_foods.append(fav)
# print(fav_foods)

# queue
# print("List your favorite foods one line at time")
# fav_foods = []
# while True:
#     fav = input("Enter a food, Q to quit, R to Remove: ")
#     if fav.lower() == 'q':
#         break
#     if fav.lower() == 'r':
#         print(f"Popped off: {fav_foods.pop(0)}")
#         print(f"favorites food now: {fav_foods}")
#         continue
#     fav_foods.append(fav)
# print(fav_foods)


#double ended queue -- this is much better solution and fast compare to queue
from collections import deque
print("List your favorite foods one line at time")
fav_foods = deque()
while True:
    fav = input("Enter a food, Q to quit, R to Remove: ")
    if fav.lower() == 'q':
        break
    if fav.lower() == 'r':
        print(f"Popped off: {fav_foods.popleft()}")
        print(f"favorites food now: {fav_foods}")
        continue
    fav_foods.append(fav)
print(fav_foods)