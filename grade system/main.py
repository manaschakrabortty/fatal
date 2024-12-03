'''
DICTIONARY
COLLECTION  DATA TYPE =KEY+VALUE =PAIR =DATA
LEFT SIDE =KEY
RIGHT SIDE = VALUE
{KEY1:VALUE1, KEY 2:VALUE2}
'''
'''
add
update
delete
view
exit
'''
# #create a dictionary
# students = {
#     'paras':100,
#     'manas':99
# }
# ##Accesing a element
# print(students['paras'])
# #uptodate the element
# students['manas'] = 300
# #delete an element
# del students['manas']
# print(students)



#Iinitialising dictionary

students_grade = { }

#add a new Studets
def add_student(name, grade):
    students_grade[name] =grade
    #[sagar] =100
    print(f"Added {name} with a {grade}")
    #Added sagar with grade a 100

#update a student
def update_student(name, grade):
    if name in students_grade:
        students_grade[name] = grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found!")

#Delete a student
def delete_student(name):
    if name in students_grade:
        del students_grade[name]
        print(f"{name} has been succesfully deleted")
    else:
        print(f"{name} is not found!")

#view all students
def display_all_students():
    if students_grade:
        for name, grade in students_grade.items():
            print(f"{name} : {grade}")
    else:
        print("No sudents found/added")


def main():
    while True:
        print('\n Student Grade Management System')
        print("1. Added Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View  Student")
        print("5.  Exit ")

        choice  = int(input("Enter what you want to show"))

        if choice ==1:
            name = input("Enter Student name= ")
            grade = int(input("Enter Student Grade "))
            add_student(name,grade)
        elif choice==2:
            name = input("Enter Student name= ")
            grade = int(input("Enter Student  Grade "))
            update_student(name,grade)
        elif choice ==3:
            name = input("Enter Student name= ")
            delete_student(name)
        
        elif choice ==4:
            display_all_students()
        
        elif choice ==5:
            print("Exit thr program")
            break
        else:
            print("Invaid choice")

