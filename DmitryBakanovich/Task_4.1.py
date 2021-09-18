### Task 4.1
'''Implement a function which receives a string and replaces all `"` symbols
with `'` and vise versa.'''

def char_replace():
    output = ''
    for char in string:
        if char == '"':
            output += '\''
        elif char == '\'':
            output += '"'
        else:
            output += char
    return output

string = input()
print(char_replace())
