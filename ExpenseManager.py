def main():
    records = []

    while True:
        print("\nExpense Manager")
        print("1. Add Record")
        print("2. View Records")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_record(records)
        elif choice == "2":
            view_records(records)
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_record(records):
    record_type = input("Enter type (expense/income): ").strip().lower()
    if record_type not in ["expense", "income"]:
        print("Invalid type. Please enter 'expense' or 'income'.")
        return
    
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Rent, Salary): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    description = input("Enter description: ")

    record = {
        "type": record_type,
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    records.append(record)
    print("Record added successfully!")

def view_records(records):
    if not records:
        print("No records found.")
        return
    
    print("\nAll Records:")
    for i, record in enumerate(records, start=1):
        print(f"{i}. {record['type'].capitalize()} | Date: {record['date']} | Category: {record['category']} | Amount: {record['amount']} | Description: {record['description']}")

if __name__ == "__main__":
    main()
