height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilogram: "))

# BMI = weight / (height/100)**2 #error
BMI = round(weight / height ** 2) # working
# BMI = round(weight / (height * height)) # working

# BMI = 18 ## debugging

print(f"Your BMI is {BMI}")
if BMI < 18.5:
    print(f"Your BMI is {BMI}, You are underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI}, You have a normal weight")
elif BMI < 30:
    print(f"Your BMI is {BMI}, You are slightly overweight")
elif BMI < 35:
    print(f"Your BMI is {BMI}, You are obese.")
# elif 18.5 <= BMI <= 25:
#     print("You have normal weight")
else:
    print(f"Your BMI is {BMI}, Clinically obese")

