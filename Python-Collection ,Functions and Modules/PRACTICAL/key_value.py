#Write a Python program to separate keys and values from a dictionary using keys() and values() methods.
student = {
    'Roll no': 1,
    'Fname'  :"Khursheed",
    'Lname':'Khan',
    'subject' :'python',
    'duration' : '6 months',
    'score': 80 
}#create dictionary
print("Keys are ->",end=" ")
print(student.keys())
print("Values are -> ",end=" ")
print(student.values())