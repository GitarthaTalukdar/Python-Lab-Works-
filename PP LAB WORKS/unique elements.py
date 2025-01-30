#Write a Python program that takes a list and returns a new list with unique elements of the first list
def unique_elements(lst):
    return list(set(lst))

lst = [1, 2, 2, 3, 4, 4,5,6, 7, 8, 8, 8, 8, 8, 5]
print("Unique elements:", unique_elements(lst))
