# we can define string with single or double quotes

print('Hello, World!')  # Output: Hello, World!
print("Python is great!")  # Output: Python is great!

# we can also use triple quotes for multi-line strings
multi_line_string = """This is a 
multi-line string.
It can span 
multiple lines."""

print(multi_line_string)





# ---------LENGTH OF STRING----------

# we can find the length of a string using the len() function
print(len("Hello, World!"))  # Output: 13
print(len("Python is great!"))  # Output: 17





# ---------OPERATIONS ON STRINGS----------


# ---CONCATENATION---

# we can concatenate strings using the + operator
greeting = "Hello, " + "World!"
print(greeting)  # Output: Hello, World!

string1 = "Python "
string2 = "with "
string3 = "DSA"
full_string = string1 + string2 + string3
print(full_string)  # Output: Python with DSA

# ---REPLICATION---

# we can replicate strings using the * operator
string = "Faaa... "
new_string = string * 3
print(new_string)  # Output: Faaa...Faaa...Faaa...

print(new_string == string + string + string)  # Output: True (replication is equivalent to concatenation)

# ---COMPARISON---

# we can compare strings using comparison operators
print("apple" == "apple")  # Output: True
print("apple" == "Apple")  # Output: False (case-sensitive)
print("apple" < "banana")  # Output: True (lexicographical order)
print("apple" > "banana")  # Output: False (lexicographical order)

'''Lexicographical order is based on the Unicode code points of the characters.
In this case, 'a' has a lower code point than 'b', so "apple" is considered less than "banana".'''

print(ord('a'))  # Output: 97 (Unicode code point of 'a')
print(ord('b'))  # Output: 98 (Unicode code point of 'b')