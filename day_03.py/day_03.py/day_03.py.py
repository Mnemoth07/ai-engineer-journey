again = "y"
varsity = 0
symphonic = 0
concert = 0
bye = 0

while again:
    name = input("Name of student: ")
    years = float(input("Years in band: "))
    practice = input("Practice at home? ")
    practice = practice.lower() == "yes"
    score = float(input("Score? "))
    again = "yes"
    again = again.lower() == "yes"

    if score >=90 and practice and years > 2:
        print(f"{name} Should be in Varsity Band.\n")
        varsity += 1

    elif score >=80 and practice and years > 1:
        print(f"{name} Should be in Mid-High Band.\n")
        symphonic += 1

    elif score >=70 and years > 0:
        print(f"{name} Should be in Intermediate Band.\n")
        concert += 1

    else: 
        print(f"{name} should no longer be in band.\n")
        bye += 1

    again = input("Do you want to put another student in? y/n ")
    print("")
    again = again.lower() == "y"

print(f"Audition Summary\n\nVarsity: {varsity}\nSymphonic: {symphonic}\nConcert: {concert}\nKicked out: {bye}")