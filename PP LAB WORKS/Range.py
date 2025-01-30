#Write a Python program to check whether a number is in a given range
def is_in_range(n, start, end):
    return start <= n <= end

print(is_in_range(10, 5, 20))
print(is_in_range(25, 5, 20))