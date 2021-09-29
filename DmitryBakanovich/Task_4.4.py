### Task 4.4
'''Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
which splits the `s` string by indexes specified in `indexes`. Wrong indexes
must be ignored.
Examples:
```python
>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]
```'''
def split_by_index(s, indexes):
    out = []
    start = 0
    for i in indexes:
        out.append(s[start:i])
        start = i
    return out

split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
split_by_index("no luck", [42])

