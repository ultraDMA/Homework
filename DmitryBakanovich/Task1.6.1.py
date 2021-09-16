""""### Task 1.6
Write a program which makes a pretty print of a part of the multiplication table.
Examples:
```
Input:
a = 2
b = 4
c = 3
d = 7

Output:
	3	4	5	6	7	
2	6	8	10	12	14	
3	9	12	15	18	21	
4	12	16	20	24	28
```
"""
def pretty_print(a, b, c, d):
    print('', *[i for i in range(c, d + 1)], sep='\t')
    for i in range(a, b + 1):
        print(i, end='\t')
        for j in range(c, d + 1):
            print(i * j, end='\t')
        print()

a, b = int(input('a = ')), int(input('b = '))
c, d = int(input('c = ')), int(input('d = '))
print('\nOutput:')
pretty_print(a, b, c, d)