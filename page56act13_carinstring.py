#Jennelle Fernando 10S
#Program 1 for actvitiy 13............
string="The cars present include Ford, Mercedes,  Toyota, BMW, Audi and Renault"
make=input("Please enter a make to search: ")

#convery the entered text to uppercase
make=make.upper()
#convery string to uppercase because we need to have a common case
#this al;lows the user to enter in any case

string=string.upper()

#Check whether the entered make is in the String variable

#If it is in; True is assignmed to present variable, if not; False will be reassigned
present=make in string

if present==True:
    print("It is present")
else:
    print("It is not present")


#Program 2
#Present = make in string
    if make in string:
            print("It is present")
    else:
        print("It is not present")
    

































