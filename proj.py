import os
import pickle
import time
import datetime
import mysql.connector

width = "150"
height = "50"
os.system("mode con cols="+width+
          " lines="+height)

j=["L",
   "I",
   "B",
   "R",
   "A",
   "R",
   "Y",
   " "]
for c in range(0,8):
    print (" "*5, j[c],)
    time.sleep(0.15)

print ("*"*35,)
print("\n")

time.sleep(0.1)

#Programming Project Starts Here

class lib:
    def __init__(self):
        self.act=0
        self.bname=" "
        self.code=0 
        
    def intro(self):
        print ("Following operations can be performed:")
        print ("\n","1. List of Students")
        print ("","2. List of Available Books")
        print ("","3. Issue a Book")
        print ("","4. Return a Book")
        print ("","5. List of Issued Books")
        print ("","6. Book Statistics (count of books)")
        print ("","7. Add a new book to the Library")
        print ("","Press Enter to Exit...")

    '''def add(self):
                    self.bname=input("Enter book Name: ")
                    self.code=input("Enter Code of book:")
    def register(self):
                   self.name=input("Name of borrower:")
                   self.bookname=raw_input("Enter the name of Book:")
                   self.code=input("Enter the book code:")
                   self.date=time.time()
    def stat(self):
                   print ("Bookname","\t","Code","\n", self.bookname,"\t"*2,)
                   print (self.code)
                   #print "Book status changed To:UnAvailable...."
                   
    def outdel(self):
                   print ("Name","\t","Bookname","\t","Code","\t")
                   #print self.name,"\t"*2 , self.bookname,"\t"*2,self.code,"\t"#,self.date
    def show(self):
                   print ("Bookname","\t","Code")
                   print (self.bname,"\t",self.code)
    def bshow(self):
                   print ("Name","\t","Bookname","\t","Code")
                   print (self.name,self.bookname,self.code) ##self.date()
    def delrec(self,n):
                   if self.name==n:
                       self.outdel()
                       return 1
                   else:
                       return 0
    def outdelstat(self):
                   print ("Book Status:Available Again") ,self.code
    def delstat(self,n):
                  if self.code==n:
                      return 1
                  else:
                      m=self.code
                      self.outdelstat()
                      return 0'''

##########DB connection

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pro_library"
)
print("You are successfully connected to the system")
print("")

#############

x=lib()
x.intro()

while True:
               print("\n")
               act=input("Your choice:")

               
               
               if act=="1":
                   print("Here is the List of All Students")
                   sql="select * from tbl_students"
                   try:
                       cur.execute(sql)
                       print()
                       print("STUDENT ID:    STUDENT NAME:         CLASS:    SECTION:")
                       print("********************************************************")
                       for b in cur:
                           print(b[0],"          ",
                                 b[1],"    ",
                                 b[2],"      ",
                                 b[3]," ")
                           print("---------------------------------------------------------")
                   finally:
                        db_connection.close()

               elif act=="3":
                   print("Here is the List of All Available books")
                   sql="select * from tbl_books"
                   print()
                   
                   try:
                       cur = db_connection.cursor()
                       sql = "INSERT INTO tbl_issued_books (Book_Id, Student_Id, Issue_Date, Due_Date, ) VALUES (%s, %s, %s, %s)"
                       s_id = input("Student ID:")
                       book_id = input("Enter the Book ID:")
                       s_id = input("Student ID:")
                       s_id = input("Student ID:")
                       val = (s_id, book_id)
                       cur.execute(sql, val)

                       """cur.execute(sql)
                       print("Book Name:    Author:    Publisher:    Edition:")
                       for b in cur:
                           print(b[1]," ",
                                 b[2]," ",
                                 b[3]," ",
                                 b[4]," ")
                       s_id=input("Student ID:")
                       book_id=input("Enter the Book ID:")
                       ts = time.time()
                       timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                       due_date=time.time()
                       #sql1="INSERT INTO `tbl_issued_books` (`Book_Id`, `Student_Id`, `Issue_Date`, `Due_Date`) VALUES (book_id, s_id, CURRENT_TIMESTAMP, '0000-00-00 00:00:00.000000')"
                       cur=db_connection.cursor()
                       cur.execute("INSERT INTO `tbl_issued_books` (`Book_Id`, `Student_Id`, `Issue_Date`, `Due_Date`) VALUES (%s,?,%s,%s,%s)", (s_id, book_id, timestamp, due_date))
                       db_connection.commit()
                       print("done")"""
                   finally:
                        db_connection.close()

                   
               elif act=="2":
                   print("Here is the List of All Available books")
                   sql="select * from tbl_books"
                   try:
                       #cur=db_connection.cursor()
                       cur.execute(sql)
                       print("Book Name:    Author:    Publisher:    Edition:")
                       print("********************************************************")
                       for b in cur:
                           print(b[1]," ",
                                 b[2]," ",
                                 b[3]," ",
                                 b[4]," ")
                   finally:
                        db_connection.close()

                    
                              
               elif act=="4":
                   ##########Return()
                   ##Delete function
                   bl=open("borrowlist.dat","rb")
                   temp=open("temp","wb")
                   n=raw_input("enter the name for Returning:")
                   
                   try:
                       while True:
                            x=pickle.load(bl)
                            m=x.code
                            if x.delrec(n)==0:
                                pickle.dump(x,temp)
                                
                            else:
                                k=m
                                #pass
                   except EOFError:
                       
                       print ("k...")
                       print ("::"*90)
                   bl.close()
                   temp.close()
                   os.remove("borrowlist.dat")
                   os.rename("temp","borrowlist.dat")

                   #Function to remove book
                
                   bs=open("bookstat.dat","rb")
                   temp=open("temp","wb")
                   #m=x.code
                   try:
                       while True:
                            x=pickle.load(bs)
                            if x.delstat(k)==0:
                                pickle.dump(x,temp)
                   except EOFError:
                       print ("Removed if in the database Else ignored .....")
                       print ("::"*90)
                   bs.close()
                   temp.close()
                   os.remove("bookstat.dat")
                   os.rename("temp","bookstat.dat")
                   
                   
               elif act=="5":
                              #borrowlist()3
                              bop=open("borrowlist.dat","rb")
                              try:
                                             while True:
                                                            x=pickle.load(bop)
                                                            x.bshow()
                              except EOFError:
                                             print ("Thats all for now...")
                                             print ("::"*90)
                                             bop.close()

                              
                              
               elif act=="6": 
                              #x.bookstat()
                              bstat=open("bookstat.dat","rb")
                              try:
                                             while True:
                                                            x=pickle.load(bstat)
                                                            x.stat()
                              except EOFError:
                                             print ("Thats all for now...")
                                             print ("::"*90)
                                             bstat.close()

                                                 
               elif act=="7":
                              #adding Books
                              
                              x=lib()
                              wpf=open("list.dat","ab")
                              while True:
                                             x.add()
                                             pickle.dump(x,wpf)
                                             ans=input("any more (y/n)?")
                                             if ans!="y":
                                                            wpf.close()
                                                            break
                                             


               else:
                              """
                                print ("\n"*50)
                              k=[" "*10,"T","h","a","n","k","s"," "," "*20,"for "," "*20," ","C ","o","m","i","n","g"]
                              for c in range(0,18):
                                  print (k[c],)
                                  time.sleep(0.1)    
                              print """
                              print("\t"*3,"Thanks for coming")
                              """
                                k=[u"\u00a9","r","e","s","e","r","v","e","d",]
                              for c in range(0,9):
                                  print (k[c],)
                                  time.sleep(0.1)
                              print
                              """
                              k=["c","o","d","e"," "*20,"by"," "*20,"JYOTI DIXIT","and","TEAM"]
                              for c in range(0,10):
                                  print (k[c],)
                                  time.sleep(0.1)
                              break

