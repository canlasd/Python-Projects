rate = eval(input("Please enter your rate"))
hours=eval(input("Please enter the hours worked"))
                 
if hours<40:
    pay=hours*rate
            


else:
    pay=hours*rate
    Overtime=hours-40
    OvertimeHours=Overtime*1.5*rate
    pay = pay+OvertimeHours

TotalPay=pay + OvertimeHours
print ("your total pay is  " ,TotalPay)
