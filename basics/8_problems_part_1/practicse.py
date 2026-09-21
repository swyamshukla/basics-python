


def check_age():
    age = int(input("Enter your age: "))
    if(age<0):
        print("Age cannot be negative.")
        return
    elif age < 18:
        print("You are a minor.")
    elif age < 65:
        print("You are an adult.")

    else:
        print("You are a senior citizen.")

    return age



print("Welcome to the age checker!")
print(check_age())
