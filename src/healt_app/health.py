
class Health:
    def __init__(self, name: str, weight_kg: float, height_m: float):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if weight_kg <= 0:
            raise ValueError("Weight must be greater than 0.")
        if height_m <= 0:
            raise ValueError("Height must be greater than 0.")

        self.name = name.strip()
        self.weight_kg = weight_kg
        self.height_m = height_m
        self.BMI = round(weight_kg / height_m ** 2, 2)
        self.category = self._categorize()

    def _categorize(self) -> str:
        if self.BMI < 18.5:
            return "Underweight"
        elif self.BMI < 25:
            return "Normal"
        elif self.BMI < 30:
            return "Overweight"
        else:
            return "Obese"
        
    
    def get_health_advice(self) -> str:
        if self.category == "Underweight":
            return ("You are currently underweight. Focus on eating nutrient-rich foods "
                    "and consider increasing your calorie intake with healthy meals. "
                    "Consulting a nutritionist or doctor is recommended.")
        elif self.category == "Normal":
            return ("You are at a healthy weight — great job! Maintain a balanced diet "
                    "and stay active with regular exercise. Keep up your current healthy habits.")
        elif self.category == "Overweight":
            return ("You are slightly overweight. Consider adjusting your diet by reducing "
                    "processed foods and increasing physical activity. "
                    "Small lifestyle changes can make a big difference over time.")
        else:
            return ("Your BMI indicates obesity. It is strongly recommended to consult "
                    "a doctor or weight loss specialist for a personalised plan. Focus on "
                    "gradual, sustainable changes to your diet and exercise routine.")
        
    def get_ideal_weight(self) -> float:
        return round(22 * self.height_m ** 2, 2)
