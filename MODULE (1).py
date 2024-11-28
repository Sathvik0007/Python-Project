#calendar
import calendar
def display_calendar(year, month):
    print(calendar.month_name[month], year) 
    print(calendar.month(year, month))  
if __name__ == "__main__":
    year = int(input("Enter the year (e.g., 2024): "))
    month = int(input("Enter the month (1-12): "))
    if 1 <= month <= 12:
        display_calendar(year, month)
    else:
        print("Invalid month! Please enter a month between 1 and 12.")

# Calculate the cc of the bike
import math
def calculate_cc(bore, stroke, cylinders):
    displacement = (math.pi / 4) * (bore ** 2) * stroke * cylinders
    return displacement
if __name__ == "__main__":
    print("Bike Engine CC Calculator")
    try:
        bore = float(input("Enter the bore (diameter of the cylinder in cm): "))
        stroke = float(input("Enter the stroke (length of the piston travel in cm): "))
        cylinders = int(input("Enter the number of cylinders: "))
        if bore <= 0 or stroke <= 0 or cylinders <= 0:
            print("Error: All values must be positive numbers.")
        else:
            engine_cc = calculate_cc(bore, stroke, cylinders)
            print(f"The engine displacement is: {engine_cc:.2f} CC")

    except ValueError:
        print("Error: Please enter valid numeric values.")

#Temp
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    try:
        choice = int(input("Choose an option (1 or 2): "))
        if choice == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F.")
        elif choice == 2:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C.")
        else:
            print("Invalid option selected!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()

#password checker
import re

def check_password_strength(password):
    """Check the strength of a password based on specific criteria."""
    strength = 0
    criteria = [
        (len(password) >= 8, "At least 8 characters long"),
        (any(char.islower() for char in password), "Contains lowercase letters"),
        (any(char.isupper() for char in password), "Contains uppercase letters"),
        (any(char.isdigit() for char in password), "Contains numbers"),
        (re.search(r"[!@#$%^&*(),.?\":{}|<>]", password), "Contains special characters"),
    ]

    for condition, _ in criteria:
        if condition:
            strength += 1

    return strength, [rule for condition, rule in criteria if not condition]

def main():
    """Main function to check password strength."""
    print("Password Strength Checker")
    password = input("Enter a password: ")

    strength, missing_criteria = check_password_strength(password)

    if strength == 5:
        print("Strong Password!")
    else:
        print("Weak Password.")
        print("Missing the following criteria:")
        for criteria in missing_criteria:
            print(f"- {criteria}")

if __name__ == "__main__":
    main()
