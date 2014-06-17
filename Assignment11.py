try:
    counter=1
    while (counter>=1):
     number=2.0**counter
     counter=counter+0.001
except OverflowError as of:
    print(number, " counter = floating point number ")
except KeyboardInterrupt:
    print("loop interrupted by CRTL+C")

"""
This program calculates the value of the number by multiplying
number by counter.  Counter increments by 0.001 after each loop.
If number is a floating point number (number with a decimal point)
except overflow occurs.  If CRTL+C is pressed the except Keyboard Interrupt
occurs
"""
