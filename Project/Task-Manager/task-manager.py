file_name = "task_manager.txt"


def taskManager():
    print("-----------------------")
    print("1. Add task")
    print("2. View task")
    print("3. Mark task as completed")
    print("4. Mark task as pending")
    print("5. Delete task")
    print("6. Exit ")


def add_task():
    while True:
        task = input("Enter the task you want to add: ")
        if not task:
            print("Task cannot be empty")
            continue
        try:
            with open(file_name, "a") as f:
                f.write(task + "\n")
            print("Task added successfully!")
        except IOError:
            print("Error occurred while adding the task.")

        user = input("Do you want to add more task? (y/n)")
        if user == "y":
            continue
        else:
            break


def view_task():
    try:
        with open(file_name) as f:
            tasks = f.readlines()
        if not tasks:
            print("No task here!")
            return
        for j, task in enumerate(tasks, 1):
            print(f"{j}. {task.rstrip()}")
    except IOError:
        print("Error occurred while viewing the tasks.")


def mark_task_as_completed():
    view_task()
    while True:
        task_no = input("Enter the task no. you want to mark as completed..: ")
        try:
            with open(file_name) as f:
                tasks = f.readlines()

            if task_no.isdigit():
                task_no = int(task_no)

                if 1 <= task_no <= len(tasks):

                    task = tasks[task_no - 1]
                    if "[completed]" not in task:
                        read_task = task.rstrip("\n") + "\t[completed]" + "\n"
                        tasks.remove(task)
                        tasks.insert(task_no - 1, read_task)

                        try:
                            with open(file_name, "w") as f:
                                f.writelines(tasks)
                            print("Task is marked as completed!")
                        except IOError:
                            print(
                                "Error occurred while marking the task as completed.")
                    else:
                        print("The task is already marked as completed!!!")
                else:
                    print("Invalid task number!")
                    continue
            else:
                print("The task number should be a digit!")
                continue

        except IOError:
            print("Error occurred while marking the task as completed.")
            continue

        user = input("Do you want to mark more task as completed? (y/n):  ")
        if user != "y":
            break


def mark_task_as_pending():
    while True:
        task_no = input("Enter the task no. you want to mark as pending..: ")
        try:
            with open(file_name) as f:
                tasks = f.readlines()
                print(type(tasks))
                print(tasks)

            if task_no.isdigit():
                task_no = int(task_no)

                if 1 <= task_no <= len(tasks):

                    task = tasks[task_no - 1]
                    if "[completed]" not in task:
                        print("The task in not completed yet!!!")
                    else:
                        read_task = task.replace("[completed]", "")
                        tasks.remove(task)
                        tasks.insert(task_no - 1, read_task)
                        try:
                            with open(file_name, "w") as f:
                                f.writelines(tasks)
                            print("Task is marked as pending!")
                        except IOError:
                            print(
                                "Error occurred while marking the task as pending.")
                else:
                    print("Invalid task number!")
                    continue
            else:
                print("The task number should be a digit!")
                continue

        except IOError:
            print("Error occurred while marking the task as pending.")
            continue

        user = input("Do you want to mark more task as pending? (y/n):  ")
        if user != "y":
            break


def delete_task():
    user = input("Enter the task number you want to delete: ")
    try:
        task_number = int(user)
        with open(file_name) as f:
            tasks = f.readlines()
        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)
            try:
                with open(file_name, "w") as f:
                    f.writelines(tasks)
                print("Task deleted successfully!")
            except IOError:
                print("Error occurred while deleting the task.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input! Task number should be an integer.")


def main():
    try:
        while True:
            taskManager()
            main_menu = input("What do you want to do press (1-6):\n")
            if main_menu == "1":
                add_task()
            elif main_menu == "2":
                view_task()
            elif main_menu == "3":
                mark_task_as_completed()
            elif main_menu == "4":
                mark_task_as_pending()
            elif main_menu == "5":
                delete_task()
            elif main_menu == "6":
                print("Thank you so much!!!")
                break
            else:
                print("Invalid input!!!")

            user = input("Do you want to perform any other task? (y/n):  ")
            while (user != "y" and user != "n"):
                print("Please enter a valid option")
                user = input("Do you want to perform any other task? (y/n):  ")
            if user == "n":
                break
            if user == "y":
                continue

    except:
        print("Something went wrong , please try again.")


main()
