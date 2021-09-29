### Task 4.3
"""Implement a function which works the same as `str.split` method
(without using `str.split` itself, ofcourse)."""

def same_as_split(string, sep = ' ', count = -1):
    out = []
    if count == 0:
        return [string]
    else:
        counter = count
    string += ' '
    start = 0
    if not sep:
        raise ValueError('empty separator')
    while counter != 0:
        element = string[start : string.find(sep, start)]
        out.append(element)
        if string.find(sep, start) == -1:
            if out[-1] == '' and sep == ' ':
                return out[0 : -1]
            return out
        start += len(element) + len(sep)
        counter -= 1

string = 'foobar, foo, bar' #input()
sep = 'foo' #input()
count = 0 #int(input())
print(same_as_split(string, sep, count))
