#Write a Python program to create a tuple with multiple data types.
t=(1,22.4,"python",True,"Programming",56)
print(t)
for item in t:
    print(f"item -> {type(item)}")
    