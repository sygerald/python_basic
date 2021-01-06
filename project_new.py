# import library#

import csv
import sys

# Declare global lists----------------#
ctype=[]
brand=[]
model=[]
price=[]
capac=[]

# Declare Welcome function--------------#
def welcome():
    
    print("*"*40)
    print("Welcome to SG Vehicle Mart")
    print("*"*40)


def brandsearch(x):
    read_file_handle = open("car_list_new.csv","r")
    reader1 = csv.reader(read_file_handle)    
        
    i=0
    index_no=[]
        
    for row in reader1:
        ctype.append(row[0])
        brand.append(row[1])
        model.append(row[2])
        price.append(row[3])
        capac.append(row[4])
        i+=1

    j=0
    if brand.count(x)==0:
        print("No such brand available.")
    else:
        for j in range(len(brand)):
            if x == brand[j]:
                index_no.append(j)
            else:
                pass
            j+=1
                             
    for k in range(len(index_no)):
        print(k+1, ". ", ctype[index_no[k]], brand[index_no[k]], model[index_no[k]],"$",price[index_no[k]], "seating:",capac[index_no[k]])
        k+=1
       
    read_file_handle.close()


def ctypesearch(x):
    read_file_handle = open("car_list_new.csv","r")
    reader1 = csv.reader(read_file_handle)    
    
    i=0
    
    index_no=[]
    
    for row in reader1:
        ctype.append(row[0])
        brand.append(row[1])
        model.append(row[2])
        price.append(row[3])
        capac.append(row[4])
        i+=1

    j=0
    
    if ctype.count(x)==0:
        print("No such type available.")
    else:
        for j in range(len(ctype)):
            if x == ctype[j]:
                index_no.append(j)
            else:
                pass   
            j+=1
                         
    for k in range(len(index_no)):
        print(k+1,". ", brand[index_no[k]], model[index_no[k]],"$",price[index_no[k]], "seating:",capac[index_no[k]])
        k+=1
   
    read_file_handle.close()

def pricesearch(x,y):
    read_file_handle = open("car_list_new.csv","r")
    reader1 = csv.reader(read_file_handle)    
    
    i=0
    
    index_no=[]
    
    for row in reader1:
        ctype.append(row[0])
        brand.append(row[1])
        model.append(row[2])
        price.append(row[3])
        capac.append(row[4])
        i+=1

    intprice = list(map(int, price))        # convert to list of integers#
    
    if max(intprice) < int(x) or min(intprice) > int(y):
        print("Outside of price range.")
    else:
        for j in range(len(intprice)):      
            if int(x) <= intprice[j] <= int(y): 
                index_no.append(j)
            else: 
                pass
            j+=1

        for k in range(len(index_no)):
            print(k+1,".", ctype[index_no[k]], brand[index_no[k]],model[index_no[k]],"$",intprice[index_no[k]])
            k+=1
     
    read_file_handle.close()
   

#--------------MAIN PROGRAM ----(31 lines)-------------------
print("\n")
welcome()

print("Press S to search by brand (e.g. Nissan):")
print("Press P to search by price in $:")
print("Press T to search by type (e.g. SUV):")
print("Press X to exit program" )
choice = input("Enter your choice: ").upper()


if choice == "S":
    brandname = input("Search by brand: ").lower()
    
    if brandname.isalpha():
        brandsearch(brandname)
    else:
        print("Please specify brand correctly")

elif choice == "P":
    maxprice = input("Max Price($): ")
    minprice = input("Min Price($): ")
    
    if maxprice.isdigit() and minprice.isdigit():
    
        if int(maxprice) > int(minprice):
            pricesearch(minprice, maxprice)
        else:
            print("Invalid prices.")
            
    else:
        print("Incorrect prices entered")

    
elif choice == "T":
    typename = input("Search by type (Sedan,SUV,MPV,Hatchback,Coupe): ").lower()

    if typename.isalpha():    
        ctypesearch(typename)
    else:
        print("Please specify car type correctly")

               
elif choice == "X":
    print("Thank you and goodbye.")
    exit()


else:
    print("Incorrect selection. Please try again.")

#-------------------- END --------------------











    
        