import string
import random
import sys

# variables
# department - department names
# number - how many EC2_names needed

def string_generator(size=10, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))

department = input("Enter Department: Sales, Logistics, Management, Qaulity, Research, Marketing, Accounting, Finances:")  
    
for _ in department:
    
    if department == ("Sales") or department.lower() == ("sales") :
        #print ("Sales")
        break
    
    elif department == ("Logistics") or department.lower() == ("logistics") :
        #print ("Logistics")
        break
    
    elif department == ("Management") or department.lower() == ("managmenet") :
        #print ("Management")
        break
    
    elif department == ("Quality") or department.lower() == ("qaulity") :
        print("Ready")
        #print ("Quality")
        break
    
    elif department == ("Research") or department.lower() == ("research") :
        print("Ready")
        #print("Research")
        break
    
    elif department == ("Marketing") or department.lower() == ("marketing") :
        print("Ready")
        #print("Marketing")
        break
    
    elif department == ("Accounting") or department.lower() == ("accounting") :
        #print ("Accounting")
        break
    
    elif department == ("Finances") or department.lower() == ("finances") :
        #print ("Finances")
        break
    
    else:
        print("Department not available.")
    
number = int(input("How many do you need?:"))

if number > (0):
    print ("Standby.")
        
if number <= (0):
    print("Must enter a number greater than zero for request.")
    while number <= (0):
        next_step = int(input("How many do you need?:"))
            #print ("Screams internally with a smile")
        break
            
for _ in range(1, number + 1):
    name = (department)
    EC2_name = (name + string_generator)
    
print("Instances named:", EC2_name)
