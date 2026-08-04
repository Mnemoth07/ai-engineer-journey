name = input("What is your name? ")
years = float(input("How many years have you been playing? "))
practice = input("Do you practice at home? ")
practice = practice.lower() == "yes"
score = float(input("What is your audition score? "))

if score >= 90 and years >= 3 and practice:
    print(f"Welcome to Varsity, {name}!")

elif score >= 80 and years >= 2 and practice:
    print(f"Welcome to Mid-High Band, {name}!")

elif score >= 70 and years >= 1 and practice:
    print(f"Welcome to Intermediate Band, {name}")

else:
    print(f"Unfortunately, you will no longer be in band, {name}.")