def calculate_bmi(weight, height):
    return weight / height**2


bmi = calculate_bmi(80, 1.7)

print(round(bmi, 2))
