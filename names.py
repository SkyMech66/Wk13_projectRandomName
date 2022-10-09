import random
import string
import sys

# variables
# depatment - department names
# number    - how many EC2_name instances requested


def string_generator(size=10, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))

department = input("Enter Department: Sales, Logistics, Management, Qaulity, Research, Marketing, Accounting, Finances: ")  
    
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
        #print ("Quality")
        break
    
    elif department == ("Research") or department.lower() == ("research") :
        #print("Research")
        break
    
    elif department == ("Marketing") or department.lower() == ("marketing") :
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
    
number = int(input("How many do you need?: "))

if number > 0:
    print("Standby.")
    
elif number <= 0:
    #print ("Screams internally with a smile")
    print("Must enter number greater than zero for request ")
 
print("Names generated")

for _ in range(1, number + 1):
    unique_name = department
    EC2_name = unique_name + (":") + string_generator()
    print("Instance named: ", EC2_name)
