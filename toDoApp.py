# toDoApp.py

tasks = []


def add_task(task): #adds task to the list, it will append each time the user will add task
    task = task.strip()
    if task == "":
        print("\nCannot add an empty task.\n")
        return
    tasks.append(task)
    print("\nTask added!\n")


def show_tasks(): #shows the present tasks listed. If there are no task it'll print out "No tasks yet."
    if len(tasks) == 0:
        print("No tasks yet.\n")
    else:
        for i in range(len(tasks)): 
            print(f"{i+1}. {tasks[i]}") #prints out each element on the list


def remove_task(task_number): #pops out an element depending on what the user which element s/he wants to remove
    if 0 <= task_number < len(tasks):
        removed = tasks.pop(task_number)
        print(f"\nTask removed! -> {removed}\n")
    else:
        print("\nPlease enter a valid task number.\n")


def main():
    print("=================")
    print("TASK TRACKER")

    while True:
        print("=================")
        print("MAIN MENU")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        print("=================")

        choice = input("Enter choice: ")
        print("-----------------")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter task number to remove: "))
                remove_task(task_number - 1)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("\nThank you and goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
