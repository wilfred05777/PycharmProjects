print("Welcome to the Roller Coaster! ")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the Roller Coaster!")

    """ Nested if statement example below """
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5 ")
    elif age <= 18:
        print("Please pay $7.")
    elif age < 22:
        print('Please pay $8')
    else:
        print("Please pay $12.")

else:
    print("Sorry, you have to grow taller before you can ride.")
