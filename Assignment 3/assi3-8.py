#WAP to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the the same number then show him success message otherwise failed. (Something like captcha)

import random

userid = input("Enter userid: ")
password = input("Enter password: ")

if userid == "admin" and password == "1234":
    code = random.randint(1000, 9999)
    print("Captcha:", code)

    user_code = int(input("Enter the same number: "))

    if user_code == code:
        print("Success")
    else:
        print("Failed")
else:
    print("Wrong userid or password")

