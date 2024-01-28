import datetime

import time
import sqlite3
import bcrypt
import logging

logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum logging level
    format="%(asctime)s - %(levelname)s - %(message)s"  # Define the format of log messages
)


def get_current_date():
    # this returns the date to other functions
    current_date = datetime.datetime.now().date()
    return current_date


def create_ac():
    # it creates the account no in the database by using simple query INSERT
    nm = input("Enter The Customer Full Name")
    at = input("Enter The Account Type")
    ad = input("enter Customer Full Address")
    mn = input("Enter The Customer Mobile NO.")
    an = input("Enter the Customer Aadhar NO.")
    pn = input("Enter The Pan card NO")
    con = sqlite3.connect("bank_manage.db")
    dt = get_current_date()
    con.execute("""
        INSERT INTO personal_bank_account
        (account_holder_name, balance, account_type, opening_date, address, mobile_number, aadhar_card_number, pan_card_number)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (nm, 0, at, dt, an, pn, an, pn))
    con.commit()
    con.close()
    print("...........Customer Account Created successfully........")


class Customer:
    # This class is separately for Editing the customer personal information only
    # it gives parameter by using its constructor is only a account no.
    def __init__(self, an):
        self.an = an

    def change_pan(self):
        pn = input("Enter pan card Number to Update")
        con = sqlite3.connect("bank_manage.db")
        q = "UPDATE personal_bank_account SET pan_card_number=? WHERE account_number=?"
        con.execute(q, (pn, self.an))
        logging.info("Pan Card Number Updated Successfully")

    def change_card_number(self):
        pn = input("Enter aadhar card Number to Update")
        con = sqlite3.connect("bank_manage.db")
        q = "UPDATE personal_bank_account SET aadhar_card_number=? WHERE account_number=?"
        con.execute(q, (pn, self.an))
        logging.info("Pan Card Number Updated Successfully")

    def change_mobile_no(self):
        mn = input("Enter Mobile card Number to Update")
        con = sqlite3.connect("bank_manage.db")
        q = "UPDATE personal_bank_account SET mobile_number=? WHERE account_number=?"
        con.execute(q, (mn, self.an))
        logging.info("Mobile Number Updated Successfully")

    def get_balance(self):
        con = sqlite3.connect("bank_manage.db")
        cur = con.cursor()
        q = "SELECT balance FROM personal_bank_account WHERE accont_number=?"
        cur.execute(q, self.an)
        result2 = cur.fetchone()
        print("Balance is", result2[0])


class Wallet:
    # This class is for only purpose of handling cash in hand transaction
    # this class get initial amt amount that we give by fetching from our database at the time of calling
    # Firstly its return the cash in hand or Another function set the cash in hand
    def __init__(self, set_amt):
        self.set_amt = set_amt

    def cash_in_hand_return(self):
        return self.set_amt

    def cash_in_hand_deposit(self):
        try:
            con3 = sqlite3.connect("bank_manage.db")
            try:
                q = "UPDATE cash_in_hand SET cash_in_hand=cash_in_hand + ?"
                con3.execute(q, (self.set_amt,))
                con3.commit()
                con3.close()
            except sqlite3.Error as e:
                con3.rollback()
                logging.info("Transaction Failed.....")
        except sqlite3.OperationalError:
            logging.warning("Error while connecting to database")

    def cash_in_hand_withdraw(self):
        try:
            con3 = sqlite3.connect("bank_manage.db")
            try:
                q = "UPDATE cash_in_hand SET cash_in_hand=cash_in_hand - ?"
                con3.execute(q, (self.set_amt,))
                con3.commit()
                con3.close()
            except sqlite3.Error as e:
                con3.rollback()
                logging.info("Transaction was failed...", e)
        except sqlite3.Error as error:
            logging.warning("Error while connecting to Database...")


class Account:
    # This is major class of this program it's having some main member functions are included in it this class
    # inherits the class Wallet in it Class Wallet have an one argument called initial Class Account have one
    # argument called an Account number Because of this argument or Inheritance we have to call a base class
    # constructor manually that why pythons allowed to call a manual constructor
    def __init__(self, an2, amt6):
        self.amt2 = amt6
        self.an2 = an2

    def deposit(self):
        # Here we have to deposit cash in customers balance so we have to do firstly give an ac no. to class then give
        # amt to the member function and the class wallet get its their initialized value from the fetching if else by
        # fetching from database so now only we have to do adding and subtraction logic in the member function for
        # respective
        try:
            con4 = sqlite3.connect("bank_manage.db")
            try:
                q1 = "UPDATE personal_bank_account SET balance=balance + ? WHERE account_number=?"
                con4.execute(q1, (self.amt2, self.an2))
                con4.commit()
                con4.close()
                ob = Wallet(self.amt2)
                ob.cash_in_hand_deposit()
                logging.info("Amount deposited to AC NO.%s", self.an2)
            except sqlite3.Error as e:
                con4.rollback()
                logging.info("Transaction failed:", e)
        except sqlite3.Error as e:
            logging.warning("Database connection failed....")

    def withdraw(self):

        try:
            con4 = sqlite3.connect("bank_manage.db")
            try:
                q1 = "UPDATE personal_bank_account SET balance=balance - ? WHERE account_number=?"
                con4.execute(q1, (self.amt2, self.an2))
                con4.commit()
                con4.close()
                ob = Wallet(self.amt2)
                ob.cash_in_hand_withdraw()
                logging.info("Amount Withdrawn from AC NO.%s", self.an2)
            except sqlite3.Error as e:
                con4.rollback()
                logging.info("Transaction Failed", e)
        except sqlite3.OperationalError:
            logging.info("Error while connecting to database...")

    def revoke_transaction(self, tr_no):
        pass

    def change_balance(self, amt2):
        pass

    def transfer(self, amt2, payee_ac_no):
        pass

    def apply_interest(self, intrest, period):
        pass

    def close_ac(self):
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
    try:
        connection = sqlite3.connect('bank_manage.db')
        cursor = connection.cursor()

        cursor.execute("SELECT hashed_password, bank_name FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

        connection.close()

        if result:
            stored_hashed_password = result[0].encode('utf-8')  # Convert hashed password to bytes
            if bcrypt.checkpw(entered_password.encode('utf-8'), stored_hashed_password):
                logging.info("Authentication successful!")
                return True, result[1]
            else:
                logging.warning("Authentication failed.")
                return False
        else:
            logging.warning("User not found.")
            return False
    except TypeError as e:
        logging.critical("An error occurred during authentication: %s", e)
        return None



print(".........BANK MANAGEMENT SOFTWARE.........")
print("PlEASE LOGIN FIRST")
un = input("Enter User name")
pa = input("Enter Password")
result = authenticate_user(un, pa)
while True:
    if result:
        time.sleep(0.5)
        print(".................Welcome", result[1], "..............")
        print("Select main menu")
        print("1.Customer Management")
        print("2.Advanced Accounts")
        print("3.Transaction history")
        print("4.Data Analysis And Reporting")
        print("5.Log Out")
        ch = int(input("Enter You Choice"))
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
            ch1 = int(input("Enter your Choice"))
            if ch1 == 1:
                create_ac()
            elif ch1 == 2:
                pass
            elif ch1 == 3:
                an = int(input("Enter Account No.To Deposit Money"))
                amt = int(input("Enter Amt to Deposit"))
                obj = Account(an,
                              amt)  # passed the account number and the amt passed to The class Account constructor
                obj.deposit()
            elif ch1 == 4:
                an = int(input("Enter Account No.To withdraw"))
                amt = int(input("Enter Amt to withdraw"))
                obj = Account(an, amt)
                obj.withdraw()
                pass
            elif ch1 == 5:
                pass
            elif ch1 == 6:
                pass
            elif ch1 == 7:
                pass
            elif ch1 == 8:
                pass
            elif ch1 == 9:
                exit(0)
        elif ch == 2:
            print("Select following operation")
            print("1.Create Fixed Deposit Account")
            print("2.Create Recurring Deposit Account")
            print("3.Grant a Loan")
            ch = int(input("Enter your Choice"))
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
            ch = int(input("Enter Your Choice"))
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
            logging.info("Thank U for using our Bank System")
            exit(0)
    else:
        break
