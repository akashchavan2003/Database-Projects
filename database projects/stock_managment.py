import sqlite3
import datetime

con = sqlite3.connect("stock.db")
con.close()


def present(char):
    # this function checks how many time the formal parameter are in the database then it returns if they one or more
    # this function for only the presence of a product or not
    con = sqlite3.connect("stock.db")
    cur = con.cursor()
    query = "SELECT COUNT(*) FROM stock_info WHERE productn = ?"
    cur.execute(query, (char,))
    count = cur.fetchone()[0]  # Fetch the count value
    con.close()

    if count > 0:
        return True
    else:
        return False


def one_check(product_name, pq):
    # this function returns the information of that you send parameter and also it less the quantity by the formal
    # parameter  that you send but. we did not check here is it here or no we check them by our original
    # that they call if it presents then they call us
    con = sqlite3.connect("stock.db")
    cur = con.cursor()
    query = "SELECT promrp, prodrate, productqty FROM stock_info WHERE productn = ?"
    cur.execute(query, (product_name,))
    result = cur.fetchone()
    updated_qty = int(result[2]) - int(pq)
    update_query = "UPDATE stock_info SET productqty = ? WHERE productn = ?"
    cur.execute(update_query, (updated_qty, product_name))
    con.commit()
    # here result includes three values like (mrp,rate qty) in tuple
    con.close()
    return result


def get_current_date():
    current_date = datetime.datetime.now().date()
    return current_date


def prepare_bill():
    ls = []
    key_names = []
    bill = +1
    tot = 0
    pro = 0
    cn = input("enter the customer name")
    cc = input("enter the mobile no.")
    returned_status = "False"
    while True:
        pn = input("enter the product name(enter 0 for exit)")
        if pn == "0":  # here we check the input is o or not if 0 means the customer has added all the products so we
            # now we can make a bill
            # there we stored a product name and qty as a dict in a list names ls
            for dictionary in ls:
                for key, value in dictionary.items():
                    res = one_check(key, value)
                    tot += float(res[0]) * float(value)
                    temp = float(res[0]) - float(res[1])
                    pro += temp * float(value)
            pdate = get_current_date()
            print("bill created....")
            print("your total bill AMT is:", tot)
            print()
            # now we have all data of this customer so we insert this data into a table named as billing info
            q = "INSERT INTO billing_info (billno, customern, total, profit, pdate, returned, customerno) " \
                "VALUES ({}, '{}', {}, {}, '{}', {}, '{}')".format(
                0, cn, tot, pro, pdate, returned_status, cc)
            con2 = sqlite3.connect("stock.db")
            con2.execute(q)
            con2.commit()
            con2.close()
            break
        else:
            check = present(pn)
            if check:
                pq = input("enter the quantity of product")
                ls.append({pn: pq})
            else:
                print("there is no product in our stock names", pn)


def print_curr_stock():
    con = sqlite3.connect("stock.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM stock_info;")
    rows = cur.fetchall()
    for t in rows:
        print("product name is:", t[0])
        print("available stock is", t[1])


def add_new_prod():
    pn = input("enter the product name ")
    con1 = sqlite3.connect("stock.db")
    cursor = con1.cursor()
    cursor.execute("SELECT * FROM stock_info")
    row = cursor.fetchall()
    con1.close()
    for one in row:
        if one[0] == pn:
            print("this product is already added")
            pqty = int(input("enter thq quantity"))
            con = sqlite3.connect("stock.db")
            con.execute("UPDATE stock_info SET productqty=productqty + ? WHERE productn = ?", (pqty, pn))
            con.commit()
            con.close()
            print("quantity added to the product")
            break
    else:
        pm = input("enter the manufacturer or company name")
        pq1 = int(input("enter the qty you received"))
        pd = input("enter the distributor name")
        bn = input("enter the product batch no")
        pex = input("enter the product expiry date(DT/MON/YEAR)")
        pmrp = input("enter the product mrp (per piece)")
        prat = input("enter the rate(per piece)")
        q = "INSERT INTO stock_info(productn, productqty, batchno, productm, EXPIRY, distn,promrp,prodrate) VALUES('" + pn + "', " + str(
            pq1) + ", '" + bn + "', '" + pm + "', '" + pex + "', '" + pd + "', '" + pmrp + "','" + prat + "')"
        con = sqlite3.connect("stock.db")
        con.execute(q)
        con.commit()
        con.close()
        print("stock added...")


def view_today_sale(date):
    sale = 0
    profit = 0
    con = sqlite3.connect("stock.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM billing_info WHERE pdate = ?", (date,))
    rows = cur.fetchall()
    for row in rows:
        print("customer name is", row[1])
        print("total bill is.", row[2])
        sale += float(row[2])
        profit += float(row[3])
    print("total sale of", date, "is:", sale)
    print("total profit of", date, "is:", profit)


def print_all_prod():
    con = sqlite3.connect("stock.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM stock_info;")
    rows = cur.fetchall()
    for t in rows:
        print("Product name:", t[0])
        print("Qty:", t[1])
        print("Batch NO:", t[2])
        print("Expiry:", t[4])
        print("Distributor:", t[5])
        print("MRP:", t[6])
        print("------------------")


while True:
    print("Select operation")
    print("1 - Prepare Bill")
    print("2 - Print Current Stock")
    print("3 - Add New Product")
    print("4 - View Today's Sale")
    print("5 - Print All Products")
    print("6 - Exit")
    ch = int(input("Provide your choice : "))

    if ch == 1:
        prepare_bill()
    elif ch == 2:
        print_curr_stock()
    elif ch == 3:
        add_new_prod()
    elif ch == 4:
        dt = input("Enter the date as follows(year-month-date)")
        view_today_sale(dt)
    elif ch == 5:
        print_all_prod()
    elif ch == 6:
        exit(0)
