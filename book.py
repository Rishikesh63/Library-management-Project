import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
con=sqlt.connect(host="localhost",user="root",passwd="Rishi@638963",database="library")
cursor=con.cursor()
def book_input():
    try:
        bookid=input("Enter Book Id")
        bname=input("Enter Book Name")
        author=input("Enter Author Name")
        price=float(input("Enter price"))
        copies=int(input("Enter No of copies"))
        qry="insert into book values({},'{}','{}',{},{},{});".format(bookid,bname,author,price,copies,copies)
        cursor.execute(qry)
        con.commit()
        print("added successfully..")
    except:
        print("SORRY...THIS BOOK ID IS ALREADY EXISTING.TRY WITH OTHER BOOK ID")
def book_edit():
    x=int(input("Enter Book ID"))
    qry="select * from book where bookid={};".format(x)
    cursor.execute(qry)
    r=cursor.fetchone()
    if r:
        y=float(input("Enter new price"))
        qry="update book set price={} where bookid = {};".format(y,x)
        cursor.execute(qry)
        con.commit()
        print("Edited Successfully.")
    else:
        print("Wrong Book Id")

def book_delete():
    x=int(input("enter book id"))
    qry="select * from book where bookid={};".format(x)
    cursor.execute(qry)
    r=cursor.fetchone()
    if r:
         qry="delete from book where bookid={};".format(x)
         cursor.execute(qry)
         con.commit()
         print("delete successfuly.")
    else:
        print("wrong book id")

def book_search():
    x=int(input("enter book id"))
    qry="select * from book where bookid={};".format(x)
    cursor.execute(qry)
    r=cursor.fetchone()
    if r:
        df = pd.read_sql(qry,con)
        print(tabulate(df,headers = 'keys',tablefmt = 'psql',showindex = False))
    else:
         print("wrong book id")















    


  
