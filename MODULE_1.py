import sys # sys is built-in module that can be used after importing.
locations=sys.path
for i in locations:
    print(i)
    
import calendar
leapdays=calendar.leapdays(2000, 2050) # how many leapdays inbetween 2000-2050.
print(leapdays)
isitleap=calendar.isleap(2024)
print(isitleap) # if 2024 has leap day then it will print true.