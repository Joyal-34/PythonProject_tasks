guess_num=5
guess_count=0

while True :
    guess_user=int(input('enter a number'))
    if guess_user==guess_num:
        print("You Won")
        break
    else:
        guess_count+=1
    if guess_count==3:
        print("you lost...you don't have anymore more chance left")
        break
    else :
        print("try Again")
