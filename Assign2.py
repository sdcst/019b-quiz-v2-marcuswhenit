"""
Write a program that uses a for loop.
Each iteration will ask the user to enter a name
Add the input to the provided list
"""
list = []
for i in range(20):
    names = input("Enter names > ")
    
    list.append(names)