#Produce an user name
#Sub Porgram to generate the user name

def createUserName(fName,lName):
    userName=(fName[0:3]+"-"+lName[0:1]).upper()
    return userName

#Main Program
firstName=["Annmarie", "Johnathan", "Peter"]
lastName=["Smith","Perera", "Eyer"]

userNameArray=[]

#Read each pair or first name and last name
for i in range(len(firstName)):

#Function call and append the Product code to the array\
    userNameArray.append(createUserName(firstName[i],lastName[i]))

print(userNameArray)

