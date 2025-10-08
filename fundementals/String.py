data = "Hello123"
print(data)

# python dose not have char, so in python, string is wither "", or ''

hello = 'they\'re'
print(hello)# they're

newLine= 'they are my \nfriends'
print(newLine)


me = "Enver"
you = "You"
print(me, "+", you)

friend = f"{me} + {you} are bestest of friends"

print(friend)
 # multi lines strings
friend2 = f"""{me} + {you} are bestest of friends
I can be a python master
"""
print(friend2)

#
message = "this is a very important message"

print(message[0]) #t
print(message[-1]) #e
print(message[0:3]) #thi
print(message[0:-1]) # this is a very important messag


# string immutability
msg ="Java is my favorite"

#msg[0]="k"
# print(msg) # TypeError: 'str' object does not support item assignment

msg = "K" + msg[1:]
print(msg) # Kava is my favorite

# len
language='Java'
print(len(language)) #4
print("index 4: ",language[3]) #index 4:  a
print("Last index: ", language[len(language)-1]) # Last index:  a

newLang="Length is "+ str(len(language))
print(newLang) # Length is 4

