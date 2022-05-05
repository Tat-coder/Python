#standard linear search
team= ['Anya', 'Max', 'Erik', 'William', 'David', 'Shirley', 'Cheryl', 'Ben', 'Rosie', 'Henry', 'Georgina']
searchName=input('Please enter a name: ')
found=False
index=0
while index<len(team) and found==False:
    if searchName==team[index]:
        found=True
    else:
        index=index+1
if found==True:
    print(searchName, 'Is in the team.')
else:
    print(searchName, ' has not been select for the team.')


# linear search on a unsorted list
team=['Anya', 'Max', 'William', 'David', 'Shirley', 'Cheryl', 'Ben', 'Rosie', 'Henry', 'Georgina']
team.sort()
searchName=input('Please enter a name: ')
found= Flase
notInList=False
index=False
index=0
comparisonCount=0
while index<len(team) and found==False and notInList==False:
    comparisonCount=comparisonCount+1
    if searchName==team[index]:
        found=True
    elif searchname<team[index]:
        notInList=True
    else:
        index=index+1
if found:
    print(searchName, 'is in the team')
else:
    print(searchName, 'has not been picked for the team.')
print('The number of comparisons made was, ' , comparisonCount)
    
