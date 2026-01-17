#Write a Python program to sort a list using both sort() and sorted().
list1=[12,34,56,88,99,80,56]
print(list1) 
list1.sort()#it will sort original list1 in ascending order
print(list1)
list2=['A','D','T','U','L']
print(list2)
print(sorted(list2))#it will print sorted list in ascending order,original list will not change
print(list2)
list2.sort()
print(list2)
list3=[1,2,3,4,8,70,23,6]
print(list3)
list3.sort(reverse=True)#it will sort list in descending order
print(list3)
