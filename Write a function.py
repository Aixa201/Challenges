def is_leap(year):
    leap = False
    if year in range(1900,10**5):
        if year % 4 == 0 and year % 100 != 0:
            leap = True
        elif  year % 100 == 0 and year % 400 !=0:
            leap = False
        elif year % 4 == 0 and year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
    return leap

year = int(input())
print(is_leap(year))