total_calories = int(input("Enter your daily calorie goal: "))
meal_percentages = [0, 0, 0, 0, 0]  # Initialize meal percentage list with zeros

for i in range(4):
    remaining_percentage = 100 - sum(meal_percentages)
    meal_percentage = float(input(f"Enter the percentage of calories you want to consume in meal {i+1} (you have {remaining_percentage}% remaining): "))
    while meal_percentage > remaining_percentage:
        print(f"Error: the sum of meal percentages exceeds 100%. You have {remaining_percentage}% remaining.")
        meal_percentage = float(input(f"Enter the percentage of calories you want to consume in meal {i+1} (you have {remaining_percentage}% remaining): "))
    meal_percentages[i] = meal_percentage

remaining_percentage = 100 - sum(meal_percentages)
print(f"Για το τελευταίο γεύμα σας αναθέτουμε το  υπολοιπώμενο ποσοστό θερμίδων: {remaining_percentage} %")
meal_percentages[4] = remaining_percentage  # Assign remaining percentage to the final meal

meal_calories = [int(total_calories * p / 100) for p in meal_percentages]  # Calculate the number of calories for each meal
print(meal_calories)