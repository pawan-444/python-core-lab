# Python supports chaining relational operators. This enables to evaluate chains of comparison without having to use logical operators.

print(1 < 2 < 3)        # True, because 1 < 2 and 2 < 3
print(3 > 2 > 1)        # True, because 3 >
print(2 >= 2 <= 3)      # True, because 2 >= 2 and 2 <= 3
print(1 < 2 > 1)        # True, because 1 < 2 and 2 > 1
print(1 < 2 < 1)        # False, because 2 is not less than 1

# Chaining can also be combined with equality operators
print(1 < 2 == 2)       # True, because 1 < 2 and 2 == 2
print(2 == 2 < 3)       # True, because 2 == 2 and 2 < 3
print(2 == 3 < 4)       # False, because 2 is not
print(1 < 2 != 3)       # True, because 1 < 2 and 2 != 3
print(2 != 2 < 3)       # False, because 2 is not != 2
print(2 != 3 < 4)       # True, because 2 != 3 and 3 < 4
