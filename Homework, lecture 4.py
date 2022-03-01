#Homework 4.1 have problems with this tasks.. 

#Homework 4.2

def is_year_leap(year):
    if year == 2000 or year == 2016: 
        return True
    else: 
        return False 

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print (yr, '->', end ='')
    result = is_year_leap(yr)
    if result == test_results[i]:
        print ('OK')
    else: 
        print('Failed')


#Homework 4.3 

def is_year_leap(year):
    if year == 2000 or year == 2016:
        return True 
    else: 
        return False 

def days_in_month(year, month):
    if year == 2000 or year == 2016:
        leap_month_list = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        date_month = leap_month_list [month]
        return date_month
    elif year == 1900 or year == 1987:
        regular_month_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 31, 31]
        date_month = regular_month_list [month]
        return date_month
    else: 
        pass 

    test_years = [1900, 2000, 2016, 1987]
    test_months = [2, 2, 1, 11]
    test_results = [28, 29, 31, 30]

    for i in range (len(test_years)):
        yr = test_years [i]
        mo= test_months [i]
        print (yr, mo, '->', end="")
        result = days_in_month (yr, mo)
        if result == test_results [i]:
            print ('OK')
        else: 
            print ('Failed')

#Homework 4.4 

def is_leap_year(year): 
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month): 
    if year < 1 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_leap_year(year):
        res = 29
    return res


def day_of_year(year, month, day): 
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

print(is_leap_year(1900))
print(days_in_month(2021, 11))
print(day_of_year(2000,2,29))

#Homework 4.5 

def is_prime(number):
    for i in range(2,number):
        if number%i == 0:
            return False
    return True

def main():
    for num in range(2,501):
        if is_prime(num):
            print(num, end=" ")

main()

#Homework 4.6 

def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784 
    # 1 mile = "1.60934" meters
    # 1 km   = 1000 meters .. 1000 * 1.60934 = 1609.344
    # 100km = 100 * 1000 meters (The function works on 100 km)
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km_100 = miles * 1609.344 * 1000 / 100
    liters = 3.785411784
    return liters / km_100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))



