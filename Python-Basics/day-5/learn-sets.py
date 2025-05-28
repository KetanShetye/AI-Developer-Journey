# Sets
# A set is a built-in data type in Python that represents an unordered collection of unique elements. 
# Sets are useful when you want to store multiple items without duplicates, 
# and perform mathematical set operations like union, intersection, difference, etc.
# Using curly braces
my_set = {1, 2, 3, 4}

# Using the set() constructor
my_set2 = set([1, 2, 3])


# Python Set Methods 
# | Method                          | Description                                            | Example                              |
# | ------------------------------- | ------------------------------------------------------ | ------------------------------------ |
# | `add()`                         | Adds a single element                                  | `s.add(10)`                          |
# | `clear()`                       | Removes all elements                                   | `s.clear()`                          |
# | `copy()`                        | Returns a shallow copy                                 | `new_set = s.copy()`                 |
# | `difference()`                  | Returns difference of sets                             | `s1.difference(s2)`                  |
# | `difference_update()`           | Updates set by removing common elements                | `s1.difference_update(s2)`           |
# | `discard()`                     | Removes an element if present                          | `s.discard(4)`                       |
# | `intersection()`                | Returns common elements                                | `s1.intersection(s2)`                |
# | `intersection_update()`         | Keeps only common elements                             | `s1.intersection_update(s2)`         |
# | `isdisjoint()`                  | Returns True if sets have no elements in common        | `s1.isdisjoint(s2)`                  |
# | `issubset()`                    | Checks if one set is subset of another                 | `s1.issubset(s2)`                    |
# | `issuperset()`                  | Checks if one set is superset of another               | `s1.issuperset(s2)`                  |
# | `pop()`                         | Removes and returns a random element                   | `s.pop()`                            |
# | `remove()`                      | Removes a specific element (raises error if not found) | `s.remove(2)`                        |
# | `symmetric_difference()`        | Returns elements in either set but not both            | `s1.symmetric_difference(s2)`        |
# | `symmetric_difference_update()` | Updates set with symmetric difference                  | `s1.symmetric_difference_update(s2)` |
# | `union()`                       | Returns all elements from both sets                    | `s1.union(s2)`                       |
# | `update()`                      | Adds elements from another set                         | `s1.update(s2)`                      |

# Initial sets
a = {1, 2, 3}
b = {3, 4, 5}

a.add(6)                            # {1, 2, 3, 6}
a.clear()                          # set()
a = {1, 2, 3}
c = a.copy()                       # {1, 2, 3}
a.difference(b)                    # {1, 2}
a.difference_update(b)             # a = {1, 2}
a = {1, 2, 3}
a.discard(2)                       # {1, 3}
a.intersection(b)                  # {3}
a.intersection_update(b)          # a = {3}
a = {1, 2, 3}
a.isdisjoint({4, 5})              # True
a.issubset({1, 2, 3, 4})          # True
{1, 2, 3, 4}.issuperset(a)        # True
a.pop()                            # removes a random element
a = {1, 2, 3}
a.remove(2)                        # {1, 3}
a.symmetric_difference(b)         # {1, 2, 4, 5}
a.symmetric_difference_update(b)  # a = {1, 2, 4, 5}
a = {1, 2, 3}
a.union(b)                         # {1, 2, 3, 4, 5}
a.update(b)                        # a = {1, 2, 3, 4, 5}
