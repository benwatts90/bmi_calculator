#BMI calculator

height = float(input("Please enter your height in metres, using a decimal: "))

weight = float(input("Please enter your weight in Kilograms, using a decimal: "))

heightSquared = lambda a: a * a

bmi = weight / heightSquared(height)

print("Your body mass index is: " + str(bmi))

if bmi < 18.5:
    print("You are underweight")
elif bmi <= 25:
    print("You have a normal body mass index")
else:
    print("You are overweight")

