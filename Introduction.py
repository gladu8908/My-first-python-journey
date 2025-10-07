"""
Introduction to Python Basics

This script contains my first Python experiments while learning:
- Printing output
- Basic arithmetic
- Variables and updating values
- Checking data types

"""
#1.

"""Running My first PYTHON SCRIPT"""

print("I Love Python")



"""Basic arithmetic"""


print(19 + 17)
print(99 - 12)

print(9 * 2)
print(120 / 12)

"""VARIABLES"""

 print("Working with Variables:")
 customer_age = 27
    account_balance = 120.50
    print("  Initial account balance:", account_balance)

    # Updating values
    account_balance = 20_000.00
    is_millionaire = False
    print("  Updated balance:", account_balance, "| Millionaire?", is_millionaire)

    account_balance = 1_300_000.00
    is_millionaire = True
    print("  Updated balance:", account_balance, "| Millionaire?", is_millionaire)
    print()

"""Checking data types"""

 print("Data Types:")
    customer_age = 49            # int
    account_balance = 120_078.89  # float
    is_millionaire = False        # bool

    print("  customer_age:", customer_age, "| type:", type(customer_age).__name__)
    print("  account_balance:", account_balance, "| type:", type(account_balance).__name__)
    print("  is_millionaire:", is_millionaire, "| type:", type(is_millionaire).__name__)
    print()

