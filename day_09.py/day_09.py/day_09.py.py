from pathlib import Path

file_path = Path(__file__).parent / "roster.csv"

def get_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            return(number)
        except ValueError:
            print("Please enter a whole number.\n")

def get_text(prompt):
    while True:
        text = input(prompt).strip()

        if text:
            return text
        else:
            print("This field cannot be blank.\n")
        

def adding_students():
    repeat = True

    while repeat:
        new_student = {}

        new_student['name'] = get_text("Student's Name: ")
        new_student['instrument'] = get_text("Student's Instrument: ")
        new_student['grade'] = get_integer("Student's Grade: ")
        new_student['years_playing'] =get_integer("Years playing: ")

        with open(file_path, "a") as file:
            file.write(
                f"{new_student['name']}," 
                f"{new_student['instrument']}," 
                f"{new_student['grade']}," 
                f"{new_student['years_playing']}\n"
            )
        
        repeat = input("\nAdd another student? y/n: ")
        repeat = repeat.lower() == "y"
        print()


def view_roster():
    try:
        print("=============")
        print("Band Roster!")
        print("=============\n")

        with open(file_path, "r") as file:            
            for line in file:
                    student_info = line.strip().split(",")

                    print()
                    print(f"Student Name: {student_info[0]}")
                    print(f"Student Instrument: {student_info[1]}")
                    print(f"Grade: {student_info[2]}")
                    print(f"Years Playing: {student_info[3]}")
            print("\n===========================\n")
    except FileNotFoundError:
        print("No roster has been created yet")

def search_roster():
        search = input("Enter Student's Name: ").strip().lower()
        found = False

        with open(file_path, "r") as file:
            for line in file:
                student_info = line.strip().split(",")
                
                name = student_info[0]
                instrument = student_info[1]
                grade = student_info[2]
                years_playing = student_info[3]

                if name.lower() == search:
                    print()
                    print("Student Found!")
                    print(f"Student Name: {name}")
                    print(f"Student Instrument: {instrument}")
                    print(f"Grade: {grade}")
                    print(f"Years Playing: {years_playing}")

                    found = True
                    break

        if not found:
            print()
            print("Student not found.")

def main_menu():
    while True:
        print()
        print("==========================")
        print("   Band Roster Manager")
        print("==========================")
        print("\n1. Add Student")
        print("2. View Roster")
        print("3. Search Student")
        print("4. Exit\n")

        choice = input("Choose an option: ")

        if choice == "1":
            print("")
            adding_students()

        elif choice == "2":
            print("")
            view_roster()

        elif choice == "3":
            print("")
            search_roster()

        elif choice == "4":
            print("")
            print("\nGoodbye!")
            break

        else:
            print("")
            print("\nInvalid choice.")


main_menu()
