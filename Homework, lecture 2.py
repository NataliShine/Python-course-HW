print(r"\\\\\\\\\\")

#Training slide

x = 10
y = 20
z = 20
print (x == y)
print (z == y)
print (x != y)
print (x > 20)
print (x < y)
print (x >= 10)
print (y <= 20)

x = 10
print(x, type(x))


#Training slide

amount = int(input('Enter amount: '))
if amount<1000:
    discount = amount*0.05
    print ('Discount', discount)
else:
    discount = amount*0.10
    print ('Discount', discount)

print ('Net payable:', amount-discount)


#Training slide 

amount = int(input('Enter amount: '))
if amount<1000:
    discount = amount*0.05
    print ('Discount', discount)
elif amount<5000:
    discount = amount*0.10
    print ('Discount', discount)
else:
    dicount = amount*0.15
    print ('Discount', discount)

print ('Net payable:', amount-discount)


#Example

number1 = int(input('Enter the first number: ')) #read number 1
number2 = int(input('Enter the second number: ')) #read number 2
if number1 > number2:
    larger_number = number1
else: larger_number = number2
print ('The largest number is: ', larger_number)


#Homework 3.1

a = int(input())
b = int(input())
c = int(input())
d = int(input())
max = a
if max < b:
   max = b
if max < c:
   max = c
if max < d:
   max = d
print(max)


#Training slide

largest_number = -999999999
number = int(input())
if number == -1:
    print (largest_number)
    exit()
if number > largest_number:
    largest_number = number

#Homework 3.2

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
max = a
min=b
if max < c:
   max = c
if max < d:
   max = d
if max < e:
   max = e
if max < f:
   max = f
if min > a:
   min = a
if min > c:
   min = c
if min > d:
   min = d
if min > e:
   min = e
if min > f:
   min = f
print (max)
print (min)

#Homework 3.3

plant =input("Your plant = ")
if plant=="Spathiphyllum":
  print("Yes - Spathiphyllum is the best plant ever!")
elif plant=="spathiphyllum":
  print("No, I want a big Spathiphyllum!")
else:
  print("Spathiphyllum! Not", plant)

#Homework 3.4

income = float(input('Enter the income: '))
if income == 400:
    tax = (0.15*income)
if income == 500:
    tax = (0.15*income)

#Homework 3.5

year = int(input("Enter a year: "))
if year < 1582:
  print ("Not within the Gregorian calendar")
if year % 4 != 0:
  print ("Common year")
elif year % 100 != 0:
  print ("Leap Year")
elif year % 400 != 0:
  print ("Common year")
else:
  print ("Leap year")

#Training slide

count = 0
while (count < 9):
    print ('The count is: ', count)
    count = count + 1
print ('Goodbye!')

#Training slide

counter = 5
while counter != 0:
  print ('Inside the loop.', counter)
  counter -= 1
print('Outside the loop', counter)

#Homework 3.6

secret_number = 768  #Our secret number
while True:
    number = int(input("Enter an integer: "))    
    if number == secret_number:
        break
    print("Ha ha! You're stuck in my loop!")

print("Well done, muggle! You are free now.")


#Training slide

power = 1
for expo in range (16):
    print ('2 to the power of', expo, 'is', power)
    power *=2

#Homework 3.7

import time
for mississippi in range (1,6):
    print (mississippi, 'Mississippi')
    time.sleep(1)
print ('Ready or not, here I come')
    
#Training slide

print ('The break instruction: ')
for i in range (1,6):
    if i == 3:
        break
    print ('Outside the loop.')
print ('\nThe continue instruction: ')
for i in range (1,6):
    if i == 3:
        continue
    print ('Inside the loop.', i)
print ('Outside the loop.')


#Homework 3.8

secret_word = ""
while True:
    secret_word = input("You're stuck in an infinite loop!\nEnter a secret word to leave the loop.")
    if secret_word == "chupacabra":
        print("You've successfully left the loop.")
        break






