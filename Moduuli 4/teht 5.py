username = "python"
password = "rules"

yritykset = 0
while yritykset < 5:
    tunnus = input("Enter username: ")
    salasana = input("Enter password: ")
    if tunnus == username and salasana == password:
        print("Welcome")
        break
    else:
        print("Incorrect username or password. Please try again.")
        yritykset += 1

if yritykset == 5:
    print("Access denied")