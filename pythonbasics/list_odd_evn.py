numbers=list(range(1,26))
even_numbers=[num for num in numbers if num % 2 ==0]
odd_numbers=[num for num in numbers if num %2!=0]
print("numbers:",numbers)
print("even number:",even_numbers)
print("odd number :",odd_numbers)
