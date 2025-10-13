# 3.7
languages = ["Python", "Go", "Java", "Javascript", "C"]

for language in languages: #iterations
    #print(language)

   # print(language, end=" ") # Python Go Java Javascript C 
    print(language, " ") # 
print()

print(range(0,10)) # range(0, 10)
print(range(10)) # range(0, 10)

for i in range(10):
    print(i, end=" ") # 0 1 2 3 4 5 6 7 8 9 

for i in range(len(languages)):
    print(languages[i], end =" ") # Python Go Java Javascript C 
print()

for i, language in enumerate(languages):
    print(i, language, end=" ") # 0 Python 1 Go 2 Java 3 Javascript 4 C 
print()

print("----------------")
print(languages[0]) # Python
for i in range (1, len(languages)):
    print(f"{languages[i]}, previous:, {languages[i-1]} ") # 

# Go, previous:, Python 
# Java, previous:, Go 
# Javascript, previous:, Java 
# C, previous:, Javascript 

print("------next------")
for i in range (0, len(languages)-1):
    print(f"{languages[i]}, next:, {languages[i+1]} ")

"""
ython, next:, Go 
Go, next:, Java 
Java, next:, Javascript 
Javascript, next:, C
"""

print("+++++++++++++++++")
for i in range(len(languages)-1, -1, -2):
    print(languages[i])