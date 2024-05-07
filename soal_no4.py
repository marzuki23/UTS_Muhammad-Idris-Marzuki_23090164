def calculate_bmi(weight, height):
    bmi = weight / (height**2)
    return bmi

def get_health_recommendation(bmi):
    if bmi < 18.5:
        return "Berat badan kurang, sebaiknya tambah berat badan."
    elif 18.5 <= bmi < 24.9:
        return "Berat badan normal, pertahankan!"
    elif 24.9 <= bmi < 29.9:
        return "Berat badan berlebih, sebaiknya kurangi berat badan."
    else:
        return "Obesitas, sebaiknya segera kurangi berat badan."

def main():
    weight = float(input("Masukkan berat badan (kg): "))
    height = float(input("Masukkan tinggi badan (meter): "))

    bmi = calculate_bmi(weight, height)
    print("BMI Anda:", bmi)

    recommendation = get_health_recommendation(bmi)
    print("Rekomendasi kesehatan:", recommendation)