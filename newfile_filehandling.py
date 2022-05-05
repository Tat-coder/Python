def newFile():
    newFile=open("newfile.txt",'w')
    for i in range(10):
        record=("year 10 computer science\n")
        print(record)
        newFile.write(record)
    newFile.close()
#main program
newFile()
