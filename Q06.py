#   Q6

#   Structure of sales record is
#   StaffID, First name, Last name, January sales, February sales,
#   March sales, April sales, May sales, June sales

staffSales = [
["101TGY" , "George" , "Taylor" , 6009 , 5262 , 3745 , 7075 , 1943 , 4432],
["103FCY" , "Fehlix" , "Chayne" , 8717 , 2521 , 5777 , 6189 , 5089 , 6957],
["102SBY" , "Sumren" , "Bergen" , 5012 , 1063 , 7937 , 9560 , 1115 , 5499],
["104SBK" , "Samira" , "Beckle" , 1140 , 9206 , 3898 , 8544 , 5937 , 8705],
["105NBT" , "Nellie" , "Bogart" , 3017 , 3342 , 5939 , 2479 , 3374 , 2297],
["106CGT" , "Cheryl" , "Grouth" , 9620 , 7160 , 5113 , 4803 , 5492 , 2195],
["107DGT" , "Danuta" , "Graunt" , 1583 , 7450 , 1026 , 7463 , 2390 , 6509],
["108JDN" , "Jaiden" , "Deckle" , 4064 , 4978 , 2984 , 3159 , 1464 , 4858],
["109JCK" , "Jimran" , "Caliks" , 6253 , 7962 , 2732 , 7504 , 2771 , 5193],
["110DDN" , "Deynar" , "Derran" , 6305 , 8817 , 5200 , 3647 , 3365 , 1256]]


#--------------------------------------------------------------------------
#   Write your code below this line
allStaffTotal=0
highestSales=0
secondSales=0
highFName=""
highLName=""
secondFName=""
secondLName=""

print("Sales foreach member of staff", "\n\n")

for staff in staffSales:
    staffTotalEach=0
    staffTotalEach=staff[3]+staff[4]+staff[5]+staff[6]+staff[7]+staff[8]
    allStaffTotal=allStaffTotal=allStaffTotal+staffTotalEach
    print("Total slaes by: ", staff[1], " ", staff[2], "is", staffTotalEach)

    if staffTotalEach>highestSales:
        secondSales=highestSales
        highestSales=staffTotalEach
        secondFName=highFName
        secondLName=highLName

        highFName=staff[1]
        highLName=staff[2]

    else:
        if staffTotalEach>secondSales:
            secondSales=staffTotalEach
            secondFName=staff[1]
            secondLName=staff[2]
#print("Variable high", high)
print("Total sales made by the whole team is", allStaffTotal)
print("Highest sales is: ", highestSales, "by: " , highFName, "", highLName)
print("Second Highest sales is: ", secondSales, "by", secondFName, " ", secondLName)
        
