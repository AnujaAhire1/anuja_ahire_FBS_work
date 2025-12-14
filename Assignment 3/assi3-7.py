# Predefined correct credentials
correct_userid = "admin"
correct_password = "1234"

# Taking input from user
userid = input("Enter User ID: ")
password = input("Enter Password: ")

# Checking credentials using branching
if userid == correct_userid and password == correct_password:
    print("Login successful!")
else:
    print("Invalid User ID or Password.")
