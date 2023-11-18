# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:39:00 2023

@author: lEO
"""

# BUILDING A MOBILE BANK APP SYSTEM ---> Using Functional Programming
# STAGE 1: Storage
bankUsers = []
usersDatabase = {}

network = ["Airtel", "MTN", "GLO", "9mobile"]

accountNumber = set([])

# STAGE 2: Definig all functions/actions this bank system can perform
def get_account_balance():
    pass

def transfer():
    pass

def deposit():
    amountDeposit = int(input("Deposit: "))
    pass
    # This will only work in the program 

def withdrawal():
    pass
    # This will only work in the program

def airtime():
    pass # Buy for ourselves and Buy for others

def get_data():
    pass # Get data for self and others

def bank_statement():
    pass

def foreign_currency_exchange():
    pass # We need to define a system that can mirror different exchange rates

def pay_bills():
    pass # Subsriptions (Netflix, Gotv, Dstv, Spectranet)

def create_account_number():
    number = 10001
    while True:
        if number in accountNumber:
            number += 1
        else:
            accountNumber.add(number)
            return number

def create_bank_user():
    # 1) Fix network dependency so people must enter correct network
    # 2) Phone numbers must be 11 characters
    
    firstname = input("Firstname: ").strip().capitalize()
    lastname = input("Lastname: ").strip().capitalize()
    age = int(input("Age: "))
    network = input("Network ('Airtel', 'MTN', 'GLO', '9mobile'): ").strip().capitalize()
    phonenumber = input("Phone Number (e.g 09076488226): ").strip()
    account_balance = 0
    accountnum = create_account_number()
    
    accountNumber.add(accountnum)
    bankUsers.append(firstname)
    usersDatabase[accountnum] = {
                            "Firstname": firstname,
                            "Lastname": lastname,
                            "Age": age,
                            "AccountBalance": account_balance,
                            "Network": network,
                            "PhoneNumber": phonenumber,
                            "Withdrawals": {},
                            "Deposits": {},
                            "AllTransactions": {},
                            }
    
    print("Welcome to the fastest banking service in Africa, we are committed to helping you succed. Congratulations on the successful opening of your bank account.")




# -----> PROGRAM STARTS
while True:
    print("Welcome to Leon's Bank App")
    print("\nPress 1: Open an account \nPress 2: Log in \nPress 3: Exit")
    choice = int(input("RESPONSE: "))
    if choice == 3:
        break
    elif choice == 2:
        pass
    elif choice == 1:
        create_bank_user()
        print("\nPress 1: View bank balance\nPress 2: Deposit\nPress 3: Withdrawals\nPress 4: Airtime\nPress 5: Get Data\nPress 6: Bank Statement\nPress 7: Pay Bills\nPress 8: Go back to previous menu")
        action = int(input("RESPONSE: "))
        if action == 1:
            pass
        elif action == 2:
            pass
        elif action == 3:
            pass
        elif action == 4:
            pass
        elif action == 5:
            pass
        elif action == 6:
            pass
        elif action == 7:
            pass
        elif action == 8:
            pass
        else:
            print("Invalid Response")














