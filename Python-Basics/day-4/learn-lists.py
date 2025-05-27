# List 
# A list is a collection which is ordered, mutable, and allows duplicate elements.
# Defined using square brackets [].
fruits = ["apple", "banana", "cherry"]

# List Properties 
# | Property   | Description                     |
# | ---------- | ------------------------------- |
# | Ordered    | Maintains the order of elements |
# | Mutable    | Can be modified after creation  |
# | Duplicates | Allows duplicate items          |
# | Indexable  | Access via index (starts at 0)  |
# | Iterable   | Can loop over it with `for`     |


# List Indexing & Slicing
lst = [10, 20, 30, 40, 50]
print(lst[1])       # 20
print(lst[-1])      # 50
print(lst[1:4])     # [20, 30, 40]
print(lst[::2])     # [10, 30, 50]

#  Nested Lists
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # 3

#  List Comprehension
squares = [x*x for x in range(5)]  # [0, 1, 4, 9, 16]

# Iteration 
for item in ["a", "b", "c"]:
    print(item)

# Membership Test
"a" in ["a", "b", "c"]  # True

 # List Methods 
# | Method         | Description                         | Example Code                    | Resulting List / Output            |
# | -------------- | ----------------------------------- | ------------------------------- | ---------------------------------- |
# | `append(x)`    | Add item to the end                 | `l = [1, 2]; l.append(3)`       | `[1, 2, 3]`                        |
# | `extend(iter)` | Extend list with iterable           | `l = [1, 2]; l.extend([3, 4])`  | `[1, 2, 3, 4]`                     |
# | `insert(i, x)` | Insert at position                  | `l = [1, 3]; l.insert(1, 2)`    | `[1, 2, 3]`                        |
# | `remove(x)`    | Remove first occurrence of value    | `l = [1, 2, 3]; l.remove(2)`    | `[1, 3]`                           |
# | `pop()`        | Remove and return last item         | `l = [1, 2, 3]; l.pop()`        | Returns `3`, list becomes `[1, 2]` |
# | `pop(i)`       | Remove and return item at index `i` | `l = [1, 2, 3]; l.pop(0)`       | Returns `1`, list becomes `[2, 3]` |
# | `clear()`      | Remove all items                    | `l = [1, 2, 3]; l.clear()`      | `[]`                               |
# | `index(x)`     | Return index of first occurrence    | `l = [1, 2, 3]; l.index(2)`     | Returns `1`                        |
# | `count(x)`     | Count occurrences of value          | `l = [1, 2, 2, 3]; l.count(2)`  | Returns `2`                        |
# | `sort()`       | Sort the list (in place)            | `l = [3, 1, 2]; l.sort()`       | `[1, 2, 3]`                        |
# | `reverse()`    | Reverse the list (in place)         | `l = [1, 2, 3]; l.reverse()`    | `[3, 2, 1]`                        |
# | `copy()`       | Return shallow copy of list         | `l = [1, 2]; copy_l = l.copy()` | `copy_l` is `[1, 2]`               |


