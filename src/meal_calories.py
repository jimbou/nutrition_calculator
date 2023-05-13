import find_meals
def input_type():
    while True:
        result = str(input("\n Θες ποσοτά ή αριθμό θερμιδών ; ")).lower()

        if result[0] in [ "π", "Π", "p", "P"]:  
            return "percentage"

        elif result[0] in ["A", "a",  "Α", "α","θ","Θ"]:  
            return "calories"

        else:
            print(f"Λάθος είσοδος: {result} ")
            continue


def run_perc():

    total_calories = int(input("Δώσε τον ημερίσιο στόχο σου σε θερμίδες: "))
    meal_percentages = [0, 0, 0, 0, 0]  # Initialize meal percentage list with zeros
    meal =["πρωινό","σνακ","μεσημεριανό","απογευματινό","βραδινό"]
    for i in range(4):
        remaining_percentage = 100 - sum(meal_percentages)
        meal_percentage = float(input(f"Δώσε το ποσοστό θερμίσων που θες να καταναλώσεις στο γευμα : {meal[i]} (Σου απομένει  {remaining_percentage}% ): "))
        while meal_percentage > remaining_percentage:
            print(f"Σφαλμα: το άθροισμα των ποσοστών θερμιδών ξεπερνά το  100%. Σου απομένει {remaining_percentage}% .")
            meal_percentage = float(input(f"Δώσε το ποσοστό θερμίσων που θες να καταναλώσεις στο γευμα :{meal[i]} (Σου απομένει  {remaining_percentage}% ): "))
        meal_percentages[i] = meal_percentage

    remaining_percentage = 100 - sum(meal_percentages)
    print(f"Για το τελευταίο γεύμα σας αναθέτουμε το  υπολοιπώμενο ποσοστό θερμίδων: {remaining_percentage} %")
    meal_percentages[4] = remaining_percentage  # Assign remaining percentage to the final meal

    meal_calories = [int(total_calories * p / 100) for p in meal_percentages]  # Calculate the number of calories for each meal
    print(meal_calories)
    return (meal_calories)

def run_cal():

    total_calories = int(input("Δώσε τον ημερίσιο στόχο σου σε θερμίδες: "))
    meal_calories = [0, 0, 0, 0, 0]  # Initialize meal calories list with zeros
    meal =["πρωινό","σνακ","μεσημεριανό","απογευματινό","βραδινό"]
    for i in range(4):
        remaining_calories = total_calories - sum(meal_calories)
        meal_cal = float(input(f"Δώσε τον αριθμό θερμίσων που θες να καταναλώσεις στο γευμα : {meal[i]} (Σου απομένoουν  {remaining_calories} θερμίδες ): "))
        while meal_cal > remaining_calories:
            print(f"Σφαλμα: το άθροισμα των ποσοστών θερμιδών ξεπερνά το συνολικο ({total_calories}). Σου απομένoουν {remaining_calories} θερμίδες .")
            meal_cal = float(input(f"Δώσε τον αριθμό θερμίσων που θες να καταναλώσεις στο γευμα :{meal[i]} (Σου απομένoουν  {remaining_calories} θερμίδες ): "))
        meal_calories[i] = meal_cal

    remaining_calories = total_calories - sum(meal_calories)
    print(f"Για το τελευταίο γεύμα σας αναθέτουμε το  υπολοιπώμενον αριθμό θερμίδων: {remaining_calories} ")
    meal_calories[4] = remaining_calories  # Assign remaining calories to the final meal

   
    print(meal_calories)
    return (meal_calories)


def run():
    result = input_type() 
    
    if result == "percentage":
        meals_calories = run_perc()
    else :
        meals_calories = run_cal()
    foods_not_liked = input("Enter any foods you don't like, separated by commas: ").lower().split(",")
    if meals_calories[0]!=0 :
        print("Πρωινό : \n")
        food_finder(meals_calories[0],foods_not_liked, "foods") #replace foods with breakfast
    if meals_calories[1]!=0 :
        print("Δεκατιανό : \n")
        food_finder(meals_calories[1], foods_not_liked,"foods")#replace foods with snack 1
    if meals_calories[2]!=0 :
        print("Μεσημεριανό : \n")
        food_finder(meals_calories[2], foods_not_liked,"foods") #replace foods with lunch
    if meals_calories[3]!=0 :
        print("Απογευματινό : \n")
        food_finder(meals_calories[3], foods_not_liked,"foods") #replace snack 2 with breakfast
    if meals_calories[4]!=0 :
        print("Βραδινό : \n")
        food_finder(meals_calories[4], foods_not_liked,"foods") #replace foods with dinner