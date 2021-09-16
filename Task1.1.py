### Task 1.1
'''Write a Python program to calculate the length of a string without using the `len` function.'''

string = input(' Input something what you want to count to: ')
count = 0
for _ in string:
    count += 1
print(f' The lenght of your string is: {count} symbol(s)')

#Ok