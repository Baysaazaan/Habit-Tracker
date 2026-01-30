#Personal tracker

tasks = []
good_habits = []
bad_habits = []
good_habits_counter = 0
bad_habits_counter = 0
tasks_counter = 0

while True:
    print("\n--- PERSONAL TRACKER ---")
    print("1. Add task")
    print("2. Complete task")
    print("3. View tasks")
    print("4. Add habit")
    print("5. View habits")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        Add_task = input("Enter the task you want to add: ")
        if Add_task not in tasks:
            tasks.append(Add_task)
            print(f"{Add_task} is now added to tasks 😊")
        else:
            print("You can't add the same task!")
    elif choice == "2":
        Complete_task = input("Enter the task you want to select as completed: ")
        if Complete_task in tasks:
            tasks.remove(Complete_task)
            print("Task completed 😊")
        else:
            print("Task not found 🥲")

    elif choice == "3":
        if len(tasks):
            print("-- Your current tasks are: --\n")
            tasks_counter = 0
            for x in tasks:
                tasks_counter += 1
                print(f"{tasks_counter}. " + x, end=" \n")
        else:
            print("\nThere is no task to do\n")

    elif choice == "4":
        Add_habit = input("Enter the habit you want to add: ")
        if Add_habit in good_habits or Add_habit in bad_habits:
            print("You can't add the same habit!")
        else:
            Habit_check = input("Is this a good or a bad habit( g / b ): ")
            if Habit_check.lower() == "g" and Add_habit not in good_habits:
                good_habits.append(Add_habit)
                print(f"{Add_habit} is now added to good habits😊")
            elif Habit_check.lower() == "b" and Add_habit not in bad_habits:
                    bad_habits.append(Add_habit)
                    print(f"{Add_habit} is now added to bad habits🥲")
            elif Add_habit in good_habits or Add_habit in bad_habits:
                print("You can't add the same habit!")
            else:
                print("Invalid option😐")

    elif choice == "5":
        if len(good_habits) > 0:
            print("-- Your good habits are: --")
            good_habits_counter = 0
            for y in good_habits:
                good_habits_counter += 1
                print(f"{good_habits_counter}. " + y, end="\n")
        else:
            print("\nYou currently don't have any good habits")
        if len(bad_habits) > 0:
            print("-- Your bad habits are: --")
            bad_habits_counter = 0
            for z in bad_habits:
                bad_habits_counter += 1
                print(f"{bad_habits_counter}. " + z, end="\n")
        else:
            print("\nYou currently don't have any bad habits")

    elif choice == "6":
        print("Bye 👋")
        break
    else:
        print("Invalid option 😐")
