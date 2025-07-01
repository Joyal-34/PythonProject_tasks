def celsius_to_farenheit(celsius):
    farenheit=(celsius*9/5)+32
    print(celsius)
def farenheit_to_celsius(farenheit):
    celsius=(farenheit-32)*5/9
    print(farenheit)
temp=int(input("enter the temperature"))
choice=input("f-farenheit,c-celsius:")
if choice=="f":
   farenheit_to_celsius(temp)
elif choice=="c":
    celsius_to_farenheit(temp)
else :
    print("Invalid")

