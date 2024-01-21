
import book
import member
import transaction
import reports
import mysql.connector as sqlt
while (True):
    print("="*160)
    print("\t\t\t--------------WELCOME TO----------------\n\
          \t\t\t--------LIBRARY MANAGEMENT SYSTEM---------\n")
    print("="*160)
    print("\t\t\t\tEnter Your Choice\n\t\t\t\t1.Book Details\n\t\t\t\t2.Member Details\n\t\t\t\t3.Transaction\n\t\t\t\t4.Report\n\t\t\t\t5.Exit")
    choice=int(input())
    if choice==1:
        while(True):
             print("\t\t\t\tEnter Your Choice \n\t\t\t\t1. Add Book Details\n\t\t\t\t2. Edit Book Details\
                \n\t\t\t\t3. Delete A Book\n\t\t\t\t4. Search A Book\n\t\t\t\t5.Back To Main Menu")
             ch = int(input())
             if ch==1:
                book.book_input()
             elif ch==2:
                 book.book_edit()  
             elif ch==3:
                  book.book_delete()
             elif ch==4:
                  book.book_search()
             elif ch==5:
                 break
        
    elif choice==2:
        while(True):
             print("\t\t\t\tEnter Your Choice \n\t\t\t\t1. Add Member Details\n\t\t\t\t2. Edit member details\
                \n\t\t\t\t3. Delete A Member\n\t\t\t\t4. Search A Member\n\t\t\t\t5.Back To Main Menu")
             ch = int(input())
             if ch==1:
                 member.member_input()
             elif ch==2:
                 member.member_edit()
             elif ch==3:
                  member.member_delete()
             elif ch==4:
                  member.member_search()
             elif ch==5:
                break
        
    elif choice==3:
         while(True):
             print("\t\t\t\tEnter Your Choice \n\t\t\t\t1. Issue Book\n\t\t\t\t2. Return Book\n\t\t\t\t3.Back To Main Menu")
             ch = int(input())
             if ch==1:
                 transaction.book_issue()
             elif ch==2:
                 transaction.book_return()
             elif ch==3:
                 break
             
             
        
    elif choice==4:
        while(True):
             print("\t\t\t\tEnter Your Choice \n\t\t\t\t1. Book Details\n\t\t\t\t2. Member Details\n\t\t\t\t3. Issue Details\n\t\t\t\t4. Return Details\n\t\t\t\t5.Best Reading Book (Chart)\n\t\t\t\t6. Back To Main Menu")
             ch = int(input())
             if ch==1:
                 reports.book_output()
             elif ch==2:
                 reports.member_output()
             elif ch==3:
                  reports.issue_output()
             elif ch==4:
                  reports.return_output()
             elif ch==5:
                  reports.col_chart() 
             elif ch==6:
                 break
        
    elif choice==5:
        break














    


  
