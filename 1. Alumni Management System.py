import mysql.connector
import pandas as pd
constr=mysql.connector.connect(host="localhost",\
user="root",\
passwd="")
print(constr)
mycursor=constr.cursor()

def create_database():

     mycursor.execute("create database if not exists aldb")
     mycursor.execute("use aldb")
     
     print(" Creating alureg table")
     sql = "CREATE TABLE if not exists alureg (\
          alu_id varchar(10),\
          fname varchar(30) ,\
          lname varchar(30) ,\
          dob date ,\
          gender varchar(10) ,\
          add_corr varchar(30) ,\
          add_offc varchar(30) ,\
          email_add varchar(30) ,\
          mob_no varchar(14) ,\
          curr_city varchar(30) ,\
          curr_company varchar(30) ,\
          desg varchar(20) ,\
          session_from year(4) ,\
          session_to year(4) ,\
          branch varchar(30));"
     mycursor.execute(sql)
     print(" Alureg table created")
     
     print(" Creating EVENT table")
     sql = "CREATE TABLE if not exists event (\
          event_name varchar(30),\
          event_date DATE ,\
          venue varchar(30), \
          status varchar(30));"
     mycursor.execute(sql)
     print(" EVENT table created")

def RegisterAlumni():
     mycursor.execute("use aldb")
     L=[]
     fname=input("Enter Your First Name : ")
     L.append(fname)
     lname=input("Enter Your Last Name :")
     L.append(lname)
     dob=input("Enter Dob in YYYY-MM-DD Format : ")
     L.append(dob)
     gender=input("Enter Your Gender : ")
     L.append(gender)
     add_c=input("Enter your correspondence address : ")
     L.append(add_c)
     add_of=input("Enter your official address : ")
     L.append(add_of)
     email=input("Enter your email address Ex: aa@gmail.com: ")
     L.append(email)
     mob=input("Enter Your Mobile No: ")
     L.append(mob)
     cur_c=input("Enter City Name You Stay : ")
     L.append(cur_c)
     com=input("Enter Company/Organization You are Working : ")
     L.append(com)
     desg=input("Enter Your Desgination in Company/Organization : ")
     L.append(desg)
     start_y=input("Enter Your Session Start Year in College: ")
     L.append(start_y)
     start_e=input("Enter Your Session End Year in College : ")
     L.append(start_e)
     branch=input("Enter Your Branch in College : ")
     L.append(branch)
     alid="al"+fname[0:2]+lname[0:2]+mob[0:4]
     L.insert(0,alid)
     alumni=(L)
     sql="insert into alureg (alu_id,fname,lname,dob,gender,add_corr,add_offc,email_add,mob_no,curr_city,curr_company,desg,session_from,session_to,branch) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
     mycursor.execute(sql,alumni)
     constr.commit()
     print("You Have Been Succesfully Registered: This is You AlumniID ,Use This For Further Correspondence")
     print(alid)
def ViewAlumniDetails():
     mycursor.execute("use aldb")
     print("Select the search criteria to View Details : ")
     print("1. Fname")
     print("2. Lname")
     print("3. Company")
     print("4. Stream")
     print("5. City")
     print("6. Session Start")
     print("7. To View All Records")
     ch=int(input("Enter the choice : "))
     if ch==1 :
          s=input("Enter First Name to Be Searched For")
          rl=(s,)
          sql="select * from alureg where first_name like %s"
          mycursor.execute(sql,rl)
     elif ch==2:
          s=input("Enter Last Name to Be Searched For")
          rl=(s,)
          sql="select * from alureg where last_name like %s"
          mycursor.execute(sql,rl)
     elif ch==3:
          s=input("Enter Company Name to Be Searched For")
          rl=(s,)
          sql="select * from alureg where curr_company=%s"
          mycursor.execute(sql,rl)
     elif ch==4:
          s=input("Enter Stream : ")
          rl=(s,)
          sql="select * from alureg where branch=%s"
          mycursor.execute(sql,rl)
     elif ch==5:
          s=input("Enter City : ")
          rl=(s,)
          sql="select * from alureg where curr_city=%s"
          mycursor.execute(sql,rl)
     elif ch==6:
          s=input("Enter Session Start Year ")
          rl=(s,)
          sql="select * from alureg where session_from=%s"
          mycursor.execute(sql,rl)
     elif ch==7:
          sql="select * from alureg"
          mycursor.execute(sql)
          res=mycursor.fetchall()
          print("The Alumni Details are as Follows")
          print("(alu_id,first_name,last_name,dob,gender,add_corr,add_offc,email_add,mob_no,curr_city,curr_company,desg,session_from,session_to,branch)")
     for x in res:
          print(x)
def EditAlumni():
     mycursor.execute("use aldb")
     alid=input("Enter Alumni ID to be edited : ")
     sql="select * from alureg where alu_id=%s"
     ed=(alid,)
     mycursor.execute(sql,ed)
     res=mycursor.fetchall()
     for x in res:
          print(x)
     print("")
     print("Fields can be updated.....")
     print("1. alu_id")
     print("2. fname")
     print("3. lname")
     print("4. dob ")
     print("5. gender")
     print("6. add_corr")
     print("7. add_offc")
     print("8. email_add")
     print("9. mob_no")
     print("10.curr_city")
     print("11.curr_company")
     print("12.desg")
     print("13.session_from")
     print("14.session_to")
     print("15.branch")
     fld=input("Enter the field which you want to edit : ")
     val=input("Enter the value you want to set : ")
     sql="Update alureg set " + fld +"='" + val + "' where alu_id='" + alid + "'"
     sq=sql
     mycursor.execute(sql)
     print("Editing Done : ")
     print("After correction the record is : ")
     sql="select * from alureg where alu_id=%s"
     ed=(alid,)
     mycursor.execute(sql,ed)
     res=mycursor.fetchall()
     for x in res:
          print(x)
     constr.commit()

def SearchAlumni():
     mycursor.execute("use aldb")
     print("Enter The Alumni ID")
     aluid=input("Enter the Alumni ID for the alumni to be viewed : ")
     sql="select * from alureg where alu_id=%s"
     rl=(aluid,)
     mycursor.execute(sql,rl)
     res=mycursor.fetchall()
     if res==None:
          print("Record not Found . . . ")
          return
     print("The details of the students are : " )
     print("(alu_id,fname,lname,dob,gender,add_corr,add_offc,email_add,mob_no,curr_city,curr_company,desg,session_from,session_to,branch)")
     for x in res:
          print(x)

def DeleteAlumni():
     mycursor.execute("use aldb")
     aluid=input("Enter the Alumni ID for the alumni to be deleted : ")
     sql="Delete from alureg where alu_id=%s"
     rl=(aluid,)
     mycursor.execute(sql,rl)
     constr.commit()

def ScheduleEvent():
     mycursor.execute("use aldb")
     E=[]
     ename=input("Enter Event Name to Schedule : ")
     E.append(ename)
     edate=input("Enter Event Date in YYYY-MM-DD :")
     E.append(edate)
     evenue=input("Enter Venue of Event :")
     E.append(evenue)
     estat=input("Enter Event Status as Completed Or Not Completed :")
     E.append(estat)
     event=(E)
     sql="insert into event (event_name,event_date,venue,status) values (%s,%s,%s,%s)"
     mycursor.execute(sql,event)
     constr.commit()
     print("You Have Succesfully Added A Event")

def ViewEventDetails():
     mycursor.execute("use aldb")
     print("Select the search criteria to View Event Details : ")
     print("1. Event Name")
     print("2. Venue")
     print("3. Status")
     print("4. To View All Records")
     ch=int(input("Enter the choice : "))
     if ch==1 :
          s=input("Enter Event Name to Be Searched For")
          rl=(s,)
          sql="select * from event where event_name like %s"
          mycursor.execute(sql,rl)
     elif ch==2:
          s=input("Enter Venue Name to Be Searched For")
          rl=(s,)
          sql="select * from event where event like %s"
          mycursor.execute(sql,rl)
     elif ch==3:
          s=input("Enter Status to Be Searched For")
          rl=(s,)
          sql="select * from event where status=%s"
          mycursor.execute(sql,rl)
     elif ch==4:
          sql="select * from event"
          mycursor.execute(sql)
     res=mycursor.fetchall()
     print("The Event Details are as Follows")
     print("(Event_Name,Event_Date,Venue,Status)")
     for x in res:
          print(x)

def DeleteEvent():
     mycursor.execute("use aldb")
     ename=input("Enter the Event Name to be deleted : ")
     sql="Delete from event where event_name=%s"
     rl=(ename,)
     mycursor.execute(sql,rl)
     constr.commit()
def MainMenu():
     while True:
          print("Enter 0 : To Create Database")
          print("Enter 1 : To Register Alumni")
          print("Enter 2 : To View Alumni Details ")
          print("Enter 3 : To Edit Alumni Details ")
          print("Enter 4 : To Search Alumni ")
          print("Enter 5 : To delete Alumni")
          print("Enter 6 : To Add a Event")
          print("Enter 7 : To Search a Event")
          print("Enter 8 : To Delete a Event")
          userInput = int(input("Please Select An Above Option: "))
          print("\n")
          if(userInput == 0):
               create_database()
          if(userInput == 1):
               RegisterAlumni()
          elif (userInput==2):
               ViewAlumniDetails()
          elif (userInput==3):
               EditAlumni()
          elif (userInput==4):
               SearchAlumni()
          elif (userInput==5):
               DeleteAlumni()
          elif (userInput==6):
               ScheduleEvent()
          elif (userInput==7):
               ViewEventDetails()
          elif (userInput==8):
               DeleteEvent()
          else:
                    print("Enter correct choice. . . ")
                    break
MainMenu()

def AskChoiceAgain():
     AksChcRun = input("\nwant To Run Again Y/n: ")
     while(AksChcRun.lower() == 'y'):
          MainMenu()          
AskChoiceAgain()
