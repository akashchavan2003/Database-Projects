import datetime
import sqlite3

con = sqlite3.connect("library.db")
con.close()


def getdate():
    a = datetime.date.today()
    dt = str(a.day) + "/" + str(a.month) + "/" + str(a.year)
    return dt


def add_new_stud():
    sn = input("enter the student name")
    si = input("enter the student id ")
    sm = input("enter the student mobile no.")
    se = input("enter student email id")
    con1 = sqlite3.connect("library.db")
    query = "INSERT INTO student_data (stname, student_id, studentmob, student_email) VALUES('" + sn + "', " + si + ",'" + sm + "', '" + se + "')"
    con1.execute(query)
    con1.commit()
    con1.close()
    print("student added")


def add_new_book():
    bn = input("enter the book name")
    ba = input("enter the book author")
    bnu = input("enter the book number")
    q = "INSERT INTO book_info(book_name,book_author,bookn) VAlUES('" + bn + "','" + ba + "'," + bnu + ")"
    con = sqlite3.connect("library.db")
    con.execute(q)
    con.commit()
    con.close()
    print("book added")


def issue_book():
    bn = input("enter the book name")
    con = sqlite3.connect("library.db")
    cursor = con.cursor()
    cursor.execute("SELECT COUNT(*) FROM book_info WHERE book_name = ?", (bn,))
    result = cursor.fetchone()
    cursor1 = con.cursor()
    query = '''
        SELECT CASE 
            WHEN COUNT(book_iss) = 0 THEN NULL
            ELSE 'True'
        END AS book_iss_exists
        FROM book_his
        WHERE book_iss IS NOT NULL
    '''
    cursor1.execute(query)
    result2 = cursor1.fetchone()
    con.close()
    if result[0] >= 1 and (result2[0] is None or result2[0] == "False"):
        sn = input("enter student name")
        con = sqlite3.connect("library .db")
        cursor = con.cursor()
        cursor.execute("SELECT COUNT(*) FROM student_data WHERE stname = ?", (sn,))
        result = cursor.fetchone()
        con.close()
        if result[0] >= 1:
            print("student is already enrolled")
            print("press 1 to confirm issue book")
            print("press 2 for exit")
            r = input()
            if int(r) == 1:
                date = getdate()
                null = "null"
                true = "True"
                q = "INSERT INTO book_his(student_name,book_name,book_iss_date,book_ret_date,book_iss)VALUES ('{}', " \
                    "'{}', " \
                    "'{}','{}','{}')".format(sn, bn, date, null, true)
                con = sqlite3.connect("library.db")
                con.execute(q)
                con.commit()
                con.close()
                print("book issued successfully to", sn)
            else:
                exit(0)
        else:
            print("please register or enroll student")
            print("press 1 for register ")
            print("press 0 for exit")
            r = input()
            if int(r) == 1:
                add_new_stud()
            else:
                exit(0)
    elif result2[0] == "True":
        print("the book is already issued to student")
    else:
        print("there is no book named as", bn, "please try again!")


def return_book():
    sn = input("enter the student name")
    con = sqlite3.connect("library.db")
    query = f'''
        SELECT 
            CASE 
                WHEN EXISTS (SELECT 1 FROM book_his WHERE student_name = ?) 
                THEN 
                    (SELECT GROUP_CONCAT(book_name, ', ') 
                     FROM book_his 
                     WHERE student_name = ?) 
                ELSE 
                    'False' 
            END AS result
    '''
    cursor = con.execute(query, (sn, sn))
    result = cursor.fetchone()
    con.close()
    count = len(result)
    if result[0] == "false":
        print("No book is issued to this student")
    if result[0] != "false":
        for book in result:
            if count == 1:
                date = getdate()
                false = "False"
                con = sqlite3.connect("library.db")
                cursor = con.cursor()
                query = f'''
                                UPDATE book_his
                                SET book_ret_date = ?, book_iss = ?
                                WHERE student_name = ?
                            '''
                cursor.execute(query, (date, false, sn,))
                con.commit()
                con.close()
                print("Book Returned Successfully..")
            if count > 1:
                date = getdate()
                false = "False"
                bn = input("enter the book name that you want to return")
                con = sqlite3.connect("library.db")
                cursor = con.cursor()
                query = f'''
                    UPDATE book_his
                    SET book_ret_date = ?, book_iss = ?
                    WHERE student_name = ? AND book_name-?
                '''
                cursor.execute(query, (date, false, sn, bn))
                con.commit()
                con.close()
                print("book Returned successfully....")


def not_ret_books():
    count = 1
    con = sqlite3.connect("library.db")
    cursor = con.cursor()
    cursor.execute("SELECT *  FROM book_his WHERE book_iss='False' ")
    res = cursor.fetchall()
    con.close()
    for book in res:
        print(count, "Student name:", book[0], "book name:", book[1])
        count = +1


def book_history():
    bn = input("enter the book name ")
    con = sqlite3.connect("library.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book_his WHERE book_name=?", (bn,))
    res = cur.fetchall()
    con.close()
    for book in res:
        print("Student name:", book[0], ".Book name:", book[1], ".Book Issue DT:", book[2], ".Book Return DT", book[3])


def stud_history():
    sn = input("enter the student name ")
    con = sqlite3.connect("library.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book_his WHERE student_name=?", (sn,))
    res = cur.fetchall()
    con.close()
    for book in res:
        print("Student name:", book[0], ".Book name:", book[1], ".Book Issue DT:", book[2], ".Book Return DT", book[3])


while True:
    print("Select an operation")
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - Not Returned Books")
    print("4 - Book History")
    print("5 - Student History")
    print("6 - Add New Student")
    print("7 - Add New Book")
    print("0 - Exit")
    ch = int(input("Provide your choice : "))

    if ch == 1:
        issue_book()
    elif ch == 2:
        return_book()
    elif ch == 3:
        not_ret_books()
    elif ch == 4:
        book_history()
    elif ch == 5:
        stud_history()
    elif ch == 6:
        add_new_stud()
    elif ch == 7:
        add_new_book()
    else:
        exit(0)
