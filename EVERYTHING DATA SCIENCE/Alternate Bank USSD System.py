# BUILDING A MOBILE BANK APP SYSTEM ---> Using Functional Programming
# STAGE 1: Storage
account_balance = 0
withdrawals = []
deposit = []
all_transactions = {}

network = ["Airtel", "MTN", "GLO", "9mobile"]

# STAGE 2: Definig all functions/actions this bank system can perform
def airtime():
    pass # Buy for ourselves and Buy for others

def get_data():
    pass # Get data for self and others

def bank_statement():
    return all_transactions

def foreign_currency_exchange():
    pass # We need to define a system that can mirror different exchange rates

def pay_bills():
    pass # Subsriptions (Netflix, Gotv, Dstv, Spectranet)



# -----> PROGRAM STARTS
# firstname = input("Firstname: ").strip().capitalize()
# lastname = input("Lastname: ").strip().capitalize()
# age = int(input("Age: "))
# network = input("Network ('Airtel', 'MTN', 'GLO', '9mobile'): ").strip().capitalize()
# phonenumber = input("Phone Number (e.g 09076488226): ").strip()

while True:
    print("Welcome to Leon's Bank App")
    print("\nPress 1: View bank balance\nPress 2: Deposit\nPress 3: Withdrawals\nPress 4: Airtime\nPress 5: Get Data\nPress 6: Bank Statement\nPress 7: Pay Bills\nPress 8: Go back to previous menu")
    action = int(input("RESPONSE: "))
    if action == 1:
        print(f"\nBalance: {account_balance}")
        
    elif action == 2:
        amountDeposit = int(input("Deposit: "))
        if amountDeposit < 500:
            print("\nYou can't deposit an amount less than 500 Naira")
        else:
            account_balance = account_balance + amountDeposit
            deposit.append(account_balance)
            
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














