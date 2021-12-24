import mysql.connector
import os


def MakeDBandTbl():
    os.system("cls")
    global username
    global pswd
    username, pswd = input("Enter username(By Default \'root\''):"), input("Please Enter Password: ")
    entry = input("Is the database and the table already created?(Y/N)\n")
    if ("N" in entry or "n" in entry):
        mydb = mysql.connector.connect(host="localhost", user=username, password=pswd)
        myc = mydb.cursor()
        myc.execute("CREATE DATABASE qovid")
        mydb.commit()
        mydb = mysql.connector.connect(host="localhost", user=username, password=pswd, database="qovid")
        myc = mydb.cursor()
        myc.execute("USE qovid")
        myc.execute(
            "CREATE TABLE logs(NAME VARCHAR(21) NOT NULL,AadharNumber VARCHAR(30) NOT NULL,Risk_Level VARCHAR(30) NOT NULL)")
        mydb.commit()
        mydb.close()

    else:
        print("Press enter to continue.")


def AddRecord(user, aadhar, risk_level):
    mydb = mysql.connector.connect(host="localhost", user=username, password=pswd, database="qovid")
    myc = mydb.cursor()
    myc.execute("USE qovid")
    myc.execute("INSERT INTO logs VALUES (\"" + user + "\",\"" + aadhar + "\",\"" + risk_level + "\")")
    mydb.commit()
    mydb.close()


# print("Done")

MakeDBandTbl()
