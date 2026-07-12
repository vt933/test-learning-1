# Core Features

# 1. Add Student
#    - Enter student name
#    - Enter student marks
#    - Store data in dictionary

# 2. Update Student Marks
#    - Search student by name
#    - Update marks if student exists

# 3. View All Students
#    - Display all student names and marks

# 4. Search Student
#    - Search student by name
#    - Display marks if found

# 5. Delete Student
#    - Remove student from dictionary

# 6. Count Students
#    - Display total number of students

# 7. Highest Scorer
#    - Display student with highest marks

# 8. Lowest Scorer
#    - Display student with lowest marks

# 9. Average Marks
#    - Calculate and display average marks

# 10. Exit
#     - Close the application

students={}

while True:
   #menu
   menu=("1.Add student",
         "2.Update student",
         "3.View Student",
         "4.Search Student",
         "5.Delete Students",
         "6.Count Students",
         "7.Highest Scorers",
         "8.Lowest Scoreres",
         "9.Average Marks",
         "10.Exit"
)
   for x in menu:
     print(x)

   user_input=int(input("enter the number you want to enter in for accessing the terminal:-"))
    #add student
   if user_input==1:
     name_student=input("enter the name of student:-")
     if name_student in students:
      print("student already exist do you want to update his marks:-")
     else:
       marks_students=int(input("enter the marks of student you want to enter:-"))
       students.update({name_student:int(marks_students)})
   #update marks
   elif user_input==2:
     search_student=input("enter the name of student you want to search:-")
     if search_student in students:
       print(f"student {search_student} exist in data ")
       updated_marks=int(input(f"enter the new marks of {search_student}:-"))
       students.update({search_student:updated_marks})
       

     elif search_student not in students:
       print("student is not in the list already so marks won't be updated")
     else:
       print("something is not correct")

   elif user_input==3:
     for name in students:
       print(name,students[name])

   elif user_input==4:
     search_student2=input("enter the name of student you want to find")
     if search_student2 in students:
       print(f"student {search_student2} is in the record")
     else:
       print(f"student {search_student2} is not in the list")

   elif user_input==5:
    del_student=input("enter the name of student you want to delete.") 
    confirm_del_student=input(f"the student {del_student} is in record are you sure you want to remove him (enter Yes if you want to remove).")
    if del_student in students and confirm_del_student=="Yes":  
     del students[del_student]   
    elif del_student in students and not confirm_del_student=="Yes":
      print(f"you have confirmed that you don't want to delete data of {del_student} student")
    else:
      print(f"{del_student} is not in record")

   elif user_input==6:
    print(len(students))

   elif user_input==7:
     for name,marks in students:
      print(max(students[name]))
     
   elif user_input==8:
     for name,marks in students:
      print(min(students[name]))

   elif user_input==9:
     for i,x in students:
       y=sum(x)
       z=y/len(students)
       print(f"Class average is {z}")
    
   elif user_input==10:
     print("you have succesfully exited the programme.")
     break
   
   else:
     print("invalid input")