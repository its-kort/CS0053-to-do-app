# toDoApp.py

tasks = []


def add_task(task):
    tasks.append(task)
    print("\nTask Added!!\n")


def show_tasks():
    if len(tasks) == 0:
        print("No Tasks Yet.\n")
    else:
        for i in range(len(tasks)):
            print(i+1, ".", tasks[i])


def remove_task(task_number):
    tasks.pop(task_number)
    print("\nTask Removed!!\n")


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
        
        choice = input("Enter choice : ")
        print("-----------------")
        
        if choice == "1":
            task = input("Enter task : ")
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
            print("\nThank you and Goodbye!!\n")
            break
        else:
            print("\nWrong Choice!!\n")


if __name__ == "__main__":
    main()