
num1=int(input("enter a number"))
num2=int(input("enter a number"))


add=num1+num2
sub=num1-num2
mul=num1*num2
div=num1/num2
while True:
    user_input=str(input("choose the choices:+,-,*,/"))
    if user_input=="exit":
        break
    if user_input=="+":
        print(add)
    elif user_input=="-":
        print(sub)
    elif user_input=="*":
        print(mul)
    elif user_input=="/":
        print(div)
    else:
        print("invalid choices")


