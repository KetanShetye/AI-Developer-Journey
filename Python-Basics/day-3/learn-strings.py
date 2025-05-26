# String :-
# A string in Python is a sequence of characters enclosed in single quotes '...', double quotes "...", or triple quotes '''...''' or """...""".
# Strings are immutable, which means once you create a string, you cannot change its contents.
# Single and double quotes
name = 'Alice'
greeting = "Hello, World!"

# Triple quotes for multiline strings
paragraph = """This is
a multiline string
in Python."""

# Most Commonly Used String Methods
# | Method               | Description                                | Example                                  |
# | -------------------- | ------------------------------------------ | ---------------------------------------- |
# | `lower()`            | Converts string to lowercase               | `"Hello".lower()` → `'hello'`            |
# | `upper()`            | Converts string to uppercase               | `"hello".upper()` → `'HELLO'`            |
# | `strip()`            | Removes leading/trailing whitespace        | `" hello ".strip()` → `'hello'`          |
# | `replace(old, new)`  | Replaces a substring with another          | `"cat".replace("c", "b")` → `'bat'`      |
# | `split(delimiter)`   | Splits string into list                    | `"a,b,c".split(",")` → `['a', 'b', 'c']` |
# | `join(iterable)`     | Joins elements using string as separator   | `",".join(['a', 'b'])` → `'a,b'`         |
# | `find(sub)`          | Returns first index of substring (or `-1`) | `"apple".find("p")` → `1`                |
# | `startswith(prefix)` | Checks if string starts with prefix        | `"apple".startswith("app")` → `True`     |
# | `endswith(suffix)`   | Checks if string ends with suffix          | `"apple".endswith("le")` → `True`        |
# | `isdigit()`          | Checks if all characters are digits        | `"123".isdigit()` → `True`               |


# Full Table of String Methods in Python (with Examples)
# | Method                    | Description                                  | Example                                        | Output                  |
# | ------------------------- | -------------------------------------------- | ---------------------------------------------- | ----------------------- |
# | `capitalize()`            | Capitalizes first character                  | `"hello".capitalize()`                         | `'Hello'`               |
# | `casefold()`              | Case-insensitive lowercase                   | `"HELLO".casefold()`                           | `'hello'`               |
# | `center(width, fillchar)` | Centers string                               | `"hi".center(5, '*')`                          | `'*hi*'`                |
# | `count(sub)`              | Counts occurrences of substring              | `"banana".count("a")`                          | `3`                     |
# | `encode()`                | Returns encoded version                      | `"hello".encode()`                             | `b'hello'`              |
# | `endswith(suffix)`        | Ends with substring?                         | `"data.csv".endswith(".csv")`                  | `True`                  |
# | `expandtabs(tabsize)`     | Expands tabs to spaces                       | `"a\tb".expandtabs(4)`                         | `'a   b'`               |
# | `find(sub)`               | First index of substring                     | `"apple".find("p")`                            | `1`                     |
# | `format()`                | Formats string                               | `"Hi {}".format("Sam")`                        | `'Hi Sam'`              |
# | `format_map(dict)`        | Formats using dict                           | `"{name}".format_map({"name": "Amy"})`         | `'Amy'`                 |
# | `index(sub)`              | Like `find()`, but raises error if not found | `"apple".index("p")`                           | `1`                     |
# | `isalnum()`               | Alphanumeric check                           | `"abc123".isalnum()`                           | `True`                  |
# | `isalpha()`               | Alphabetic check                             | `"abc".isalpha()`                              | `True`                  |
# | `isascii()`               | ASCII check                                  | `"abc".isascii()`                              | `True`                  |
# | `isdecimal()`             | Decimal check                                | `"123".isdecimal()`                            | `True`                  |
# | `isdigit()`               | Digit check                                  | `"123".isdigit()`                              | `True`                  |
# | `isidentifier()`          | Valid identifier?                            | `"name1".isidentifier()`                       | `True`                  |
# | `islower()`               | All lowercase?                               | `"abc".islower()`                              | `True`                  |
# | `isnumeric()`             | Numeric check                                | `"123".isnumeric()`                            | `True`                  |
# | `isprintable()`           | Printable characters only?                   | `"abc".isprintable()`                          | `True`                  |
# | `isspace()`               | Only whitespace?                             | `" \t\n".isspace()`                            | `True`                  |
# | `istitle()`               | Titlecased?                                  | `"Hello World".istitle()`                      | `True`                  |
# | `isupper()`               | All uppercase?                               | `"ABC".isupper()`                              | `True`                  |
# | `join(iterable)`          | Join with separator                          | `"-".join(['a', 'b'])`                         | `'a-b'`                 |
# | `ljust(width, fillchar)`  | Left-align with padding                      | `"hi".ljust(4, '*')`                           | `'hi**'`                |
# | `lower()`                 | Lowercase string                             | `"HELLO".lower()`                              | `'hello'`               |
# | `lstrip()`                | Remove leading spaces                        | `"  hello".lstrip()`                           | `'hello'`               |
# | `maketrans()`             | Create translation table                     | `str.maketrans("abc", "123")`                  | `{97:49, 98:50, 99:51}` |
# | `translate(table)`        | Translate using map                          | `"abc".translate(str.maketrans("abc", "123"))` | `'123'`                 |
# | `partition(sep)`          | Split into 3 parts                           | `"a-b-c".partition("-")`                       | `('a', '-', 'b-c')`     |
# | `replace(old, new)`       | Replace substrings                           | `"hi".replace("h", "b")`                       | `'bi'`                  |
# | `rfind(sub)`              | Last index of substring                      | `"hello hello".rfind("lo")`                    | `9`                     |
# | `rindex(sub)`             | Last index (error if not found)              | `"hello".rindex("l")`                          | `3`                     |
# | `rjust(width, fillchar)`  | Right-align string                           | `"hi".rjust(4, '*')`                           | `'**hi'`                |
# | `rpartition(sep)`         | Split from right                             | `"a-b-c".rpartition("-")`                      | `('a-b', '-', 'c')`     |
# | `rsplit(sep, maxsplit)`   | Split from right                             | `"a,b,c".rsplit(",", 1)`                       | `['a,b', 'c']`          |
# | `rstrip()`                | Remove trailing whitespace                   | `"hello  ".rstrip()`                           | `'hello'`               |
# | `split(sep, maxsplit)`    | Split string                                 | `"a,b,c".split(",")`                           | `['a', 'b', 'c']`       |
# | `splitlines()`            | Split at line breaks                         | `"a\nb".splitlines()`                          | `['a', 'b']`            |
# | `startswith(prefix)`      | Starts with substring?                       | `"apple".startswith("app")`                    | `True`                  |
# | `strip()`                 | Remove leading/trailing spaces               | `"  hi  ".strip()`                             | `'hi'`                  |
# | `swapcase()`              | Swap upper/lower                             | `"HeLLo".swapcase()`                           | `'hEllO'`               |
# | `title()`                 | Title case                                   | `"hello world".title()`                        | `'Hello World'`         |
# | `upper()`                 | Uppercase                                    | `"hello".upper()`                              | `'HELLO'`               |
# | `zfill(width)`            | Pad with zeros on left                       | `"42".zfill(5)`                                | `'00042'`               |
