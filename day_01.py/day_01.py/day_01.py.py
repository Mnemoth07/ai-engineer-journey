name = input("What is your name? ")
job = input("What career do you currently have? ")
goal = input("What career do you want? ")
hours = float(input("How many hours will you study each week? "))
years = float(input("How many years do you think it will take to reach your goal? "))
salary = float(input("How much do you hope to make in salary? "))

weeks_per_year = 52
annual_hours = hours * weeks_per_year

print()
print(f"{name} currently works as a {job}.")
print(f"His goal is to become an {goal}.")
print(f"At {hours:g} hours per week for {years:g} years, he will complete {annual_hours*years:g} hours of preparation.")
print(f"His long-term target salary is ${salary:g}")