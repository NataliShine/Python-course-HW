#Homework 3.9

word = input('')
word = word.upper()
for letr in word:
    if letr == 'A':
        continue
    if letr == 'E':
        continue
    if letr == 'I':
        continue
    if letr == 'O':
        continue
    if letr == 'U':
        continue
    print (letr)


#Homework 3.10

word = input('')
resStr = ''
word = word.upper()
for letr in word:
    if letr == 'A':
        continue
    if letr == 'E':
        continue
    if letr == 'I':
        continue
    if letr == 'O':
        continue
    if letr == 'U':
        continue
    resStr = resStr + letr
print (resStr)


#Training slide

numbers = [11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
    if num%2 == 0:
        print ('the list contains an even number')
        break
    else:
        print ('the list does not contain even munbers')

#Training slide

count = 0
while count < 5:
    print (count, 'is less than 5')
    count = count + 1
else:
    print (count, 'is not less than 5')

#Homework 3.11 don't know how to do :(

#Homework 3.12

def calculate(a, b, formula):
  if formula == '+':
    return a + b
  elif formula == '-':
    return a - b
  elif formula == '*':
    return a * b
  elif formula == '/':
    return a / b
  else:
    print('Just Leave!')
    return 'Closing program...'

print('Choose a number')
a = float(input())
print('Choose a second number')
b = float(input())
print('Do you want to * / - or + ?')
formula = input()
answer = calculate(a, b, formula)
print(answer)



