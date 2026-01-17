#Write a Python program to iterate over a list using a for loop. 
my_list=[10,20,30,40,50,60]
print("----Iteration using each element-------")
for item in my_list:  #iteration using element
    print(item,end=" ")
print("----Iteration using Index--------")
for i in range(len(my_list)):#iteration using index
    print(my_list[i],end=" ")