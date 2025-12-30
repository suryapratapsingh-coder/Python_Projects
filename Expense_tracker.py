expenses_list = []
print("----Welcome to Expense Tracker----")

while True:
    print("===Menu===")
    print("1. Add Expense ")
    print("2. View All Expense ")
    print("3. View Total Spending ")
    print("4. Exit ")

    choice = int(input(" Please Enter Your Choice :"))

    #ADD expenses

    if(choice==1):
        date= input("Enter The Date:")
        category = input("Enter the Category:")
        description = input("Enter the Details: ")
        amount = float(input("Enter the Amount:"))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses_list.append(expense)
        print("...expense Added succesfully...")

    # view all expesnse
    elif(choice==2):
        if(len(expenses_list)==0):
            print("No Expenses")
        else:
            print("All Expenses:")
            count = 1
            for eachexpense in expenses_list:
                print(f"Expense No.{count}=={eachexpense["date"]},{eachexpense["category"]},{eachexpense["description"]},{eachexpense["amount"]} ")
                count = count + 1

    # 3. view total spending
    elif(choice == 3):
        total=0
        for eachexpense in expenses_list:
            total = total + eachexpense["amount"]
            print("\n Total Spending ", total)

    # EXIT
    elif(choice == 4):
        print("...End...")
        break

    else:
        print("invalid input")                            