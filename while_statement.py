"""

example of while statement
number=1
while number<=5:
    print(number)
    number=number+1
print("goodbye")
"""

"""
# example of for statement
for number in range(6):
    print(number)
"""
"""
# Takes input from user then computes average
number_nums=eval(input("Input number of numbers to be averaged"))
total=0
for number in range(number_nums):
                 next_num=eval(input("Input the number"))
                 total=total+next_num
Average = total/number_nums
print("The average is  ", Average)

"""
"""
for number in range(1,11):
    if number==4:
        break
    print (number)
else:
    print ("exited normally")

"""

# Takes input from user then quits if -1 is entered

number_nums =eval(input("Enter Number or press (-1) to quit"))
total=0
counter=1
while number_nums!=-1:
    
    number_nums=eval(input("Enter next number or press(-1) to quit"))
    total=total+number_nums
    counter=counter+1

Sum = total+number_nums
average=Sum/counter
print("The sum is:  ", total)
print("The average is:  ", average)
    

    


