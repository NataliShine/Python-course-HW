#Homework 5.1

n=int(input("Enter the number: "))
fact=1
if n<0:
    print("factorial doesn't exist for negative numbers")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of", n, "is", fact)

#Homework 5.2 

def fib(term):
   if term <= 1:
       return (term)
   else:
       return (fib(term-1) + fib(term-2))

number_of_terms = 20
for i in range(number_of_terms):
    print(fib(i))


