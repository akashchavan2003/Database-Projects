import sqlite3
import bcrypt
import sys
import hashlib


def hash_password(password):
    # Hash the password using a strong hashing algorithm (e.g., SHA-256)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


def check_password(input_password, stored_hashed_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), stored_hashed_password)


def login():
    con = sqlite3.connect("bank_manage.db")
    con.close()
    print("Please Login First")
    un = input("enter username")
    pa = input("Enter password")
    con = sqlite3.connect("bank_manage.db")
    cur = con.cursor()
    q = "SELECT * FROM master_table WHERE username=? AND password=?"
    data = (un, pa)
    cur.execute(q, data)
    result = cur.fetchone()
    con.close()
    return result


def create_user(username, password, bn):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    connection = sqlite3.connect('bank_manage.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username, hashed_password,bank_name) VALUES (?, ?,?)",
                   (username, hashed_password, bn))
    connection.commit()
    connection.close()


result = login()
if result:
    print("                  SUCCESSFULLY LOGINED......                   ")
    print("Select your choice")
    print("1. Add New Bank or Register")
    print("2. Change password of Customer Bank Ac")
    print("3. Deregister Bank Ac")
    print("4. Log Out")
    ch = int(input("Enter"))  # Convert input to an integer

    if ch == 1:
        print("Enter details")
        bn = input("Enter bank Name")
        un = input("Enter A New Username ")
        pa = input("Enter A New Password")
        create_user(un, pa, bn)
        print("NEW BANK ADDED")
    elif ch == 2:
        print("Enter The Bank ID")
        bi = input()
        un = input("enter User name")
        con = sqlite3.connect("bank_manage.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE user_id=?", (bi,))
        result = cur.fetchone()
        print(result)
        con.close()
        if result[1] == un and result[0] == int(bi):
            print("Your Bank Name is", result[3])
            pp = input("Enter your Previous Password")
            result2 = check_password(pp, result[2])
            if result2:
                print("Previous Password Is Authenticated")
                np = input("Now Please Enter Your New Password")
                hp = hash_password(np)
                con = sqlite3.connect("bank_manage.db")
                con.execute("UPDATE users SET hashed_password= ? WHERE user_id=?", (hp, bi))
                con.commit()
                con.close()
                print("........SUCCESSFULLY PASSWORD IS UPDATED....... ")
            else:
                print("Previous Password does not Match Please Try Again.....")
        else:
            print("Please Enter a Valid ID and Username.....")
    elif ch == 3:
        pass
    elif ch == 4:
        sys.exit(0)

else:
    print("Wrong Username And Password Please Try Again!...")
