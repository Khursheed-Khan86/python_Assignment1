#Write a Python program to merge two lists into one dictionary using a loop.
key=['roll_no','name','age']
value=[1,'Amit',18]
print(key)
print(value)
result={}
for i in range(len(key)):
   result[key[i]]=value[i]
print("After merging two list in one dictionary: ")
print(result)