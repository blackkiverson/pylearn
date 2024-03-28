import re

# Reading a file and searching for a word
with open("hello_world.txt", encoding="utf-8", mode="r") as f:
    strings = re.findall(r"[\w']+", f.read())
    for string in strings:
        print(string)

with open("hello_world.txt", encoding="utf-8", mode="r") as f:
    strings = re.findall("may", f.read())
    if strings:
        print(''.join(strings) + " was found!!!") ## may was found!!!
    else:
        print(''.join(strings) + " was not found!!!")

# Searching for a word in a string
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print(tuples)  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
    print(tuple[0])  ## username
    print(tuple[1])  ## host

# Searching for emails in a file
with open("hello_world.txt", encoding="utf-8", mode="r") as f:
    strings = re.findall(r'[\w\.-]+@[\w\.-]+', f.read())
    for string in strings:
        print(string)

