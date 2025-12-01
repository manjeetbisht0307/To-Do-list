# Input values:
# 1. Add Task
# 2. Edit Task
# 3. Delete Task
# 4. Exit
# Select an option: 1
# Enter task: Buy groceries
# Output value:
# Task added successfully.
task={}
list=True
while list:
    user_input=int(input(("1. Add \n2. Show Tasks \n3. Delete Task \n4. Exit\n")))
    if user_input==1:
        add_task=input(("Add your task in To-Do list"))
        task[add_task]="undone"
    elif user_input==2:
        print(f"Tasks-\n")
        for item in task:
            print(item)
    elif user_input==3:
        edit_task=input("Enter the Task").lower()
        task[edit_task]="Done"





