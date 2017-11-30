import pymysql

# Open database connection
db = pymysql.connect(host='sh-cdb-gspfisfw.sql.tencentcdb.com',port=63698,user='testuser',password='test123',db='TESTDB')
# prepare a cursor object using cursor() method
cur=db.cursor()

# execute SQL query using execute() method
#cur.execute("SELECT VERSION()")

#Fetch a single row using fetchone() method
#dat=cur.fetchone()

#print("Database version : %s"%dat)

# cur.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Create table as per requirement
""" sql=CREATE TABLE EMPLOYEE (
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT )"""
# prepare sql query to insert a record into the database
"""sql=INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
        VALUES('%s','%s',%s,'%s',%s) %('kela','Hu',38,'F',9999)"""

sql="SELECT * FROM EMPLOYEE WHERE INCOME >%d" %2000

try:
    #Execute the SQL command
    cur.execute(sql)
    #Commit your changes in the database
    #db.commit()

    #Fetch all the rows in a list of lists
    results=cur.fetchall()
    for row in results:
        
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%f" %tuple([i for i in row]))
except:
    #Rollback in case there is any error
    #db.rollback()
    print("error, unable to fetch data")


#disconnect from server
db.close()