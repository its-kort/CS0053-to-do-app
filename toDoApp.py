tasks=[]
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

def removetask(tasknumber):
    tasks.pop(tasknumber)
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
            ch = input("Enter choice : ")
            print("-----------------")
            if ch=="1":
                t = input("Enter task : ")

                addtask(t)
            elif ch=="2":
                showTasks()
            elif ch=="3":
                n=int(input("Enter task no to remove: "))
                removetask(n)
            elif ch=="4":
                print("\nThank you and Goodbye!!\n")
                break;
            else:
                print("\nWrong Choice!!\n")

main()
