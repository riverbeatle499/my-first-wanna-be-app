tasks = []
done = []
print("hey my russian brother enjoy me creation")
while True:
    user_input = input("what are your tasks btw when you done just type the word done ")
    if user_input == "done":
        break
    tasks.append(user_input)
    done.append("[]")
print("now lets see what tasks are done")
while True:
    print("\n--- your current tasks ---")
    for i in range(len(tasks)):
        print(i + 1, done[i], tasks[i])
    choice = input("\nType the task number you did but if you want to quit type 'exit' : ")
    if choice == "exit":
        print("i knew you were too lazy")
        break
    task_number = int(choice)
    index = task_number - 1
    done[index] = "[X]"
    print("task done")