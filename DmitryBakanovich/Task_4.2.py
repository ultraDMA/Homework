### Task 4.2
'''Write a function that check whether a string is a palindrome or not. Usage of
any reversing functions is prohibited. To check your implementation you can use
strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).'''

def is_palindrome(str):
    string = [i.lower() for i in str if i.isalpha()]
    for j in range(0, len(string) // 2):
        if string[j] != string[len(string) - j - 1]:
            return False
    return True

string = input()
if is_palindrome(string):
    print('Yeah, it\'s palindrome!')
else:
    print('No palindrome found')