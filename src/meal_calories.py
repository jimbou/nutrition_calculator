def run():
    total_calories = int(input("Δώσε τον ημερίσιο στόχο σου σε θερμίδες: "))
    meal_percentages = [0, 0, 0, 0, 0]  # Initialize meal percentage list with zeros
    meal =["πρωινό","σνακ","μεσημεριανό","απογευματινό","βραδινό"]
    for i in range(4):
        remaining_percentage = 100 - sum(meal_percentages)
        meal_percentage = float(input(f"Δώσε το ποσοστό θερμίσων που θες να καταναλώσεις στο γευμα {meal[i]} (Σου απομένει  {remaining_percentage}% ): "))
        while meal_percentage > remaining_percentage:
            print(f"Σφαλμα: το άθροισμα των ποσοστών θερμιδών ξεπερνά το  100%. Σου απομένει {remaining_percentage}% .")
            meal_percentage = float(input(f"Δώσε το ποσοστό θερμίσων που θες να καταναλώσεις στο γευμα {meal[i]} (Σου απομένει  {remaining_percentage}% ): "))
        meal_percentages[i] = meal_percentage

    remaining_percentage = 100 - sum(meal_percentages)
    print(f"Για το τελευταίο γεύμα σας αναθέτουμε το  υπολοιπώμενο ποσοστό θερμίδων: {remaining_percentage} %")
    meal_percentages[4] = remaining_percentage  # Assign remaining percentage to the final meal

    meal_calories = [int(total_calories * p / 100) for p in meal_percentages]  # Calculate the number of calories for each meal
    print(meal_calories)