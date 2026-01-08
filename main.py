password = input("Enter your password: ")

if 8<= len(password) <=15:
    print ("Password leght is valid.")
else:
    print ("Password too short or too long. Please try again!")