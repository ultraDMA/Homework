### Task 1.3
'''Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
Examples:
```
Input: ['red', 'white', 'black', 'red', 'green', 'black']
Output: ['black', 'green', 'red', 'white', 'red']
```'''

words = [_ for _ in input().split(', ')]
words = set(words)
output = [_ for _ in words]
output.sort()
print(output)

# Ok