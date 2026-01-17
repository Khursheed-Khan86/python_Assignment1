#Write a Python program to update a value in a dictionary.
student = {
    'Roll no': 1,
    'Fname'  :"Khursheed",
    'Lname':'Khan',
    'subject' :'python',
    'duration' : '6 months',
    'score': 80 
}
print(student)
student['score']=90 #updating value of score
print("----------After Updation of Score-----------")
print(student)
