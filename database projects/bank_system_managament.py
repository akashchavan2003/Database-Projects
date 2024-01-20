import datetime
import bcrypt
import sqlite3


class customer:
    pass


class Account:
    pass


class Transaction:
    pass


class Fdaccount:
    pass


class RDaccount:
    pass


class Loan:
    pass


def authenticate_user(username, entered_password):
    # Retrieve hashed password from the database based on the username
    connection = sqlite3.connect('bank_manage.db')
    cursor = connection.cursor()

    cursor.execute("SELECT hashed_password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    connection.close()

    if result:
        stored_hashed_password = result[0]
        # Check if the entered password matches the stored hash
        if bcrypt.checkpw(entered_password.encode('utf-8'), stored_hashed_password):
            print("Authentication successful!")
            return True
        else:
            print("Authentication failed.")
            return False
    else:
        print("User not found.")
        return False


print("PlEASE LOGIN FIRST")
un = input("Enter User name")
pa = input("Enter Password")
result = authenticate_user(un, pa)
if result:
    print("Select main menu")
    print("1.Customer Management")
    print("2.Advanced Accounts")
    print("3.Transaction history")
    print("4.Data Analysis And Reporting")
    print("5.Log Out")
    ch = input("Enter You Choice")
    if ch == 1:
        print("Select following operations")
        print("1.Create Account")
        print("2.View Account Detail")
        print("3.Deposit Money")
        print("4.Withdraw money")
        print("5.Transfer money")
        print("6.Check Balance")
        print("7.Account Statement")
        print("Close Account")
        print("9.Exit")
        ch = input("Enter your Choice")
        if ch == 1:
            pass
        elif ch == 2:
            pass
        elif ch == 3:
            pass
        elif ch == 4:
            pass
        elif ch == 5:
            pass
        elif ch == 6:
            pass
        elif ch == 7:
            pass
        elif ch == 8:
            pass
        elif ch == 9:
            exit(0)
    elif ch == 2:
        print("Select following operation")
        print("1.Create Fixed Deposit Account")
        print("2.Create Recurring Deposit Account")
        print("3.Grant a Loan")
        ch = input("Enter your Choice")
        if ch == 1:
            pass
        elif ch == 2:
            pass
        elif ch == 3:
            pass

    elif ch == 3:
        print("Enter Your Choice")
        print("1.View Day book")
        print("2.Analyze Cash in Hand")
        print("3.Customer Transaction History")
        ch = input("Enter Your Choice")
        if ch == 1:
            pass
        elif ch == 2:
            pass
        elif ch == 3:
            pass

    elif ch == 4:
        print("Enter your choice")
        print("1.Total Accounts")
        print("2.Balance Sheet")
    elif ch == 5:
        exit(0)
    else:
        print("Both Username And Password Is Wrong")
