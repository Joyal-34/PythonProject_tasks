user_details={}
while True:
    user_opt=input('choose from  CRUD /Login : ')

    if user_opt =="c" :
       user_details['name']=input("Enter the name :")
       user_details['age']=input("Enter your Age :")
       user_details['password']=input("enter the password :")
       print('User data uploaded Sucessfully.....')

    elif user_opt=="r":
        print(user_details )
    elif user_opt=="u":
        update_data=input("what you want to update name,age,password")
        if update_data=='name':
           user_details['name']=input('Enter your name :')
        elif update_data=='age':
            user_details['age']=input("update age")
        elif update_data=='password':
            user_details['password']=input("update password")
            print('your data updated sucessfully')
    elif user_opt=="d":
        user_details.clear()
        print("delete successful")
    elif user_opt=='login':
        user_name=input('enter user name')
        password=input("enter password")
        if user_name==user_details['name'] and password==user_details['password']:
            print('sucessfully logged in.....')
        else:
            print('incorrect username or password')
            break