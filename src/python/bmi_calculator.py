def calculate_bmi(weight_kg, height_m):
    """
    Calculates Body Mass Index (BMI).
    """
    if height_m <= 0:
        return 0
    return weight_kg / (height_m ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

if __name__ == "__main__":
    weight = 70
    height = 1.75
    bmi = calculate_bmi(weight, height)
    print(f"Weight: {weight}kg, Height: {height}m")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {get_bmi_category(bmi)}")
