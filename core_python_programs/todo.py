tasks = ["Buy milk", "Study Python", "Workout"]

while True:
    print("\n1. Add task\n2. View tasks\n3. Delete task\n4. Exit")
    taskOption = input("Please choose option number: ")

    match taskOption:
        case '1':
            newTask = input("Enter task: ").strip()
            if newTask:
                tasks.append(newTask)
                print("Task added successfully")
            else:
                print("Task cannot be empty")

        case '2':
            if not tasks:
                print("No tasks available")
            else:
                print("------------- Tasks -------------")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        case '3':
            if not tasks:
                print("No tasks to delete")
            else:
                try:
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")

                    taskNumber = int(input("Enter task number: "))

                    if 1 <= taskNumber <= len(tasks):
                        del tasks[taskNumber - 1]
                        print("Task deleted successfully")
                    else:
                        print("Invalid task number")

                except ValueError:
                    print("Please enter a valid number")

        case '4':
            print("Goodbye!")
            break

        case _:
            print("Invalid option, try again.")
