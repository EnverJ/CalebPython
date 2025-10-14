# 3.8
for i in range(10):
    for j in range(i,10):
        print(i* j, end=" \t")
    print()

# sub array
arr = [1,2,3,4,5,6,7]
for i in range(len(arr)):
    for j in range(i, len(arr)):
        print(arr[i:j+1], end=" ")
    print()
"""
[1][1, 2][1, 2, 3][1, 2, 3, 4][1, 2, 3, 4, 5][1, 2, 3, 4, 5, 6][1, 2, 3, 4, 5, 6, 7]
[2][2, 3][2, 3, 4][2, 3, 4, 5][2, 3, 4, 5, 6][2, 3, 4, 5, 6, 7]
[3][3, 4][3, 4, 5][3, 4, 5, 6][3, 4, 5, 6, 7]
[4][4, 5][4, 5, 6][4, 5, 6, 7]
[5][5, 6][5, 6, 7]
[6][6, 7]
[7]

"""

# nested while loop
i = 0
while i < 10:
    j = 0
    while j < 10:
        print(j, end =" ")
        j += 1
    print()
    i += 1
    """
    0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
    """

# factorial
i = 10
while i > 0:
    factorial = 1
    j = i
    while j > 0:
        print(j, end=" ")
        factorial *= j
        j -= 1
        if j>0:
            print("X", end = " ")
        else:
            print("=", end=" ")
    print(factorial)
    i -= 1
print("0 = 1")


