def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login successful"
    else:
        return "Invalid username or password"

username = input("Enter username: ")
password = input("Enter password: ")

print(login(username, password))