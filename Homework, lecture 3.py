#Training slide 

numbers  = [10, 5, 7, 2,1]
print ('Original list content:', numbers) #Printing original list content

numbers [0] = 111 
print ('New list content:', numbers)

#Training slide 

numbers = [10, 5, 7, 2, 1]
print ('Original list content:', numbers) #Printing original list content 
numbers[0] = 111
print ('\nPrevious list content:', numbers) #Printing original list content
numbers [1] = numbers [4] #Copying value of the fifth element to the second 
print ('New list content:', numbers) #Printing current list content 

#Training slide

numbers = [10, 5, 7, 2, 1]
print ('Original list content:', numbers)
numbers [0] = 111
print ('\nPrevious list content;', numbers)
numbers [1] = numbers [4]
print ('Previous list content:', numbers)
print (numbers) #Printing the whole list 

#Training slide, len function 

numbers = [10, 5, 7, 2, 1]
print ('Original list content:', numbers)
numbers [0] = 111
print ('\nPrevious list content:', numbers)
numbers [1] = numbers [4]
print ('Previous list content:', numbers)
print ('\nList lenght:', len(numbers))

#Training slide

numbers = [10, 5, 7, 2, 1]
print ('Original list content:', numbers)
numbers [0] = 111
print ('\nPrevious list content:', numbers)
numbers [1] = numbers [4]
print ('Previous list content:', numbers)
print ("\nList's lenght:", len(numbers))
del numbers [1] #Removing the second element from the list
print ("New list's content:", numbers) #Printing cureent list content

#Training slide

numbers = [111, 7, 2, 1]
print (numbers[-1])
print (numbers[-2])

#Homework 3.1 

het_list = [1, 2, 3, 4, 5] #This is an existing list of numbers hidden in the hat 
print ('Lenght of the list:', len(het_list)) #Lenght of list 
place = int(input()) #User put his number 
het_list [2] = place #Replace the middle number of list for user number 
del het_list [4] #Delete the last element of the list 
print ('Lenght of the list:', len(het_list)) #Lenght of the existing list 
print (het_list)

#Training slide 

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

numbers.append (4)
print (len(numbers))
print (numbers)

numbers.insert (0,222)
print (len(numbers))
print (numbers)

#Training slide 

my_list = []
for i in range (5):
    my_list.append (i+1)
    print (my_list)
    print ('len = ', my_list)
print()
print (my_list)

#Training slide 

my_list = [10, 1, 8, 3, 5]
total = 0
for i in range (len(my_list)):
    total += my_list[i]
print (total)

#Training list 

my_list = [10, 1,8,3,5]
total = 0
for i in my_list: 
    total += 1 
print (total)

#Training slide 

variable_1 = 1
variable_2 = 2
variable_2 = variable_1
variable_1 = variable_2
print (variable_1, variable_2)
print()

#Homework 3.2 

beatles = []  #empty list created 
print ('Step 1:', beatles) 
beatles.append('John Lenon, Paul McCartney, George Harrison') #add names to my list 
print ('Step 2:', beatles)
for i in range (2): #user put names and this names added to list 
    beatles.append(input('Enter the name:'))
print ('Step3', beatles)
for i in range(2): #delete one name 
    del beatles[-1]
print ('Step 4:', beatles)
beatles.insert(0, 'Ringo Star') #add new name 
print ('Step 5', beatles)
print("The Fab", len(beatles))

#Training slide 

my_list = ['white', 'purple', 'yellow', 'green']
print (len(my_list))
del my_list[2]
print (len(my_list))

#Training slide 

my_list = [8, 10, 6, 2, 4]
swapped = True 
while swapped:
    swapped = False
    for i in range(len(my_list)-1):
        if my_list[i] > my_list [i+1]:
            swapped = True 
            my_list [i], my_list [i+1] = my_list [i+1], my_list [i]
print (my_list)



