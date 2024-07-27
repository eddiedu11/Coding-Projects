def main():

    def display():
        print("\nCurrent Tasks:")
        for index, task in enumerate(tasks):
            status = "Completed" if task["Completion"] else "Not Completed"
            print(f"{index + 1}. {task['Task']} - {status}")

    tasks = [] 

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Complete Task")
        print("4. Exit")
        print("======================")

        choice = input("Enter your choice: ")

        # Switch choices
        if choice == "1":   
            n_tasks = int(input("How many tasks do you want to add? ")) 

            for i in range(n_tasks):
                task = input("Enter the task: ") 
                tasks.append({"Task": task, "Completion": False})
                print("Task Added!")

        elif choice == "2":
            display() 
        
        elif choice == "3":
            display() 
            task_index = int(input("Which task did you complete?: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["Completion"] = True
                print("Task marked as Completed!") 
            else:
                print("Invalid Task Index!") 
        
        elif choice == "4":
            print("\nExiting To-Do List.")
            break
        
        else:
            print("Invalid Choice. Please Try Again!")
    
if __name__ == "__main__":
    main() 
