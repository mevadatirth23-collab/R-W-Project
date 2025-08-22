# Pattern Generator and Number Analyzer with Input Validation

def generate_pattern():
    while True:
        try:
            rows = int(input("Enter the number of rows for the pattern: "))
            if rows <= 0:
                print("Error: Row count must be a positive integer. Please try again.\n")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.\n")

    print("Pattern:")
    for i in range(1, rows + 1):
        print("*" * i)
    print()
def analyze_numbers():
    while True:
        try:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))

            if start > end:
                print("Error: Start of range must be less than or equal to end. Please try again.\n")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter integers only.\n")

    total_sum = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(f"Number {num} is Even")
        else:
            print(f"Number {num} is Odd")
        total_sum += num

    print(f"Sum of all numbers from {start} to {end} is: {total_sum}\n")


def main():
    # Welcome message and instructions
    print("Welcome to the Pattern Generator and Number Analyzer!\n")
    print("This program allows you to:")
    print("- Generate patterns (right-angled triangle).")
    print("- Analyze a range of numbers (odd/even and sum).\n")

    while True:
        print("Select an option:")
        print("1. Generate a Pattern")
        print("2. Analyze a Range of Numbers")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_pattern()
        elif choice == "2":
            analyze_numbers()
        elif choice == "3":
            # Exit message
            print("\nThank you for using the Student Data Organizer.")
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

# Run the program
if __name__ == "__main__":
    main()