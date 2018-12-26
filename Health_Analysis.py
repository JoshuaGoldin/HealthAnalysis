import MySQLdb
def print_results(r, indexes):
 #   for row in results:
 #       print "row length", len(r)
    tempobj = {};
    a = 0
    for i in r:
        # print "id"
        # print row

        # print "i", i
        # i=i+1
        tempobj[indexes[a]] = i
        a = a + 1
        # print "i", i
    # print "row len", len(row)
    #print "row1", row1
    return tempobj;
print "Step 1"
db = MySQLdb.connect("localhost", "JoshuaGoldin", "chessmaster", "Health")
print "Step 2"
import json
cursor = db.cursor()
prompt=raw_input("Type 1 if table exists")
if prompt == "1":
    cursor.execute("Drop Table If Exists Client")
    cursor.execute("Drop Table If Exists Client_Blood")
print "Step 3"
cursor.execute("Select Version()")
print "Step 4"
data = cursor.fetchone()
print "Database version : %s " % data
Client = """Create Table Client (ID Char(20), First_Name Char(20), Last_Name Char(20), Age Int, Sex Char(1))"""
print "Client Table created"
Client_Blood = """Create Table Client_Blood (ID Char(20), Age Int, Blood_Type Char(3), RBCN Int, RBCS Int, WBCN Int)"""
print "Client Blood created"
try:
    cursor.execute(Client)
    print "hi"
    cursor.execute(Client_Blood)
    print "bye"
    db.commit()
except Exception as E:
    print E
    print "Error"
    db.rollback()
print "Step 5"
Client_Data = """Insert Into Client(ID, First_Name, Last_Name, Age, Sex) values ('00001', 'Joshua', 'Goldin', 21, 'm')"""
print "Client Data inserted"
Client_Blood_Data = """Insert Into Client_Blood(ID, Age, Blood_Type, RBCN, RBCS, WBCN) values ('00001', 21, 'a-', 6100000, 400000, 10000)"""
print "Client Blood Data inserted"
print Client_Data
try:
    cursor.execute(Client_Data)
    print "a"
    a=cursor.rowcount
    print a
    cursor.execute(Client_Blood_Data)
    db.commit()
except Exception as E:
    print E
    print "Abortinsert"
    db.rollback
#print field_names
Get_Client = "Select * From Client"
print "Got Get_Client"
Get_Client_Blood = "Select * From Client_Blood"
print "Got Get_Client"
try:
    cursor.execute(Get_Client)
    print "Executed Get_Client"
    results = cursor.fetchall()
    cursor.execute(Get_Client_Blood)
    print "Executed Get_Client_Blood"
    results1 = cursor.fetchall()
    print "Set results"
    #results=results+results1
    #print "Results: ", results
    i=0
    a=01
    #row=[]
    row1={}
    l=["id", "fname", "lname", "age", "sex"]
    l1=["blood_type", "rbcn", "rbcs", "wbcn"]
    for x in results:
        data = print_results(x, l)
    # for y in results1:
    #     data = print_results(y, l1)

    #data.update(print_results(results1[0],l1))
    print "hello"
    print "data: ", data
    #print "id, fname, lname, age, sex, blood_type, rbcn, rbcs, wbcn", (id, fname, lname, str(age), sex, blood_type, str(rbcn), str(rbcs), str(wbcn))
    db.commit()
except Exception as E:
    print E
    db.rollback()
    print "Error: unable to fetch data"
db.close()