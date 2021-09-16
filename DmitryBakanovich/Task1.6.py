### Task 1.6
"""Write a Python program to convert a given tuple of positive integers into an integer. 
Examples:
```
Input: (1, 2, 3, 4)
Output: 1234
```"""

numbers = tuple(int(i) for i in input().split(',') if int(i) >= 0)
output = int(''.join(map(str, numbers)))
print(f'Input: {numbers}')
print(f'Output: {output}')
