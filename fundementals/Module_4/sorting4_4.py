#
work_days=["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday"]
work_days.sort()
print(work_days) # ['Friday', 'Monday', 'Saturday', 'Thursday', 'Tuesday', 'Wednesday']

numbers=[2,3,4,5,2,22,23,1204]
numbers.sort()
print(numbers) #[2, 2, 3, 4, 5, 22, 23, 1204]
numbers.sort(key=str)
print(numbers) # [1204, 2, 2, 22, 23, 3, 4, 5]

print("----reverse=True----")
print(sorted(numbers, reverse=True)) # [1204, 23, 22, 5, 4, 3, 2, 2]
#
print("-------------------")
print(sorted(numbers)) # [2, 2, 3, 4, 5, 22, 23, 1204]
print(numbers)  # [1204, 2, 2, 22, 23, 3, 4, 5]

StringNum=["2","3","4","5","2","22","23",'1204']
StringNum.sort()
print(StringNum) # ['1204', '2', '2', '22', '23', '3', '4', '5']

StringNum.sort(key=int)
print(StringNum) #['2', '2', '3', '4', '5', '22', '23', '1204']

letters = ['A', 'a', 'abc', "ABC", 'aBc', 'Abc', 'abC']
print(sorted(letters)) # ['A', 'ABC', 'Abc', 'a', 'aBc', 'abC', 'abc']
print(sorted(letters, reverse=True)) # ['abc', 'abC', 'aBc', 'a', 'Abc', 'ABC', 'A']

mixed=[True, False, 1,23,3.33333]
print(sorted(mixed, key= float)) # [False, True, 1, 3.33333, 23]


