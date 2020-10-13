name = input("What is your name Human?\n")
print()

age = input("How old are you? (In years)\n")
print()

tall = float(input("How tall are you? (In meters)\n"))
print()

weight = float(input("How much do you weigh? (In kilograms)\n"))
print()

bmi = float(weight / tall ** 2)
bmi = format(round(bmi, 2))

print("Your name is "+ name +" and you are "+ age +" years old. Your BMI is " + bmi)