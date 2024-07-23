def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI value according to WHO guidelines.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to BMI Calculator")
    print("-------------------------")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calculate_bmi(weight, height)
    bmi_category = interpret_bmi(bmi)
    
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are in the category of: {bmi_category}")

if __name__ == "__main__":
    main()
