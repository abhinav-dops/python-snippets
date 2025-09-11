import os
import shutil
from datetime import datetime

log_file = "organizer.log"
undo_file = "undo.json"

# Log each action to a file
def log_action(message):
    with open(log_file, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

# Show the log content
def show_log():
    if os.path.exists(log_file):
        with open(log_file, "r") as log:
            print("\n📝 Log File:")
            print(log.read())
    else:
        print(" No log file found.")

# Organize files by file extension
def organize_by_extension(folder_path):
    undo_stack = []

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        if os.path.isfile(full_path):
            ext = filename.split(".")[-1] if "." in filename else "no_extension"
            target_folder = os.path.join(folder_path, ext)

            os.makedirs(target_folder, exist_ok=True)
            target_path = os.path.join(target_folder, filename)
            shutil.move(full_path, target_path)

            undo_stack.append((target_path, full_path))
            log_action(f"Moved '{filename}' to '{ext}/'")

    # Save undo info
    with open(undo_file, "w") as f:
        for src, dest in undo_stack:
            f.write(f"{src}::{dest}\n")

    print(" Files organized by extension.")

# Organize files by last modified date
def organize_by_date(folder_path):
    undo_stack = []

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        if os.path.isfile(full_path):
            mod_time = os.path.getmtime(full_path)
            date_folder = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")

            target_folder = os.path.join(folder_path, date_folder)
            os.makedirs(target_folder, exist_ok=True)

            target_path = os.path.join(target_folder, filename)
            shutil.move(full_path, target_path)

            undo_stack.append((target_path, full_path))
            log_action(f"Moved '{filename}' to '{date_folder}/'")

    with open(undo_file, "w") as f:
        for src, dest in undo_stack:
            f.write(f"{src}::{dest}\n")

    print("Files organized by date.")

# Undo the last move by reading the undo file
def undo_last_move():
    if not os.path.exists(undo_file):
        print("No undo data available.")
        return

    with open(undo_file, "r") as f:
        lines = f.readlines()

    for line in reversed(lines):
        src, dest = line.strip().split("::")
        if os.path.exists(src):
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.move(src, dest)
            log_action(f"Undo: Moved '{os.path.basename(src)}' back to original location.")
        else:
            print(f"File not found: {src}")

    os.remove(undo_file)
    print(" Undo completed.")

# Command-line menu
def main():
    folder_path = input(" Enter the folder path to organize: ").strip()

    while True:
        print("\n What would you like to do?")
        print("1. Organize by file extension")
        print("2. Organize by modified date")
        print("3. Undo last move")
        print("4. Show log file")
        print("5. Exit")

        choice = input(" Enter your choice (1-5): ")

        if choice == "1":
            organize_by_extension(folder_path)
        elif choice == "2":
            organize_by_date(folder_path)
        elif choice == "3":
            undo_last_move()
        elif choice == "4":
            show_log()
        elif choice == "5":
            print(" Exiting...")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
