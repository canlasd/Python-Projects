
from statistics import mean

my_list=[]

input_number=eval(input("Enter a number:  type -999 to quit"))



  


while(input_number!=-999):
    my_list.append(input_number)
    input_number=eval(input("Enter a number:  type -999 to quit"))

if(input_number== -999 and len(my_list)>0):
    print("Average is  " , (mean(my_list)))
    print("The list is  " , my_list)

else:
    print("No Input")
    



          
                 

