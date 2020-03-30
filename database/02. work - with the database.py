##
#   program to work on already created database.
#   test on taking password from employee, and say their name on the write id n pass
#   finally give emp data on the customer they want, except credit, unless specified to quit.
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
# Code Quality - C-
# Last Edited - 2 Mar, 2020
# Check my Github on - ***
##
##
#   signature by mazushi
#   signature by mazushi
##
# modules
import os,sqlite3,dbm,time,sys


# test_feature
try:
    import copy_b
    print("you didnt run the first program")
except:
    print("database already initialized -  thank you for following rules.")


com = sqlite3.connect("muta.db")
cur = com.cursor()

def cust(com,cur):
        que = input("Do you want customer data? or LOGOUT? (Y/N)")
        que = que.upper()
        if que == "Y":
            # print("What customer data do you want?")
            info(com,cur)
        else:
            time.sleep(1)
            print("LOG OUT.")
            sys.exit()

def info(com,cur):
    while True:
        inc = input("What would you like to seach FOR? (ID/NAME/ALL/ROOT)")
        inc = inc.upper()
        
        if (inc == "ROOT"):
            pass_code = str(input("Enter root pass: "))
            if ( pass_code != heavens ):
                print("root environment not allowed for you.\n you have been reported")
                sys.exit()
            else:
                print(" thanks for ruining me ")
                cur.execute("select * from customer")
                doomsday = cur.fetchall()
                print(doomsday)
            
        
        elif (inc == "ALL"):
            cur.execute("select id from customer")
            id_store = cur.fetchall()
            # id_cust = cur.fetchall()
            take = int(input("Enter ID: "))
            print(id_store)
            for id_search in (0,5):
                if (take == id_store[id_search][0]):
                    print ("data for customer - ",take)
                    cur.execute("select id,name,room_id,comments,grade from customer where id = {0}".format(take))
                    print_data = cur.fetchall()
                    if print_data!=None:
                        print("Customer DATA = ",print_data[0])
                    else:
                        print("Record not Found")
                    break
                
        
        elif (inc == "ID"):
            take = input ("Enter Name: ")
            print(take)
            cur.execute('select id from customer where name = "{0}"'.format(take))
            data_p = cur.fetchall()
            if (data_p!=None):
                # print(data_p)
                print("Customer ID = ",data_p[0][0])
            else:
                print("Record not Found")
        
        
        elif (inc == "NAME"):
            name_take = input ("Enter ID: ")
            print(name_take)
            cur.execute('select id from customer where id = {0}'.format(name_take))
            data_n = cur.fetchall() 
            if (data_n!=None):
                print("Customer NAME = ",data_n[0][0])
            else:
                print("Record not Found")
        
        
        else:
            choici = input("invalid value. Try again?(Y/N)")
            if ( choici == "N"):
                print("System Exit\n\nThank You.")
                sys.exit()


# initial _ initialization
cur.execute("select emp_id from employee")
idkeys = cur.fetchall()
cur.execute("select emp_pass from employee")
passkeys = cur.fetchall()
heavens = str(passkeys[2][0])

print("System Ready.")

print("\n\nMURAGAPA HOTEL AND SYSTEMS LTD: ")
ide = int(input("Employee ID: "))
passe = int(input("Password: "))

for ids in range(0,3):
    if (ide == idkeys[ids][0]):
        idf  = ids
        break
if (passe == passkeys[idf][0]):
    print("Success taking you to customer data")
    cust(com,cur)
    #reak
else:
    print("invalid pass")
# else:
#   print("hmm somethings wrong")


# extracting emp data from db
