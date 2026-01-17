"""Write a Python program to create a list with elements of multiple data types (integers, 
strings, floats, etc.)
"""
my_list=[10,'python',2.5,"programming",True]
print(my_list)
for item in my_list:
    print(f"{item} -> {type(item)}")