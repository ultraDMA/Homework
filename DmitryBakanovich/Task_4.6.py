### Task 4.6
'''Implement a function `get_shortest_word(s: str) -> str` which returns the
longest word in the given string. The word can contain any symbols except
whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
the string with a same length return the word that occures first.
Example:
```python

>>> get_shortest_word('Python is simple and effective!')
'effective!'

>>> get_shortest_word('Any pythonista like namespaces a lot.')
'pythonista'
```'''

def get_shortest_word(s: str):
    string = s.split()
    for i in string:
        if len(i) == max(len(word) for word in string):
            return i

print(get_shortest_word('Any pythonista like namespaces a lot.'))
print(get_shortest_word('Python is simple and effective!'))