days_in_month={'Jan':31
               ,'Feb':28
               , 'Mar':31}

print(days_in_month.keys())
print(days_in_month.values())
print(days_in_month.items())
'Feb' in days_in_month

"""
creating new dictionary and add new dictionary to original"""

days_in_month2={'May':31, 'Jun':30, 'Jul':31}
days_in_month.update(days_in_month2)
print(days_in_month.keys())
print(days_in_month2.keys())
