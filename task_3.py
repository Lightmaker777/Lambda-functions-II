# Task 3

# decorator named 'protected' that will only allow a valid user to execute the function it decorates.

# The decorator must return a lambda function that will ask the credentials (username and password) to the user (input()) and validate them against hard coded values (for instance, admin|admin).

def protected(func):
    def wrapper(*args, **kwargs):
        username = input("Username: ")
        password = input("Password: ")

        if username == "admin" and password == "admin":
            return func(*args, **kwargs)
        else:
            print("You are not authorized")

    return wrapper

def public():
    print("Hello World!")

@protected
def private():
    print("Welcome, admin!")

public()
private()



