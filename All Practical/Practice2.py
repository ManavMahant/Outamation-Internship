# List, Tuple, Dictionary, Set
"""
marks = [94 , 87 , 79 , 89 , 97 , 66 , 75 , 67]
print(marks)
print(type(marks))
print(marks[2])
print(marks[6])
print(len(marks))


student = ["Manav" , "Jay" , "Dharmik" , "Dhruv" , "Taksh" , "Smit" , "Kush" , "Pranav" , "Dev"]
print(student)
student[1] = "Sahal"
print(student) 


student1 = ["Sahal" , 70 , "Khambhat"]
print(student1)
student1[0] = "Smit"
print(student1)

print(student[1:6])

marks.append(78)
marks.sort(reverse=True)
print(marks) 

print(marks[2])"""

"""movies = []
movies.append(input("Enter 1st movies name = "))
movies.append(input("Enter 2nd movies name = "))
movies.append(input("Enter 3rd movies name = "))
print(movies)"""

"""list = [1,2,3,4,3,2,4]
copy_list = list.copy()
copy_list.reverse()

if (copy_list == list):
    print("List is Pelindrome")
else:
    print("List is Not Pelindrome")
"""

"""info = {
    "Name"     : "Manav",
    "Age"      : 22,
    "Hight"    : 5.7,
    "Is Adult" : True
    }

print(info["Name"])
print(info["Age"])
info["Name"] = "Dharmik"
info["surname"] = "Patel"
info["Age"] = 23
print(info)
"""
"""
studentinfo = {
    "Name" : "Manav",
    "Sub" : 
    {
        "math" : 88,
        "sci"  : 90,
        "phy"  : 85,
        "cem"  : 87
    }
}
print(studentinfo["Name"])
print(studentinfo["Sub"])
print(studentinfo)"""

subject = {
    "c++", "python", "java", "javascript", "java", "python", "c", "c++", "python", "javascript"
           }
print(subject)
print(len(subject))