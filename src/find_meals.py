import openpyxl
import random

# Read meals from Excel file
def import_foods():
    workbook = openpyxl.load_workbook("/content/nutrition_calculator/foods.xlsx")
    worksheet = workbook["Lunch"]
    meals = {}
    for row in worksheet.iter_rows(min_row=2, values_only=True):
        name = row[0]
        ingredients = row[1].split(";")
        calories = row[2]
        unit = True if row[3]==1 else False
        meals[name] = {"name": name, "calories": calories, "ingredients": ingredients, "unit": unit}
    print(meals) 
    return meals
    # Define the user's calorie goal and foods they don't like
    


def find_foods(meals):
    calorie_goal = int(input("Enter your calorie goal: "))
    foods_not_liked = input("Enter any foods you don't like, separated by commas: ").lower().split(",")
    
    # Filter meals to exclude foods the user doesn't like
    meals_filtered = {k: v for k, v in meals.items() if not any(food.lower() in v["ingredients"] for food in foods_not_liked)}

    # Find a meal that meets the calorie goal (+/- 15%) and return the meal and amount
    #meal = None
    #while not meal:
    #    meal = random.choice(list(meals_filtered.values()))
    geumata = list(meals_filtered.values())
    random.shuffle(geumata)


    final_foods=[]
    # Shuffle the list in place

    for meal in geumata:
      
        if meal["unit"]:
            amount = round(calorie_goal / meal["calories"])
            if amount > 0 and amount <3:
                meal["amount"] = amount
            else:
                meal = None
        else:
            amount = round(calorie_goal / meal["calories"] ,1)
            if amount > 0 :
                meal["amount"] = amount
            else:
                meal = None
        
        if meal and abs(meal["calories"] * amount - calorie_goal)  > 0.15 * calorie_goal :
            meal = None
        elif meal:
          if  meal["unit"]:
              meal["calories"]=round(meal['calories'] * meal['amount'])
              print(f"Πρέπει να τρώς  {meal['amount']}  {meal['name']} για {meal['calories']}  θερμίδες.")
              final_foods.append(meal)
          else:
              meal['amount']= round(amount*100)
              meal["calories"]=round(meal['calories'] * amount)
              print(f"Πρέπει να τρώς  {meal['amount']} γραμμάρια {meal['name']} για {meal['calories']} θερμίδες.")
              final_foods.append(meal)

    print(final_foods)
# Print the meal and amount

def run():
  find_foods(import_foods())