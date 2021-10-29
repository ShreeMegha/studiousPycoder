#***********Dr. NALLI KUPPUSWAMI VIVEKANANDA VIDYALAYA JUNIOR COLLEGE *************”
#******************VIDYALAYA MANAGER *****************************" 
#*******Designed and Maintained By:" 
#*******S. Aishwarya - CLASS XII A - ROLL NO - 23 [ 2020-2021 ]" 
#*******K. Chandheni - CLASS XII A - ROLL NO - 24 [ 2020-2021 ]" 
#*******G. Megha Shree - CLASS XII A - ROLL NO - 26 [ 2020-2021 ]" 

import mysql.connector as sqlcnt

# GLOBAL VARIABLES DECLARATION 

myConnnection = " "
cursor= " "
username= " "
password = " "

#MODULE TO CHECK MYSQL CONNECTIVITY 

def mysqlconnectionCheck():
    global myConnection 
    global userName 
    global password

    userName = input("\n ENTER MYSQL SERVER'S USERNAME : ") 
    password = input("\n ENTER MYSQL SERVER'S PASSWORD : ")

    myConnection = sqlcnt.connect(host="localhost",user=userName,password=password,database="Project")
    if myConnection:
        print("\n CONGRATS! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED")
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD !")    




#1MODULE FOR CREATING STUDENT TABLE
def tablecreate():
    if myConnection:
        cursor=myConnection.cursor()
        CreateTable = ("CREATE TABLE STUDENT(ROLL_NO INT, STUDENT_NAME VARCHAR(30),ADMISSION_NO INT PRIMARY KEY, FATHER_NAME VARCHAR(30),MOTHER_NAME VARCHAR(30),PHONE_NO VARCHAR(12), ADDRESS VARCHAR(100),STUDENT_CLASS INT,STUDENT_SECTION CHAR(3),BLOODGROUP CHAR(4),DATEOFBIRTH varchar(15))")
        cursor.execute(CreateTable)
        myConnection.commit()
        cursor.close()
        print("\n CREATED TABLE SUCCESSFULLY!!")


#2MODULE TO ENROLL STUDENT VALUES
def studentvalues():
    if myConnection:
        cursor=myConnection.cursor()
        while True:
            rollno=int(input("ENTER ROLL_NO : "))
            sname=input("ENTER STUDENT'S NAME : ")
            admissionno=int(input("ENTER ADMISSION_NO : "))
            fname=input(" ENTER FATHER'S NAME : ")
            mname=input(" ENTER MOTHER'S NAME : ")
            phone=input(" ENTER CONTACT NO. : ")
            address=input(" ENTER ADDRESS : ")
            sclass =int(input(" ENTER CLASS : "))
            ssection=input(" ENTER SECTION : ")
            bloodgroup=input("ENTER BLOOD GROUP : ")
            dob=(input("ENTER DATE OF BIRTH(YYYY-MM-DD) : "))

            insert = ("INSERT INTO STUDENT(ROLL_NO, STUDENT_NAME ,ADMISSION_NO, FATHER_NAME ,MOTHER_NAME ,PHONE_NO, ADDRESS, STUDENT_CLASS ,STUDENT_SECTION, BLOODGROUP, DATEOFBIRTH)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            values = (rollno,sname,admissionno,fname,mname,phone,address,sclass,ssection,bloodgroup,dob)
            cursor.execute(insert,values)
            cursor.execute("commit")
            ch = input("DO YOU WANT TO CONTINUE (Y/N):")
            if ch == 'n' or ch == 'N':
                break
            
        cursor.close()
        print("\n STUDENT VALUES ENROLLED SUCCESSFULLY !")
    else:
        print("\n ERROR ESTABLISHING MYSQL CONNECTION !")



#3MODULE TO DISPLAY STUDENT'S DATA
def displaystudent():
    if myConnection:
        cursor=myConnection.cursor()
        cursor.execute("SELECT * FROM STUDENT")
        data = cursor.fetchall()
        count = cursor.rowcount
        print("Total No.of rows in resultset:",count)
        for row in data:
            print(row)
        cursor.close()
    else:
        print("\n ERROR! TRY AGAIN")




#4MODULE TO ALTER STUDENT DATA
def alterstudent():
    if myConnection:
        cursor = myConnection.cursor()
        cursor.execute("ALTER TABLE STUDENT ADD CITY char(20)")
        myConnection.commit()
        
        


#5MODULE TO DISPLAY FIELD STRUCTURE
def fieldstructure():
    if myConnection:
        cursor = myConnection.cursor()
        try:
            table = input("Enter Table Name:")
            cursor.execute("DESC %s"%table)
            for i in cursor:
                print(i)
        except:
            print("SORRY !! ERROR OCCURED!! TRY AGAIN!!")

#6UPDATING THE STUDENTS CITY
def updatestudent():
    if myConnection:
        cursor = myConnection.cursor()
        try:
            rollno = int(input("ENTER ROLL NUMBER OF STUDENT WHOSE CITY TO BE UPDATED:"))
            qry = "SELECT * FROM STUDENT WHERE ROLL_NO = %s"%rollno
            cursor.execute(qry)
            data=cursor.fetchall()

            if len(data)!=0:
                city =input("Enter Updated city:")
                query = "UPDATE STUDENT SET CITY = %s WHERE ROLL_NO = %s"
                values = (city,rollno)
                cursor.execute(query,values)
                for i in cursor:
                    print("STUDENT RECORD UPDATED SUCCESSFULLY")
                    print(i)
                myConnection.commit()
                q1 = "SELECT * FROM STUDENT WHERE ROLL_NO =%s"%rollno
                cursor.execute(q1)
                for i in cursor:
                    print(i)
                       
            else:
                print("STUDENT RECORD NOT FOUND")
            
        except:
            print("SORRY !! ERROR OCCURED!! TRY AGAIN!!")

        
        



#7MODULE TO SEARCH VALUES OF STUDENT
def searchvalues():
    if myConnection:
        cursor = myConnection.cursor()
        print("ENTER:1 TO SEARCH BY ROLL_NO")
        print("ENTER:2 TO SEARCH BY NAME")
        choice = int (input("ENTER YOUR CHOICE:"))
       #searching by student roll no
        if choice==1:
            try:
                rollno = int(input("ENTER ROLL NUMBER OF STUDENT TO SEARCH:"))
                qry = "SELECT * FROM STUDENT WHERE ROLL_NO = %s"%rollno
                cursor.execute(qry)
                data=cursor.fetchall()
                if len(data)!=0:
                    print(data)
            except:
                print("ERROR!!, TRY AGAIN")
           
        #searching by student name
        if choice==2:
            try:
                name=input("ENTER STUDENT NAME TO SEARCH :")
                sql = "SELECT * FROM STUDENT WHERE STUDENT_NAME = '%s'"%name
                cursor.execute(sql)
                data=cursor.fetchall()
                if len(data)==0:
                    print("STUDENT NOT FOUND")
                else:
                    print(data)
            except:
                print("ERROR!!, TRY AGAIN")
    


#8MODULE TO ADD STUDENTS MARK DETAILS
def addmark():
    if myConnection:
        cursor = myConnection.cursor()
        cursor.execute("ALTER TABLE STUDENT ADD HALF_YEARLY_MARK int")
        cursor.execute("ALTER TABLE STUDENT ADD ANNUAL_MARK int")
        myConnection.commit()
        while True:
            rollno = int(input("ENTER STUDENT ROLLNO TO ADD MARKS:"))
            hf_mark = int(input("ENTER HALF YEARLY MARK:"))
            anl_mark = int(input("ENTER ANNUAL MARK:"))
            qry = "UPDATE STUDENT SET HALF_YEARLY_MARK =%s, ANNUAL_MARK =%s WHERE ROLL_NO =%s"
            values = (hf_mark,anl_mark,rollno)
            cursor.execute(qry,values)
            myConnection.commit()
            ch = input("DO YOU WANT TO CONTINUE(Y/N):")
            if ch=="N" or ch=="n":
                break
            
        for i in cursor:
            print(i)
        print("MARKS ADDED")
    else:
        print("ERROR !! TRY AGAIN..!")


#9MODULE TO DELETE COLUMN CITY
def deletecity():
    if myConnection:
        cursor = myConnection.cursor()
        cursor.execute("ALTER TABLE STUDENT DROP COLUMN CITY")
        myConnection.commit()
        print("DELETED COLUMN CITY")
    else:
        print("ERROR")

        
    
#10MODULE TO UPGRADE STUDENTS MARK
def markupgrade():
    if myConnection:
        cursor = myConnection.cursor()
        cursor.execute("UPDATE STUDENT SET ANNUAL_MARK = ANNUAL_MARK + 5")
        myConnection.commit()
        print("ANNUAL MARK UPDATED TO ALL")
    else:
        print("ERROR")
        
    


#0MODULE TO PROVIDE HELP FOR USER
def helpme():
    print(" FOR MORE DETAILS PLEASE VISIT THE OFFICIAL WEBSITE : drnkvv.org ")
    

    



#MAIN SCREEN
print("#########################################################################################################################")

print("\n |                                      2020-2021                                             |")
print("\n |                                       WELCOME                                              |")
print("\n |       DR. NALLI KUPPUSWAMI VIVEKANANDA VIDYALAYA SENIOR SECONDARY SCHOOL, KORATTUR         |")
print("\n |************************************ VIDYALAYA MANAGER *************************************|")
print("\n |                                DESIGNED AND MAINTAINED BY:                                 |")
print("\n |                  S. Aishwarya - CLASS XII A - ROLL NO - 12123 [ 2020-2021 ]                |")
print("\n |                  K. Chandheni - CLASS XII A - ROLL NO - 12124 [ 2020-2021 ]                |")
print("\n |                 G. Megha Shree - CLASS XII A - ROLL NO - 12126 [ 2020-2021 ]               |")

print("\n |--------------------------------------------------------------------------------------------|")
print("\n |                                   VIDYALAYA MANAGER                                        |")
print("\n |--------------------------------------------------------------------------------------------|")

print("#########################################################################################################################")


#PROGRAM STARTS

myConnection = mysqlconnectionCheck()
if myConnection:
    while(1):

        print("|----------------------------------------------------------------------------------------------------|")
        print("|        ENTER 1 : CREATE NEW STUDENT TABLE                                                          |")
        print("|        ENTER 2 : ENROLL STUDENT VALUES                                                             |")
        print("|        ENTER 3 : DISPLAY STUDENT's DATA                                                            |")
        print("|        ENTER 4 : ALTER STUDENT's DATA                                                              |")
        print("|        ENTER 5 : FIELD STRUCTURE                                                                   |")
        print("|        ENTER 6 : UPDATE STUDENT's DATA                                                             |")
        print("|        ENTER 7 : STUDENT VALUE SEARCH                                                              |")
        print("|        ENTER 8 : ADD STUDENTS MARK DETAILS                                                         |")
        print("|        ENTER 9 : DELETE COLUMN CITY                                                                |")
        print("|        ENTER 10: UPGRADE STUDENT MARKS                                                            |")
        print("|        ENTER 11: EXIT                                                                              |")
        print("|----------------------------------------------------------------------------------------------------|")
        print("|        ENTER 0 : HELP                                                                              |")
        print("|----------------------------------------------------------------------------------------------------|")

        choice = int(input(" ENTER YOUR CHOICE : "))
        if choice==1:
            tablecreate()
        elif choice==2:
            studentvalues()
        elif choice==3:
            displaystudent()
        elif choice==4:
            alterstudent()
        elif choice==5:
            fieldstructure()
        elif choice==6:
            updatestudent()
        elif choice==7:
            searchvalues()
        elif choice==8:
            addmark()
        elif choice==9:
            deletecity()
        elif choice==10:
            markupgrade()
        elif choice==11:
            myConnection.close()
            break
        elif choice==0:
            helpme()
        else:
            print("SORRY, MAY BE WRONG INPUT!, TRY AGAIN!!!!")
    else:
        print("\n CHECK YOUR MYSQL CONNECTION!!!")



#PROJECT ENDS        
         


        
        
    
    




    
