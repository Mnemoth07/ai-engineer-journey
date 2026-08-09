#////////////////////////////////////////
# These are the functions

from http.client import FOUND


roster = []

def adding_students(roster):
    repeat = "y"
    while repeat:

        new_student = {}

        new_student['name'] = input("Student's Name: ")
        new_student['instrument'] = input("Student's Instrument: ")
        new_student['grade'] = int(input("Student's Grade: "))
        new_student['years_playing'] = int(input("Years playing: "))
        
        roster.append(new_student)
        
        repeat = input("\nAdd another student? y/n: ")
        repeat = repeat.lower() == "y"
        print("")
    
    return roster

def print_roster(roster):
    kick = 0
    while kick < len(roster):
        print(f"\nStudent: {roster[kick]['name']}\nInstrument: {roster[kick]['instrument']}\nGrade: {roster[kick]['grade']}\nYears Playing: {roster[kick]['years_playing']}\n\n")

        kick += 1

def search_roster(roster):
    
    repeat = "y"
    while repeat:
        search = input("Student's name: ")
    
        found = False

        for new_student in roster:
            if new_student['name'] == search:
                print(f"\nStudent: {new_student['name']}\nInstrument: {new_student['instrument']}\nGrade: {new_student['grade']}\nYears Playing: {new_student['years_playing']}\n")
            
                found = True
                break

        if not found:
            print("\nStudent not found.")
        repeat = input("\nSearch for another student? y/n: ")
        repeat = repeat.lower() == "y"
        print("")

#///////////////////////////////////////////////////////////////

# This is the site:

adding_students(roster)

print("\n===========")
print("Band roster")
print("===========\n")
print_roster(roster)
print("\n================")

print("\nGo ahead and search a student!\n")
search_roster(roster)

print("Have a good day!")