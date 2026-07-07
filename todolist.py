# a python file to create to-do list

task=[]
complete_task=[]
features=("1.Add task",
          "2.Remove task",
          "3.View task",
          "4.Search task",
          "5.Clear all task",
          "6.Task Completed",
          "7.Completed all task",
          "8.exit",
)

while True:

    for feature in features: 
        print(feature)
    user_input=int(input("enter the input as (1,2,3,4,5,6 i.e. as numbers to access features)"))
    
    if user_input==1:
        task_name=input('name the task you would like to add in your to-do list')
        task.append(task_name)
        print(f"the user has added task {task_name}")
        print()
    elif user_input==2:
        remove_task=input("enter the task you would like to remove")
        if remove_task in task:
          print("the task has been removed")
          task.remove(remove_task)
        elif remove_task in complete_task:
            print("task has been completed are you sure")
            user_input2=input("enter yes to delete.")
            if user_input2=="yes":
                complete_task.remove(remove_task)               
            else:
                print(f"the user has denied to delete")

        else:
          print("task not found")
        print()
    elif user_input==3:
        for x in task:
         print(x)
        print()

    elif user_input==4:
        search_task=input("enter the task you want to search:-")
        if search_task in task:
            print('task is incomplete')
        elif search_task in complete_task:
            print("task has been completed")
        elif search_task not in complete_task and search_task not in task:
            print("task not in list")
        else:
            print("some error by the user")

    elif user_input==5:
        user_input_clr_tsk=int(input("enter 1 or 2 (1 for removing current task 2 for removing all completed task:-)"))
        if user_input_clr_tsk==1:
            user_input_clr_tsk_confirm=input("are you sure you want to remove all task enter yes to remove:-")

            if user_input_clr_tsk_confirm=="yes":
             task.clear()

        elif user_input_clr_tsk==2:
            user_input_clr_tsk_confirm_2=input("are you sure you want to remove all task enter yes to remove:-")
            if user_input_clr_tsk_confirm_2=="yes":
             complete_task.clear()
            else:
                print("user denied")

    elif user_input==6:
        complete_task_usr=input("enter the task you have completed")

        if complete_task_usr in task:
            print(f"the {complete_task_usr} has been completed")
            complete_task.append(complete_task_usr)
            task.remove(complete_task_usr)

        elif complete_task_usr not in task:
            print("task is not in current_task")

        else:
            print("system error")

    elif user_input==7:
        for x in task:
            complete_task.append(x)
        task.clear()

    elif user_input==8:
        print("you have successfully exited to-do list")
        break
