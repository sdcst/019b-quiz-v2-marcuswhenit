#!python3
# Write a program that uses a for loop to ask the user to enter in 5 numbers. The program will determine the sum of the 5 numbers and calculate the average
# You must use only 1 input statement in your program

sum = 0
# loop from 1 to n
for i in range(5):
    n = int(input("Enter number"))
    sum = sum + n
print(f"Sum of the 5 numbers is {sum}")
average = sum / 2
print(f"Average of {sum} is {average}")