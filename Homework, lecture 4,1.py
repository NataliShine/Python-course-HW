#Training slide 

def message():
    print ('Enetr a value:' )
    a= input()
    print(a)

print ('We start here.')
message()
print ('We end here.')

#Training slide 

def message (what, number):
    print ('Enter', what, 'number', number)

a= "NANANA"
message (a, '333')

message ('telephone', 11)
message ('price', 5)
message ('number', 'number')

#Training slide 

def my_function (a, b, c):
    print (a, b , c)

my_function (1, 2, 3)

def introduction (first_name, last_name):
    print ('Hello, my name is:', first_name, last_name)

introduction ('Luke', 'Skywalker')
introduction ('Jesse', 'Quick')
introduction ('Clark', 'Kent')

def introduction (first_name, last_name):
    print ('Hello, my name is:', first_name, last_name)

introduction ('Skywalker', 'Luke')
introduction ('Quick', 'Jesse')
introduction ('Kent', 'Clark')

#Training slide 

def adding (a, b, c):
    print (a, '+', b, "+", c, '=', a+b+c)

adding (1,2,3)
adding (c = 1, a = 2, b=3)
adding (4, 3, c=2)
adding (3, c=1, b=2)
adding (3, a=1, b=2)

#Training slide 

def strange_function(n):
    if (n % 2 == 0):
        return True 
print (strange_function (2))
print (strange_function (1))
print ()

print (strange_function (8))
print (strange_function (5))
print()

print (strange_function (10))
print (strange_function (52))
print()

#Training slide 

def strange_list_fun (n):
    strange_list = []

    for i in range (0, n):
        strange_list.insert (0, 1)

    return strange_list
print (strange_list_fun (5))

#Training slide 

def hil (my_list):
    my_list [1] = 1111
    print ('Inside the func:', my_list)

a = ['Adam', 'John', 'Lucy', 'Goose']
print ('Original list:', a)
hil (a)
print ('Orig after proc:', a)
print ()

a = ['Adam', 'John', 'Lucy', 'Goose']
print ('Original list:', a)
hil (a[:])
print ('Orig after proc:', a)
print ()

a = ['Adam', 'John', 'Lucy', 'Goose']
print ('Original list:', a)
hil (a[:2])
print ('Orig after proc:', a)
print()

