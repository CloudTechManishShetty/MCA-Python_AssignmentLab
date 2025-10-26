import os

FILE_NAME = "students.txt"

def safeguard_file_operation():
    print("--- Safeguarding File: ",FILE_NAME," ---")

    try:
        with open(FILE_NAME, 'r') as file:
            print("File '",FILE_NAME,"' found and opened successfully.")
            content = file.read().strip()
            if content:
                print("Content preview:\n" + content[:100] + ("..." if len(content) > 100 else ""))
            else:
                print("File is empty.")

    except FileNotFoundError:
        print("File '",FILE_NAME,"' is missing. Creating a new file...")
        try:
            with open(FILE_NAME, 'w') as file:
                file.write("Student Records:\n")
                file.write("Name, Age, Grade\n")
            print("New file '",FILE_NAME,"' created successfully.")
        except IOError as e:
            print("Error creating file: ",e)
    
    except Exception as e:
        print("An unexpected error occurred: ",e)

if os.path.exists(FILE_NAME):
    os.remove(FILE_NAME)
    print("(Cleaned up previous '",FILE_NAME,"' for fresh demo)")

safeguard_file_operation()
print("\n--- Demonstration complete. Running again to show 'File found' case ---")
safeguard_file_operation()