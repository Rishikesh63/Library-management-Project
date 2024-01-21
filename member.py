import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
con=sqlt.connect(host="localhost",user="root",passwd="Rishi@638963",database="library")
cursor=con.cursor()
def member_input():
    try:
        memberid=int(input("Enter Member Id"))
        membername = input("Enter Member Name")
        mem_add=input("Enter Member Address")
        phone = input("Enter Phone No") 
     
        qry="insert into member values({},'{}','{}','{}');".format(memberid,membername,mem_add,phone)
        cursor.execute(qry)
        con.commit()
        print("Added Successfully.")
    except:
        print("SORRY...THIS MEMBER ID IS ALREADY EXISTING..TRY OTHER MEMBER ID")
   
def member_edit():
    x=int(input("Enter Member Id"))
    qry = "select * from member where memberid={};".format(x)
    cursor.execute(qry)
    r=cursor.fetchone()
    if r:
        y=input("Enter New Address")
        qry = "update member set mem_add = '{}' where memberid = {};".format(y,x)
        cursor.execute(qry)
        con.commit()
        print("Edited Successfully.")
    else :
        print("Wrong Member Id")

def member_delete():
    x= int(input("Enter Member Id"))
    qry="select * from member where memberid = {};".format(x)
    cursor.execute(qry)
    r=cursor.fetchone()
    if r:
         qry="delete from member where memberid={};".format(x)
         cursor.execute(qry)
         con.commit()
         print("Deleted Successfully.")
    else:
        print("Wrong Member Id")

def member_search():
    x=int(input("Enter Member Id"))
    qry="select * from member where memberid = {};".format(x)
    cursor.execute(qry)
    r=cursor.fetchone()
    if r:
        df = pd.read_sql(qry,con)
        print(tabulate(df,headers = 'keys',tablefmt = 'psql',showindex = False))
    else:
        print("Wrong Member Id")














    


  
