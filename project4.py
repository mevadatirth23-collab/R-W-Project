# Functional Treat
dataset = []
summary = {}

def display_summary():
    """Display dataset summary using built-in functions"""
    global dataset, summary
    if not dataset:
        print("No dataset found. Please input data first!")
        return
    total = len(dataset)
    minimum = min(dataset)
    maximum = max(dataset)
    summation = sum(dataset)
    average = summation / total
    summary = {
        "total": total,
        "min": minimum,
        "max": maximum,
        "sum": summation,
        "average": average
    }
    print("\nData Summary:")
    for k, v in summary.items():
        print(f"- {k.capitalize()} value: {v}")

def calculate_average():
    """User-defined function to calculate average"""
    if not dataset:
        print("Dataset is empty!")
        return
    avg = sum(dataset) / len(dataset)
    print(f"Average of dataset: {avg}")


def find_duplicates():
    """User-defined function to find duplicates in dataset"""
    if not dataset:
        print("Dataset is empty!")
        return
    duplicates = [x for x in dataset if dataset.count(x) > 1]
    print("Duplicates:", set(duplicates) if duplicates else "No duplicates found")

def print_args(*args, **kwargs):
    """Function demonstrating *args and **kwargs"""
    print("Args:", args)
    print("Kwargs:", kwargs)

def factorial(n):
    """Recursive function to calculate factorial"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def filter_data_by_threshold():
    """Filter dataset using lambda and threshold"""
    global dataset
    if not dataset:
        print("Dataset is empty!")
        return
    threshold = int(input("Enter threshold value: "))
    filtered = list(filter(lambda x: x >= threshold, dataset))
    print(f"Filtered Data (>= {threshold}):", filtered)

def dataset_statistics():
    """Return multiple dataset statistics"""
    if not dataset:
        print("Dataset is empty!")
        return
    return min(dataset), max(dataset), sum(dataset), sum(dataset) / len(dataset)

def sort_data():
    """Sort dataset in ascending or descending order"""
    global dataset
    if not dataset:
        print("Dataset is empty!")
        return
    print("1. Ascending\n2. Descending")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        dataset.sort()
        print("Sorted Data (Ascending):", dataset)
    else:
        dataset.sort(reverse=True)
        print("Sorted Data (Descending):", dataset)

# Main Menu

def main_menu():
    """Main menu for Functional Treat Program"""
    while True:
        print("\nWelcome to Functional Treat Program")
        print("Main Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")

        choice = input("Please enter your choice: ")

        if choice == "1":
            global dataset
            dataset = list(map(int, input("Enter numbers separated by spaces: ").split()))
            print("Data has been stored successfully!")
        elif choice == "2":
            display_summary()
        elif choice == "3":
            num = int(input("Enter a number to calculate factorial: "))
            print(f"Factorial of {num} is: {factorial(num)}")
        elif choice == "4":
            filter_data_by_threshold()
        elif choice == "5":
            sort_data()
        elif choice == "6":
            stats = dataset_statistics()
            if stats:
                print(f"Dataset Statistics:\n- Minimum: {stats[0]}\n- Maximum: {stats[1]}\n- Sum: {stats[2]}\n- Average: {stats[3]:.2f}")
        elif choice == "7":
            print("Thank you for using Functional Treat. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()