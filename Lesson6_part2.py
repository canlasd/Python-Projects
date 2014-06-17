from Lesson6 import Time

"""
# First Time object
myTime1 = Time()
# myTime1.print_time()
myTime1.set_time(1, 2, 3)

# Second Time object
myTime2 = Time()
myTime2.set_time(12, 0, 0)

print ("My two time objects are now storing:")
myTime1.print_time()
myTime2.print_time()

print(myTime1.__class__)


"""



myTime=Time()

# create object


myTime.set_time(12,58,46)

for i in range(100):
    myTime.print_time()
    myTime.tick()
