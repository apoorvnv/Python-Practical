import mysql.connector
db=mysql.connector.connect(host="localhost",user="sahiil",passwd="3000",database=
                           "demo")
cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS student") #This drops the table and replaces it
query="""CREATE TABLE student(
NAME VARCHAR(20), Surname VARCHAR(20),
AGE INT, PRN VARCHAR(30))"""
cursor.execute(query)
#----------------------------------------------------#
choice=input("ENTER OPERATION TO PERFORM, INSERT ,UPDATE ,DELETE ,EXIT----> ")
print()
while choice!="EXIT":
    
    if choice=="INSERT":
        
        #INSERTING VALUES
        query="""INSERT INTO student(NAME, Surname, AGE, PRN)
                VALUES(%s, %s, %s, %s )"""
        val=int(input("PRESS 1 if you want to add more data or PRESS 0 to exit: "))
        print()
        while val!=0:
            records_to_insert = [input("ENTER NAME: "),input("ENTER SURNAME: "),int(input("ENTER AGE: ")),input("ENTER PRN: ")]
            print()
            cursor.execute(query,records_to_insert)
            val=int(input("PRESS 1 if you want to add more data or PRESS 0 to exit: "))
            db.commit()
    elif choice=="UPDATE":
        
        #UPDATE
        P=input("ENTER PRN of STUDENT---> ")
        #changing Age
        A=int(input("ENTER NEW AGE---> "))
        query="update student set AGE={0} where PRN={1}".format(A,P)
        cursor.execute(query)
        db.commit()

    elif choice=="DELETE":
        #DELETE
        P=int(input("ENTER PRN OF STUDENT TO BE DELETED: "))
        query="delete from student where PRN={0}".format(P)
        cursor.execute(query)
        db.commit()
        
        
        
    choice=input("ENTER OPERATION TO PERFORM, INSERT ,UPDATE ,DELETE ,EXIT----> ")
    print()
    

db.close()
