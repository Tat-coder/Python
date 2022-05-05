#Jennelle Fernando 10S
#create first name array
firstName=["Ann", "Tom", "Jane", "Windy"]

#Create a last anme array
lastName=["Smith", "Perera","Eliz", "Eyer"]

#Create amd empty 2D array that can store the users
userName=[]

for index in range(0, len(firstName)): #Loop to travase
    fName=firstName[index]
    userNameFirst=fName[0:2].lower() #extract strings from first anme
    lName=lastName[index]
    userNameLast=lName[0:1].lower()#extract string from the last Name
    userName.append(userNameFirst+"-"+userNameLast)
    print("The user name of", firstName[index], "is", userName[index])

print('\n')
#print user name array

print(userName)

print('\n')
#print for each user name
for each in userName:
    print(each)
    

