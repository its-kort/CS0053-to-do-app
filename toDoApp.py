# toDoApp.py

tasks=[]
<<<<<<< HEAD
def addtask(task) :
    tasks.append(task)
    print("\nTask Added!!\n")

def showTasks( ):
    print("TASKS")
    if len(tasks)==0 :
        print("No Tasks Yet.\n")
    else:

        for i in range (len(tasks)):
            print(f"{i+1}. {tasks[i]}\n")

def removetask(task_number):
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
            if choice =="1":
                tasks = input("Enter task : ")

                addtask(tasks)
            elif choice =="2":
                showTasks()
            elif choice =="3":
                try:
                    task_number =int(input("Enter task no to remove: "))
                    removetask(task_number)
                except ValueError:
                        print("Please enter a valid number.")
            elif choice =="4":
                print("\nThank you and Goodbye!!\n")
                break;
            else:
                print("\nWrong Choice!!\n")

if __name__ == "__main__":
    main()
=======

def addtask(task) :
  tasks.append(task)
  print("task added!")

def showTasks( ):
    if len(tasks)==0 :
      print("no tasks yet")
    else:
     for i in range (len(tasks)):
      print(i+1,".",tasks[i])

def removetask(tasknumber):
    tasks.pop(tasknumber) 
    print("task removed!!")

def main():
    while True:
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4- Exit")
        ch = input("enter choice : ")
        if ch=="1":
            t = input("enter task : ")
            addtask(t)
        elif ch=="2":
            showTasks()
        elif ch=="3":
            n=int(input("enter task no to remove: "))
            removetask(n)   
        elif ch=="4":
            break;
        else:
            print("wrong choice!!")
main()
>>>>>>> main
