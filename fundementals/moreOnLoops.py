# 3.7

languages = ["Python", "Go", "Java", "Javascript", "C", "C", "Python","Python", "Java"]

search = "Python"
count = 0
print(f"Searching for {search}")

print("Python" in languages) # True

# or

for language in languages:
    if language == search:
        print(f"{search}")
        count += 1
        continue
        print(f"{search}")
    print(f"❌{language}")

print(f"Thanks for searching, we found {search} {count} times") # Thanks for searching, we found Python 3 times



find = "python"
print(f"Searching for {find}")

for lang in languages:
    if lang == find:
        print(f"🫡 {lang}")
        break
else: 
    print(f"{find} not found") # python not found

# While loop 
j = 30
while j >= 0:
    j -=2
    print(f"{j}", end =" ") # 28 26 24 22 20 18 16 14 12 10 8 6 4 2 0 -2 -----End------
print("-----End------")

print(range (0, 30, 2)) # range(0, 30, 2)
print(list(range(30,2,-2))) # [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]

initialization = 5
stop_at = 10
increment = 1

for i in range (initialization, stop_at, increment):
    print("for loop: ", i, end= " ") # for loop:  5 for loop:  6 for loop:  7 for loop:  8 for loop:  9 


while initialization < stop_at:
    print("While loop: ", initialization, end = " ") # While loop:  5 While loop:  6 While loop:  7 While loop:  8 While loop:  9 
    initialization += increment

print()

k = 0
while k < 10 :
    if k ** 2 > 50:
        print(f"square big enough: {k}") # square big enough: 8
        break
    k += 1
else:
    print("None are big enough")

# do while loop
# python dose not have do while loop. bu t we can make it up

print()

m = 15
print(m)
m += 1

while m <= 10:
    print(m)
    m += 1
# 15

 


