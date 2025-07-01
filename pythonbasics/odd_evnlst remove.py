numbers=list(range(1,11))
new_li=[]
even_numbers=[num for num in numbers if num % 2 ==0]
odd_numbers=[num for num in numbers if num %2!=0]
print("numbers:",numbers)
print("even number:",even_numbers)
print("odd number :",odd_numbers)
new_li.append(even_numbers)
new_li.append(odd_numbers)
print("new_li:",new_li)


