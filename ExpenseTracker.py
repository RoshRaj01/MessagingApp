import json
import os


def menu():
    
    print("Welcome to Expense Manager 2.0")
    print("1. List of Expenses")
    print("2. New Expense")
    print("3. Total Expenses")
    print("4. Exit")
        
    ch = input("Choose an option: ")
    return ch

def new_expense():
    type = int(input("Enter type 1. Expense, 2. Income: "))
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    return type, category, amount, description

def total_expense():
    for i in data["expense"]:
            ExpTotal += IncTotal + i

    for i in data["income"]:
        IncTotal += IncTotal + i

    total = ExpTotal + IncTotal
    return total

if os.path.exists('data.json'):
    with open('data.json','r') as file:
        data = json.loads(file.read())
else:
    print("New Program initializing...")
    data = {
        'income': [],
        'expense': []
    }

    
while True:
    ch = menu()

    if ch == "1":
        for i in data["expense"]:
            print(i)

    elif ch == "2":
        type, category, amount, description = new_expense()
        details = {
            "category": category, 
            "amount": amount, 
            "description": description
            }
        if type == 1:
            data["expense"].append(details)
        elif type == 2:
            data["income"].append(details)
        else:
            print("Invalid input, couldn't add the last expense:",details.__str__())

    elif ch == "3":
        print("The total:",total_expense())
    
    elif ch == "4":
        with open('data.json','w') as file:
            json.dump(data,file)
        print("Exciting the code...")
        break
