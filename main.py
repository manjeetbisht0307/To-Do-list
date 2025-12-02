# Input values:
# 1. Add Task
# 2. Show Tasks
# 3. Edit Task
# 4. Exit
# Select an option: 1
# Enter task: Buy groceries
# Output value:
# Task added successfully.
task={}
list=True
while list:
    user_input=int(input(("1. Add \n2. Show Tasks \n3. Edit Task as done \n4. Exit\nOnly Numeric\n")))
    if user_input==1:
        add_task=input(("Add your task in To-Do list\n"))
        task[add_task]="undone"
        print("Task added successfully!")
    elif user_input==2:
        print(f"Tasks-\n")
        for item in task:
            print(f"{item}-{task[item]}")
        print("\n")
    elif user_input==3:
        edit_task=input("Enter the Task to mark as done-\n").lower()
        task[edit_task]="Done"
    else:
        list=False





