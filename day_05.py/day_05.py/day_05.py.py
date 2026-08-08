def collect_students(students, repeat):
    while repeat:
        new_student = input("\nAdd another student: ")
        students.append(new_student)
        repeat = input("\nWould you like to add another student? y/n: ")
        repeat = repeat.lower() == "y"
    return(students, repeat)

def print_roster(students, shelf):
    print("\n===========")
    print("Band Roster")
    print("===========\n")
    while shelf < len(students):
        print(students[shelf])
        shelf += 1
    print(f"\nTotal Students: {len(students)}")
    print("========================\n")

def search_student(repeat_one, students):
    while repeat_one:
        laze = input("\nSearch Student: ")
        if laze in students:
            print(f"\n{laze} is enrolled!")
        else: print("\nnot enrolled.")
        repeat_one = input("\nSearch another student? y/n: ")
        repeat_one = repeat_one.lower() == "y"

repeat = input("Would you like to add students? y/n: ")
students = []

collect_students(students, repeat)

shelf = 0

print_roster(students, shelf)

repeat_one = input("\nWould you like to search for a student in your roster? y/n: ")

search_student(repeat_one, students)

print("Have a good day!")