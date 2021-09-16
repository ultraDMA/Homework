### Task 1.4
"""Write a Python program to sort a dictionary by key."""

my_dict = {0: 'alpha', 2: 'gamma', 1: 'beta', 4: 'epsilon', 3: 'delta'}
keys = sorted(my_dict.keys())
my_dict_sorted = {}
for key in keys:
    my_dict_sorted.update({key: my_dict[key]})
print('sorted dict:\t', my_dict_sorted)
