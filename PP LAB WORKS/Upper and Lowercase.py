#Calculate the number of upper case letters and lower case letters in a string
def count_case(s):
    upper_case = sum(1 for c in s if c.isupper())
    lower_case = sum(1 for c in s if c.islower())
    return upper_case , lower_case

s= input("enter a string:")
upper,lower = count_case(s)
print(f"Upper case letters:{upper}")
print(f"lower case letters:{lower}")
