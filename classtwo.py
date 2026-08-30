# task 1 -- is number positive or negative

# task 2 -- takes two input username and password -- if same then print loginv else print re try

# Preset correct credentials
correct_username = "admin"
correct_password = "12345password"

# Take input from the user
username = input("Enter username: ")
password = input("Enter password: ")

# Check if credentials match
if username == correct_username and password == correct_password:
    print("login")
else:
    print("re try")