# if a year devisible by 4 and not divisible by 100 or divisible by 400 then it is a leap year


year = int(input("Enter a year: "))


def is_leap_year(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False    


