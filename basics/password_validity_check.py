import re

def is_valid(password):

    """password must be atleast 8 characters
       starts with letters or underscore
       cannot contain any special characters except underscore
       cannot contain blank spaces"""
    
    
    if len(password) < 8:
        print("Invalid password, consider a longer password.")
        return
    else:
        pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
        if re.search(pattern, password):
            print("Valid Password...")
        else:
            print("Invalid Password...")


password = input("Enter the password : ")

is_valid(password)