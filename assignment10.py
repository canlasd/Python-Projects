
import shelve

records=shelve.open('C:/Python Projects/records.txt', 'c')

# input the student string value.  Note only input was used
student=input("Please enter student's name (or -999 to quit): ")


while (student!='-999'):

        # input the grade.  Note eval is added before input to store input as number
        # if eval was removed, the input value will be treated as string
        grade=eval(input("Please enter student's grade "))
        records[student]=grade
        # this is an alternate solution.  This stores the key [student] and
        # value grade.  Both of which were inputted by the user
        
        
        student=input("Please enter student's name (or -999 to quit): ")
        


        print()
        print()

search=input("Which Student Score you would like to see:  -999 to quit:  ")
while search!='-999':
    if search in records:
        print("Student's name:  ", search, "         Student's Grade:  ", records[search])
          
          
          
    else:
        
        print (search,  "not found")
          
    print()
    print()

    search=input("Which Student Score you would like to see:  -999 to quit")

# WATCH OUT FOR INDENTATIONS.  Wrong indentations can result in infinite loops

records.sync()
records.close()

             
            
        

        
    
    
