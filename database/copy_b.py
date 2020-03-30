##
# this is just going to create a table, following procedures soon.
# also while inserting some random data for instant use.
# by the one n only.
##
##
# Hello Welcome to [], based on []
# and various other modules.
# Please note the minimum required modules : mutagen, pygame, ttkthemes
# To install you must use: "pip install *" as * followed by the right module syntax.
# Coded to work on Python 3.8
# Last test on Python 3.8
# Might need some changed for older versions.
# Written by Ayushmaan Karmokar.
##
##
# Code Quality - E-
# Last Edited - 2 Mar, 2020
# Check my Github on - ***
##
##
#   signature by mazushi
#   signature by mazushi
##
# modules
import os,sqlite3
import dbm
import time

com = sqlite3.connect("muta.db")
cur = com.cursor()
#
cur.execute("create table customer (id int(5),name varchar(50),credit varchar(19),room_id int(4),comments varchar(100),grade varchar(2))")
cur.execute("create table employee (emp_id int(2),emp_name varchar(20),emp_comments varchar(20),emp_pass int(5))")
#
print("Tables Created Feeding Data..")
time.sleep(1)
cur.execute('''insert into customer(ID,name,credit,room_id,comments,grade) values (10001,"Ravi P","4567 8901 2345 6789",3101,"likes roses","B-"),(10002,"Bridgette B","4588 8505 2444 6782",2105,"always keep extra champagne","A+"),(10003,"Rena L","4564 8301 2545 6769",3102,"raque is the soap","A"),(10004,"Lisa P","4547 8341 5334 6484",5101,"new customer","B+"),(10005,"Jennie C","8909 6546 4324 6432",9101,"only give higher floors","C")''')
#
print("Table Customer is feeded with 5 data..")
time.sleep(1)
#
print("Feeding data to employee")
cur.execute('''insert into employee(emp_id,emp_name,emp_comments,emp_pass) values (12,"Farhan C","null",3245),(13,"Jaque D","null",4455),(14,"Grisa M","null",9900)''')
print("Table emp is feeded with 3 data")
time.sleep(1)
#
print("line executed, data not saved")
time.sleep(1)
print("everything done - testing data")
# cur.execute("select name from customer where id = 10001")
id_store = 10001
print("select id,name,room_id,comments,grade from customer where id = {0}".format(id_store))
cur.execute("select id,name,room_id,comments,grade from customer where id = {0}".format(id_store))
a = cur.fetchall()
print(a[0])
# test 2
print("final test")
cur.execute("select * from employee")
b = cur.fetchone()
print(b[0])
print('\n\n done..!')
#cur.fetchall()
com.commit()
com.close()
print("close this program, you wont need to do this again")



## 
## 

### 
### 
'''db = dbm.open("lol","c")
db["lol"] = "WRITE OPE"

if db["lol"]!=None:
	print("lasun")
else:
	print("wata")
	
print(db["lol"])'''
# FTW

