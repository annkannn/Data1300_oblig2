
try:
    name = input("What is your name: ").strip()
    if not name:
        raise ValueError("Cannot be empty")
    
    weight_kg  = float(input("How much do you weigh (kg): "))
    if weight_kg <= 0:
        raise ValueError("Weight must be higher than 0!")
    
    height_m = float(input("how tall are you: "))
    if height_m <= 0:
        raise ValueError("Height must be higher than 0!")
    
except ValueError as e:
    print(f"Invalid input {e}")

BMI_calc = round(weight_kg / (height_m)**2,2)
print(f"Hello {name}! your BMI is {BMI_calc}")

if BMI_calc < 18.5:
    print("Underweight")
elif 18.5 <= BMI_calc <= 24.9:
    print("Normal")
