def factorial(num_1):
    fact=1
    for i in range(1,num_1+1):
        fact=fact*i
    print(fact)
num_1=int(input('Enter a number'))
factorial(num_1)
