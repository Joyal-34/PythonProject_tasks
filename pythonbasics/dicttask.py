this_dict={
    "user_name":"x",
    "password":"y"
}
user_1=input("Enter the user_name ")
user_2=input("Enter the password")
if user_1==this_dict["user_name"] and user_2==this_dict["password"]:
    print("login Sucessfully")
else :
    print("login Failed")