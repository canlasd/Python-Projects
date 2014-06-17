"""

try:
    age=eval(input('Please enter your age: '))
    ten_years=age+10
    print("In ten years, you'll be " ,ten_years)

except NameError:
    print("A NameError has occurred")

except Exception:
    #this handles all possible exceptions since all exceptions inherit
    #from Exception class
    print("You must enter a number for your age")
    




print("have a nice day.  Goodbye.")

# list the specific exceptions first then the overall exception.  This way
#it is easy to track specific exception errors



try:
    my_list=[0,1,2]
    print(my_list[4])
except IndexError as ie:
    print(ie)



try:
    infile=open('C\Documents and Settings\Mike\Desktop\myfile.txt','r')
    infile.write("Hello")

    infile.close()

except IOError as ioe:
    print(ioe.filename)
    print(ioe.strerror)




try:
    infile=open('data.txt','r')
    try:
        value=infile.readline()
        number=int(value)
        print(number)
    finally:
        infile.close()
        print("the data file was closed")
except IOError as io:
    print("Could not open file:" , io.filename)
except ValueError:
    print("Could not convert", value, " to a number")

"""


    












    
    
