def greet():
    print("Hello")
    print("Hello, Enver")

greet()
greet()
"""
Hello
Hello, Enver
Hello
Hello, Enver
"""
print("-------greet1--------")
def greet1(name):
    if name == "Josh":
   #     return # finish here or
       pass # continue
    else:
        print("Hello")
        print(f"Hello, {name}")


#greet1("Caleb")
#greet1("Enver")
greet1("Josh")
print("--------greet1-------")

"""
Hello
Hello, Caleb
Hello
Hello, Enver
"""


print("Practice return")
#         return
def greet3(name = "User"):  # for a default user in case, there is no parameter provide
    return f"Hello {name}, welcome to coding club"
  

me = "Enver"
greeting = greet3(me)
print(greeting) # Hello Enver, welcome to coding club
print(greet3()) # Hello Enver, welcome to coding club

#         return. and default
print("///////////////////")
def greet4(name = "User", be_nice = False):  # for a default user in case, there is no parameter provide
    if be_nice:      
        return f"Hello {name}, welcome to coding club"
    return f"Go away!!!! {name}"
  

me = "Enver"
greeting = greet4(me, True)
print(greeting) # Hello Enver, welcome to coding club. # Hello Enver, welcome to coding club
print(greet4()) # Go away!!!! User
print(greet4("NONO", False)) # Go away!!!! NONO
print(greet4(be_nice=True, name="Tara")) # Hello Tara, welcome to coding club

print("------example---------")
def example(pos1, pos2, pos3, /, either1,either2, *, keyword1,keyword2,keyword3):
    print("pos1", pos1)
    print("pos2", pos2)
    print("pos3", pos3)
    print("either1", either1)
    print("either2", either2)
    print("keyword1", keyword1)
    print("keyword2", keyword2)
    print("keyword3", keyword3)
example(1,2,3,4,5,keyword1=6,keyword2=7,keyword3=8)
"""
pos1 1
pos2 2
pos3 3
either1 4
either2 5
keyword1 6
keyword2 7
keyword3 8
"""
print("............................")
example(1,2,3,4,5,keyword1=6,keyword2=8,keyword3=7)

"""
pos1 1
pos2 2
pos3 3
either1 4
either2 5
keyword1 6
keyword2 8
keyword3 7
"""
    
def greet_People(people):
    for i in people:
        print(f"Hello, {i}")
people = ["Ezmet", "Enver", "Kudret"]
greet_People(people)

"""
Hello, Ezmet
Hello, Enver
Hello, Kudret
"""

print("use * to make a string")
def greet (person):
    print(f"Hi, {person}")
def greet_All(*folks):
    for person in folks:
        greet(person)
greet_All("Ez","Kud", "En")

"""
Hi, Ez
Hi, Kud
Hi, En
"""
print("+++++++++")
def print_info(name, age, email):
    print(f"{name} is {age}, contact email is {email}")
# print_info("Enver", 30, "Enver@enver.com") # Enver is 30, contact email is Enver@enver.com
# or
data = ["Enver", 30, "Enver@enver.com"]
print_info(*data) # Enver is 30, contact email is Enver@enver.com
 