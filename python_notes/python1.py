"concepts about set difference"

"Set A = {1, 2, 3, 4}"
"Set B = {1, 2, 5 ,6}"
"Then, A - B = [elements that are in A but not in B] == {3, 4}"
"B - A = [elements that are in B but are not in A] == {5, 6}"
# Note that the objects in the set are unordered;
# you cannot assume that their traversal or print order will be the same across machines!


# below is a demonstration of the [map] and [filter] function
"""
>>> list(map(lambda x: x * x, [1,2,3]))
[1, 4, 9]

>>> list(filter(lambda x: x > 3, [1,2,3,4,5,4,3,2,1]))
[4, 5, 4]

"""
# Exercise:
# Write a list comprehension which, from a list,
# generates a lowercased version of each string that has length greater than five.
"""
>>> strings = ['Some string', 'Art', 'Music', 'Artificial Intelligence']
    print([_.lowercase() for _ in strings if len(_) > 5 ])
['some string', 'artificial intelligence']

"""




