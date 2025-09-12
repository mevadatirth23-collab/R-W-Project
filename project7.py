# Install required external module (run once)
# pip install colorama

import datetime
import time
import math
import random
import uuid
import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)

# Custom Modules (File Operations)

class FileManager:
    @staticmethod
    def create_file(filename):
        with open(filename, 'w') as f:
            pass
        print(Fore.GREEN + f"File '{filename}' created successfully!")

    @staticmethod
    def write_file(filename, data):
        with open(filename, 'w') as f:
            f.write(data)
        print(Fore.GREEN + "Data written successfully!")

    @staticmethod
    def read_file(filename):
        try:
            with open(filename, 'r') as f:
                content = f.read()
            print(Fore.CYAN + f"File Content:\n{content}")
        except FileNotFoundError:
            print(Fore.RED + "File not found!")

    @staticmethod
    def append_file(filename, data):
        with open(filename, 'a') as f:
            f.write(data)
        print(Fore.GREEN + "Data appended successfully!")

# Date and Time Functions

def show_current_datetime():
    now = datetime.datetime.now()
    print(Fore.YELLOW + "Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_date_difference():
    d1 = input("Enter first date (YYYY-MM-DD): ")
    d2 = input("Enter second date (YYYY-MM-DD): ")
    date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    diff = abs((date2 - date1).days)
    print(Fore.YELLOW + f"Difference: {diff} days")

def format_date():
    d = input("Enter a date (YYYY-MM-DD): ")
    date_obj = datetime.datetime.strptime(d, "%Y-%m-%d")
    print(Fore.YELLOW + "Formatted Date:", date_obj.strftime("%A, %d %B %Y"))

def stopwatch():
    input("Press Enter to start stopwatch...")
    start = time.time()
    input("Press Enter to stop stopwatch...")
    end = time.time()
    print(Fore.YELLOW + f"Elapsed Time: {round(end - start, 2)} seconds")

def countdown():
    t = int(input("Enter countdown time in seconds: "))
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(Fore.YELLOW + timer, end="\r")
        time.sleep(1)
        t -= 1
    print(Fore.GREEN + "Time's up!")

# Math Operations

def calculate_factorial():
    n = int(input("Enter a number: "))
    print(Fore.YELLOW + f"Factorial: {math.factorial(n)}")

def compound_interest():
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest (%): "))
    t = float(input("Enter time (years): "))
    ci = p * ((1 + r/100) ** t)
    print(Fore.YELLOW + f"Compound Interest: {round(ci, 2)}")

def trig_calculations():
    angle = float(input("Enter angle in degrees: "))
    rad = math.radians(angle)
    print(Fore.YELLOW + f"sin({angle}) = {math.sin(rad)}")
    print(Fore.YELLOW + f"cos({angle}) = {math.cos(rad)}")
    print(Fore.YELLOW + f"tan({angle}) = {math.tan(rad)}")

def area_of_circle():
    r = float(input("Enter radius: "))
    area = math.pi * r * r
    print(Fore.YELLOW + f"Area of Circle: {area}")

# Random Data Generation

def generate_random_number():
    print(Fore.YELLOW + f"Random Number: {random.randint(1, 100)}")

def generate_random_list():
    lst = random.sample(range(1, 100), 5)
    print(Fore.YELLOW + f"Random List: {lst}")

def generate_random_password():
    length = int(input("Enter password length: "))
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    print(Fore.YELLOW + f"Generated Password: {password}")

def generate_random_otp():
    otp = random.randint(100000, 999999)
    print(Fore.YELLOW + f"Generated OTP: {otp}")

# UUID Generator

def generate_uuid():
    print(Fore.YELLOW + f"Generated UUID: {uuid.uuid4()}")

# Dynamic Module Explorer

def explore_module():
    module_name = input("Enter module name to explore (e.g. math): ")
    try:
        module = sys.modules.get(module_name) or __import__(module_name)
        print(Fore.CYAN + f"Available attributes in {module_name}:")
        print(dir(module))
    except ImportError:
        print(Fore.RED + "Module not found!")

# Menu System

def main_menu():
    while True:
        print(Fore.CYAN + "\n===== Multi-Utility Toolkit =====")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            datetime_menu()
        elif choice == '2':
            math_menu()
        elif choice == '3':
            random_menu()
        elif choice == '4':
            generate_uuid()
        elif choice == '5':
            file_menu()
        elif choice == '6':
            explore_module()
        elif choice == '7':
            print(Fore.GREEN + "Thank you for using the Multi-Utility Toolkit!")
            break
        else:
            print(Fore.RED + "Invalid choice, try again.")

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            show_current_datetime()
        elif choice == '2':
            calculate_date_difference()
        elif choice == '3':
            format_date()
        elif choice == '4':
            stopwatch()
        elif choice == '5':
            countdown()
        elif choice == '6':
            break
        else:
            print("Invalid choice!")

def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Circle")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            calculate_factorial()
        elif choice == '2':
            compound_interest()
        elif choice == '3':
            trig_calculations()
        elif choice == '4':
            area_of_circle()
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            generate_random_number()
        elif choice == '2':
            generate_random_list()
        elif choice == '3':
            generate_random_password()
        elif choice == '4':
            generate_random_otp()
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            fname = input("Enter file name: ")
            FileManager.create_file(fname)
        elif choice == '2':
            fname = input("Enter file name: ")
            data = input("Enter data to write: ")
            FileManager.write_file(fname, data)
        elif choice == '3':
            fname = input("Enter file name: ")
            FileManager.read_file(fname)
        elif choice == '4':
            fname = input("Enter file name: ")
            data = input("Enter data to append: ")
            FileManager.append_file(fname, data)
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()
