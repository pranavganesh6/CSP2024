# List to store different categories of monthly expenses
expenses = []

# List to store budget summaries for each run
budget_history = []

# This function calculates total expenses and remaining balance
# Parameters: salary (int), list of expenses
def calculate_budget(salary, expenses_list):
    total = 0
    for expense in expenses_list:
        total += expense
    savings = salary - total

    # Output results
    print("\n----- Budget Summary -----")
    print("Total Monthly Income: $" + str(salary))
    print("Total Monthly Expenses: $" + str(total))
    print("Remaining Balance: $" + str(savings))

    if savings > 0:
        print("Nice! You are saving money.")
    elif savings == 0:
        print("You’re breaking even.")
    else:
        print("Warning! You’re spending more than you make.")

    # Store the summary in a dictionary and append to history
    summary = {
        "salary": salary,
        "expenses": expenses_list.copy(),  # use copy to prevent accidental overwrite
        "total_expenses": total,
        "remaining_balance": savings
    }
    budget_history.append(summary)

    return savings

# Welcome message
print("Welcome to the Budget Tracker!")
home_type = input("Do you live in a house or apartment? ").lower()
salary = int(input("What is your monthly salary? $"))

# Ask specific questions based on home type
if home_type == "apartment":
    rent = int(input("How much is your monthly rent? $"))
    utilities = int(input("How much do you spend on utilities? $"))
    parking = int(input("How much is your parking fee? $"))
    expenses.extend([rent, utilities, parking])

elif home_type == "house":
    mortgage = int(input("How much is your monthly mortgage? $"))
    property_tax = int(input("How much are your property taxes per month? $"))
    maintenance = int(input("How much do you spend on maintenance? $"))
    expenses.extend([mortgage, property_tax, maintenance])
else:
    print("Unknown home type. No housing costs added.")

# General expenses
groceries = int(input("How much do you spend on groceries? $"))
transportation = int(input("How much do you spend on transportation? $"))
entertainment = int(input("How much do you spend on entertainment? $"))
expenses.extend([groceries, transportation, entertainment])

# Calculate and store the budget summary
calculate_budget(salary, expenses)

