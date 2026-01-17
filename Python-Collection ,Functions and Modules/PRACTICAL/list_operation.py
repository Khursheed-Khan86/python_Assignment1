#Write a Python program to add elements to a list using insert() and append(). 
my_list=[]
# append insert at last position
my_list.append("python")
my_list.append("java")
my_list.append("php")
print(my_list)
my_list.insert(1,"c++")#insert at index 1(second position)
my_list.insert(-1,"c")#insert at position just before  last element
print(my_list)
my_list.insert(len(my_list),"flutter")#insert at last position
print(my_list)
