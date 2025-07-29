tasks = []
sh
for i in range(1,6):
    task = input(f"Enter task {i}: ")
    tasks.append(task)

print(f"Your tasks :")
for t in tasks :
    print("-",t)

remove_task = ""

while remove_task != "stop":

    remove_task = input("Enter one task you want to remove: ")

    if remove_task == "stop":
        break

    if remove_task in tasks:
      tasks.remove(remove_task)
      print(f"\n {remove_task} has been removed.")

    else:
        print(f"\n'{remove_task}' was not found in your list.")



print("\nUpdated Task List: ")
for t in tasks: 
    print("-", t)
