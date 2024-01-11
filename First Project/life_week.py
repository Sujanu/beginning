# to display remaining days in days week month format

age = input("enter your current age: ")

years = 90 - int(age)

weeks = years *  52

days = weeks * 7  # or days = years * 365

months = years * 12  # or months = years * 12


print(f"You have {days} days, {weeks} weeks, and {months} months left ")