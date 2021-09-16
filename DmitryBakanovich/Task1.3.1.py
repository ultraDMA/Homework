### Task 1.3
'''Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
Examples:
```
Input: 60
Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
'''

number = int(input())
output = [i for i in range(1, number + 1) if number % i == 0]
print(output)

# ok