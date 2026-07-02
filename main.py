print("Welcome to Password Strength Analyser!")

name = input("What's your name? ")


def greet():
    print(f'Welcome, {name}!')


greet()


def get_password():
    password = input('Enter your password: ')
    return password
password = get_password()

# def score_password():


has_upper = False
has_lower = False
has_number = False
has_special_characters = False
special_characters = r"!@#$%^&*()_-+={[}]|\<,>.?/':;"

def check_length(password):
    print(f"Password length:", len(password))

check_length(password)


while len(password) < 8:
    print('''Password is too Weak!
Minimum length is 8 characters''')
    password = input('Enter your password: ')
    print(f"Password length:", len(password))

def check_characters(password):
    global has_upper
    global has_lower
    global has_number
    global has_special_characters

    
    for i in password:
        if i.isupper():
            has_upper = True

        if i.islower():
            has_lower = True

        if i.isdigit():
            has_number = True

        if i in special_characters:
            has_special_characters = True


check_characters(password)


print(f"Contains uppercase: {has_upper}")
print(f"Contains lowercase: {has_lower}")
print(f"Contains numeric character: {has_number}")
print(f"Contains special characters: {has_special_characters}")

if len(password) <= 11:
    print('''Length is medium!
Could be better!''')
    print(f"Thank you, {name}!")


else:
    print("Length is perfect!")
    print(f"Thank you, {name}!")
