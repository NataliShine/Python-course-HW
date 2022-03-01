#Training slide

def my_function ():
    var = 222
    print ('Do I know that variable?', var)

var = 1 
my_function ()
print (var)

#Training slide 

def my_function ():
    global var
    var = 2
    print ('Do I know that variable?', var)

var = 1
my_function ()
print (var)

#Training slide 

def my_function (n):
    print ('I got', n)
    n += 1 
    print ('I have', n)

var = 1
my_function (var)
print (var)

#Training slide 

def bmi (weight, height):
    if weight or height <=0:
        return None
    return weight / height ** 2

print (bmi(0, 0))
print (bmi(4, 4))
print (bmi(-99, 1.65))
print (bmi(0, -10))
print (bmi(52.5, 1.65))

#Training slide

def bmi (weight, height): 
    return weight / height ** 2

print (bmi(52.5, 1.65))

#Training slide 

def bmi (weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200: 
        return None 

    return weight / height ** 2 

print (bmi(352.5, 1.65))

#Training slide 

def is_a_triangle (a, b, c):
    if a + b <=c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False 
    return True

print (is_a_triangle (1, 1, 1))
print (is_a_triangle (1, 1, 3))

#Training slide 

def is_a_triangle (a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True 

print (is_a_triangle (1, 1, 1))
print (is_a_triangle (1, 1, 3))

#Training slide 

def is_a_triangle (a, b, c):
    return a + b > c and b + c >a and c + a >b

a = float (input('Enter the first side\s lenght:'))
b = float (input('Enter the second side\s lenght:'))
c = float (input('Enter the third side\s lenght:'))

if is_a_triangle (a, b, c):
    print ('Yes, it can be a triangle.')
else:
    print ('No, it is not a triangle')

#Training slide 

def is_a_triangle (a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron (a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def area_of_triangle (a, b, c):
    if not is_a_triangle (a, b, c):
        return None
    return heron (a, b, c)

print (area_of_triangle (1., 1., 2. ** .5))

#Training slide 

def factorial_function(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return factorial_function (n - 1) + factorial_function (n - 2)

for n in range (1, 10):
        print (n, '->', factorial_function(n))

#Training slide 

my_tuple = (1, 10, 100, 1000)

print (my_tuple[0])
print (my_tuple[-1])
print (my_tuple[1:])
print (my_tuple[:-2])

for elem in my_tuple:
    print (elem)

#Training slide 

school_class = {}

while True:
    name = input ("Enter the student's name: ")
    if name == '':
        break

    score = int (input("Enetr the student's score (0-10): "))
    if score not in range (0, 11):
        break

    if name in school_class:
        school_class [name] += (score,)
    else:
        school_class [name] = (score,)

for name in sorted (school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class [name]:
        adding += score
        counter +=1
    print (name, ':', adding / counter)