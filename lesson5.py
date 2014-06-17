"""
def hello_lesson ():
    ""This function prints out Hello Lesson 4 and 5""
    print("Hello Lesson4")
    print("Hello Lesson5")

hello_lesson()
print("Let's try that again")
print()
hello_lesson()



def print_value(value):
    ""This function prints the value passed in""
    print("Your value is:", value)

print_value(5)
print_value("number")

name="Pat"
print_value(name)



def change_value(value):
    ""This function changes the value passed in to 1 (global)""
    global number
    number=1
    

number=5
print("Outside number is:  " , number)
change_value(number)
print("Outside, number is now: " , number)



def square(num):
    ""this function calculates the square of a number""
    return num*num

for i in range(1,11):
    print(square(i))
    
"""

def convert_to_fahrenheit(num):
    """This converts a list of numbers from celsius to fahrenheit"""
    return ((9.0/5.0)*num)+32

for i in range(1,10):
    print(convert_to_fahrenheit(i))



    





