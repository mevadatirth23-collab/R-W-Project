import os
from datetime import datetime

class Journal:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        entry = input("\nEnter your journal entry:\n")
        try:
            with open(self.filename, "a") as f:
                time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
                f.write(time + " " + entry + "\n")
            print("Entry added successfully!\n")
        except:
            print("Error: Could not write entry.")

    def view_entries(self):
        if not os.path.exists(self.filename):
            print("No journal entries found. Start by adding a new entry!")
            return
        try:
            with open(self.filename, "r") as f:
                data = f.readlines()
                if len(data) == 0:
                    print("No journal entries found. Start by adding a new entry!")
                else:
                    print("\nYour Journal Entries:")
                    print("-----------------------")
                    for line in data:
                        print(line.strip())
        except:
            print("Error: Could not read entries.")

    def search_entry(self):
        if not os.path.exists(self.filename):
            print("No journal file found. Please add a new entry first.")
            return
        key = input("Enter a keyword or date to search: ")
        found = False
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    if key.lower() in line.lower():
                        if not found:
                            print("\nMatching Entries:")
                            print("-----------------------")
                        print(line.strip())
                        found = True
            if not found:
                print("No entries found for:", key)
        except:
            print("Error while searching entries.")
    def delete_entries(self):
        if not os.path.exists(self.filename):
            print("No journal entries to delete.")
            return
        choice = input("Are you sure you want to delete all entries? (yes/no): ")
        if choice.lower() == "yes":
            try:
                os.remove(self.filename)
                print("All journal entries have been deleted.")
            except:
                print("Error: Could not delete entries.")
        else:
            print("Delete cancelled.")

def main():
    journal = Journal()
    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            journal.add_entry()
        elif choice == "2":
            journal.view_entries()
        elif choice == "3":
            journal.search_entry()
        elif choice == "4":
            journal.delete_entries()
        elif choice == "5":
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
