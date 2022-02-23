#Training slide 

list_1 = [1]
list_2 = list_1
print (list_1, list_2)

list_1 [0] = 2 
print (list_1, list_2)

#Training slide 

list_1 = [1]
list_2 = list_1 [:]
print (list_1, list_2)
list_1 [0] = 2
print (list_1, list_2)
my_list = [10, 8, 6, 4, 2]
new_list = my_list [1:3]
print (new_list)

#Training slide 

my_list = [10, 8, 6, 4, 2]
new_list = my_list [:3]
print (new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list [3:]
print (new_list)

#Training slide 

my_list - [0, 3, 12, 8, 2]
print (5 in my_list)
print (5 not in my_list)
print (12 in my_list)

#Training slide 

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False 
for i in range (len(my_list)):
    found = my_list [i] == to_find
    if found:
        break 
if found:
    print ('Element found at index', i)
else: 
    print ('absent')

#Homework 3.4 

mylist = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique = []
for x in mylist:
    if x not in unique:
        unique.append (x)
print (mylist)
print ('Unique elements:', unique)

#Training slide 

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print (a)
print (a[1])
print (a[2])
print (a[3])
print()
print (a[0][0])
print (a[0][1])
print (a[0][2])
print()
print (a[2][0])
print (a[2][1])
print (a[2][2])
print()

#Training slide

n = 5
matrix5 = [[0 for j in range(n)] for i in range (n)]
print ('Sixe is:', n, 'x', n)
print (matrix5)
print ()
print (matrix5[0])
print (matrix5[1])
print (matrix5[2])
print (matrix5[3])
print (matrix5[4])
print()

for i in range(n):
    print(matrix5[i])

print()
matrix5[0][0] = 99
for i in range (n):
    print (matrix5[i])

#Homework 3.5 

s = input().strip()
sw = s.split(" ")

newList = []
for str in sw:
    newList.append(int(str))

numberSum = sum(newList)

print (numberSum)

#Homework 3.6 

s = '4 4 777 77 77 0 9 22 2 5 2'
l = s.split()
new_l = []
 
for i in l:
  if l.count(i) > 1 and i not in new_l:
    print(i, end=' ')
    new_l.append(i)





