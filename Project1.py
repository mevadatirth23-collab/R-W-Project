# Interactive Personal Data Collector

# Welcome message
print("Welcome to the Interactive Personal Data Collector!\n")

# Collect Information from user
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_number = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

# Display collected information with type and memory address
print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number: {fav_number} (Type: {type(fav_number)}, Memory Address: {id(fav_number)})")

# Perform calculation: Birth Year estimation
current_year = 2025
birth_year = current_year - age
print(f"\nYour birth year is approximately: {birth_year} (based on your age of {age})")

# Example of type casting
height_int = int(height)
print(f"Rounded height (converted from float to int): {height_int}")

# Exit message
print("\nThank you for using the Personal Data Collector. Goodbye!")
