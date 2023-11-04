import math

# a = 4
# b = 6
# c = 18

# lcm = math.lcm(a, b, c)

# print(f"The least common multiple of {a}, {b}, and {c} is {lcm}.")
# ---------------------------------------------------------------------------------------------

# x = -5
# absolute_value = abs(x)
# print(absolute_value)  # This will print 5
# ---------------------------------------------------------------------------------------------

# def find_lcd(a, b, c):
#     # Find the common divisors of a, b, and c
#     common_divisors = set()
#     for i in range(1, min(a, b, c) + 1):
#         if a % i == 0 and b % i == 0 and c % i == 0:
#             common_divisors.add(i)

#     if common_divisors:
#         # The least common divisor is the maximum value in the common divisors set
#         lcd = max(common_divisors)
#         return lcd
#     else:
#         return None  # If there are no common divisors, return None


# Example usage:
a = 4
b = 6
c = 18
lcd = find_lcd(a, b, c)
if lcd is not None:
    print(f"The least common divisor of {a}, {b}, and {c} is {lcd}.")
else:
    print("There are no common divisors.")
# ---------------------------------------------------------------------------------------------


# def find_first_common_divisor(numbers):
#     # Sort the numbers in ascending order
#     numbers.sort()

#     # Start checking for common divisors from 2 (the smallest possible divisor)
#     for divisor in range(2, numbers[0] + 1):
#         # Check if the divisor is a common divisor of all numbers
#         is_common_divisor = all(number % divisor == 0 for number in numbers)

#         if is_common_divisor:
#             return divisor

#     return None  # If there are no common divisors, return None


# # Example usage:
# numbers = [12, 18, 24]
# first_common_divisor = find_first_common_divisor(numbers)
# if first_common_divisor is not None:
#     print(f"The first common divisor of {numbers} is {first_common_divisor}.")
# else:
#     print("There are no common divisors.")
