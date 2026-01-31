from datetime import datetime
# Expense Tracker
expense = []
print("Welcome to My Expense Tracker")
print("=" * 40)

while True:
    print("\nChoose the following option to Continue...")
    print("1. Add Expense")
    print("2. Show Expense")
    print("3. Total Expense")
    print("4. Monthly Total Expense")
    print("5. Exit Expense")

    try:
        choice = int(input("Enter your Choice: "))
    except ValueError:
        print("Please Enter Integer Choice")
        continue

    if choice == 1:
        print("\nTo Add Expenses Please give the following Detail")
        date = input("Enter the date [dd-mm-yyyy]: ")
        try:
            datetime.strptime(date,"%d-%m-%Y")
            
        except ValueError:
            print("Invalid date!!!")
            continue


        category = input("Enter the category of expense: ")

        try:
            amount = float(input("Enter the Amount: "))
        except ValueError:
            print("Invalid amount")
            continue

        expenses = {
            "date": date,
            "category": category,
            "amount": amount
        }
        expense.append(expenses)
        print("Expense Successfully Added")

    elif choice == 2:
        if not expense:
            print("List is empty...Add expenses to it")
        else:
            print("\nFollowing are the expenses")
            print("-" * 40)
            print("Date\t\tCategory\tAmount")
            print("-" * 40)
            for e in expense:
                print(f"{e['date']}\t{e['category']}\t\t{e['amount']}")

    elif choice == 3:
         if not expense:
            print("List is empty...Add expenses to it")
         else:
             total = 0
             for e in expense:
                total += e["amount"]
             print("Total Expense =", total)
    elif choice==4:
        total=0
        month=input("Enter the Month of year(Example:01-2025)")
        for e in expense:
            if e['date'][3:]==month:
                total+=e['amount']
        print("Total Expenses in month",total)

    elif choice == 5:
        break

    else:
        print("Invalid Choice")

print("\nThanks for using My Expense Tracker")
