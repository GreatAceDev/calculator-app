print("--- The Great Universal Time Converter Ace Edition ---")
choice = input("Enter the unit you have (Days, Hours, Minutes, Months, or Years): ").lower()

if choice == "days":
    days = float(input("Enter number of days: "))
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    months = days / 30.44
    years = days / 365.25
    print(f"{days:.2f} days = {hours:.2f} hours, {minutes:.2f} minutes, {seconds:.2f} seconds, {months:.2f} months, or {years:.2f} years.")

elif choice == "hours":
    hours = float(input("Enter number of hours: "))
    days = hours / 24
    minutes = hours * 60
    seconds = minutes * 60
    months = days / 30.44
    years = days / 365.25
    print(f"{hours:.2f} hours = {days:.2f} days, {minutes:.2f} minutes, {seconds:.2f} seconds, {months:.2f} months, or {years:.2f} years.")
    print("You'r Welcome")
elif choice == "minutes":
    minutes = float(input("Enter number of minutes: "))
    hours = minutes / 60
    days = hours / 24
    seconds = minutes * 60
    months = days / 30.44
    years = days / 365.25
    print(f"{minutes:.2f} minutes = {days:.4f} days, {hours:.2f} hours, {seconds:.2f} seconds, {months:.2f} months, or {years:.2f} years.")
    print("You'r Welcome")
elif choice == "months":
    months = float(input("Enter number of months: "))
    # MATH: To get days, multiply months by 30.44. Then use previous math logic.
    days = months * 30.44
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    years = days / 365.25 # Divide days by 365.25
    print(f"{months:.2f} months = {days:.2f} days, {hours:.2f} hours, {minutes:.2f} minutes, {seconds:.2f} seconds, or {years:.2f} years.")
    print("You'r Welcome")
elif choice == "years":
    years = float(input("Enter number of years: "))
    days = years * 365.25
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    months = years * 12
    print(f"{years:.2f} years = {days:.2f} days, {hours:.2f} hours, {minutes:.2f} minutes, {seconds:.2f} seconds, or {months:.2f} months.")
    print("You'r Welcome")
else:
    print("Invalid choice! Try typing Days, Hours, Minutes, Months, or Years.")
