import openpyxl
import random
import re
import sys

pattern = r'[;|,]'
food_type_lun ={}
food_type_din ={}

def choose_food_type():
    
    
    print("Ποσες φορες θελετε να τρώτε ανα βδομαάδα τις παρακάτω κατηγορίες φαγητών, συνολο να ναι 14")
    print ("Κατηγοριες: Κοτοπουλο, Μοσχαρι, Μακαρονια, Οστρακοειδή, Aυγα, Λαδερα, Οσπρια, Ψαρι , Junk food , Ελαφρύ γεύμα")
    rem = 14
    chicken = int(input("\nΚοτοπουλο: "))
    food_type["chicken"] =chicken
    rem -= chicken
    if (rem < 0 ):
        print("Δωσατε παραπάνω από 14 γεύματα για την βδομάδα")
        sys.exit()
    else :
        print (f"Σας απομενουν {rem} γευματα ")
        beef = int(input("\nΜοσχαρι: "))
        food_type["beef"] =beef
        rem -= beef
    if (rem < 0 ):
        print("Δωσατε παραπάνω από 14 γεύματα για την βδομάδα")
        sys.exit()
    else :
        print (f"Σας απομενουν {rem} γευματα ")
        pasta = int(input("\nΜακαρονια: "))
        food_type["pasta"] =pasta
        rem -= pasta
    if (rem < 0 ):
        print("Δωσατε παραπάνω από 14 γεύματα για την βδομάδα")
        sys.exit()
    else :
        print (f"Σας απομενουν {rem} γευματα ")
        selfish = int(input("\nΟστρακοειδή: "))
        food_type["selfish"] =selfish
        rem -= selfish
    if (rem < 0 ):
        print("Δωσατε παραπάνω από 14 γεύματα για την βδομάδα")
        sys.exit()
    else :
        print (f"Σας απομενουν {rem} γευματα ")
        eggs = int(input("\nAυγα: "))
        food_type["eggs"] =eggs
        rem -= eggs
    if (rem < 0 ):
        print("Δωσατε παραπάνω από 14 γεύματα για την βδομάδα")
        sys.exit()
    else :
        print (f"Σας απομενουν {rem} γευματα ")
        ladera = int(input("\nΛαδερα: "))
        food_type["ladera"] =ladera
        rem -= ladera
    if (rem < 0 ):
        print("Δωσατε παραπάνω από 14 γεύματα για την βδομάδα")
        sys.exit()
    else :
        print (f"Σας απομενουν {rem} γευματα ")
        legumes = int(input("\nΟσπρια: "))
        food_type["legumes"] =legumes
        rem -= legumes
    if (rem < 0 ):
        print("Δωσατε παραπάνω από 14 γεύματα για την βδομάδα")
        sys.exit()
    else :
        print (f"Σας απομενουν {rem} γευματα ")
        fish = int(input("\nΨαρι: "))
        rem -= fish
        food_type["fish"] =fish
    if (rem < 0 ):
        print("Δωσατε παραπάνω από 14 γεύματα για την βδομάδα")
        sys.exit()
    else :
        print (f"Σας απομενουν {rem} γευματα ")
        junk_food = int(input("\nJunk food:"))
        rem -= junk_food
        food_type["junk_food"] =junk_food
    if (rem < 0 ):
        print("Δωσατε παραπάνω από 14 γεύματα για την βδομάδα")
        sys.exit()
    else :
        print (f"Σας απομενουν {rem} γευματα ")
        light_meal = int(input("\nΕλαφρύ γεύμα:"))
        food_type["light_meal"] =light_meal
        rem -= light_meal
    if (rem < 0 ):
        print("Δωσατε παραπάνω από 14 γεύματα για την βδομάδα")
        sys.exit()
    else :
        print (f"Σας απομενουν {rem} γευματα ")
    if rem > 0 :
        print("Δωσατε λιγοτερα  από 14 γεύματα για την βδομάδα")
        sys.exit()

    for key, value in food_type.items():
        print(key, value)
    return food_type

# Read meals from Excel file
def import_foods(food_file,food_type):
    workbook = openpyxl.load_workbook("/content/nutrition_calculator/"+food_file+".xlsx")
    worksheet = workbook[food_type]
    meals = {}
    for row in worksheet.iter_rows(min_row=2, values_only=True):
        name = row[0]
        ingredients = re.split(pattern, row[1])
        calories = row[2]
        description = row[3]
        unit = True if row[4]==1 else False
        heavy = row[5]
        fats = row[6]
        carbs = row[7]
        proteins = row[8]
        meals[name] = {"name": name, "calories": calories, "ingredients": ingredients, "unit": unit, "description":description, "heavy":heavy, "fats":fats,"carbs":carbs,"proteins":proteins }
    #print(meals) 
    return meals
    # Define the user's calorie goal and foods they don't like
    


def find_foods(meals,calorie_goal,foods_not_liked , num_meals):
    #calorie_goal = int(input("Enter your calorie goal: "))
    #foods_not_liked = input("Enter any foods you don't like, separated by commas: ").lower().split(",")
    
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
              print(f"Πρέπει να τρώς  {meal['amount']}  {meal['name']} για {meal['calories']}  θερμίδες.\n")
              final_foods.append(meal)
              num_meals = num_meals-1
              if (num_meals == 0): 
                break #gia na dialegei mono ena fagito
          else:
              meal['amount']= round(amount*100)
              meal["calories"]=round(meal['calories'] * amount)
              print(f"Πρέπει να τρώς  {meal['amount']} γραμμάρια {meal['name']} για {meal['calories']} θερμίδες.\n")
              final_foods.append(meal)
              #print (meal)
              num_meals = num_meals-1
              if (num_meals == 0): 
                break #gia na dialegei mono ena fagito
    return final_foods
              

    #print(final_foods) #ama dialegei mono ena fagito
# Print the meal and amount


def split_lun_din(food_type):
    turn ="lun"
    food_type_lun = food_type
    food_type_din =food_type
    for key, value in food_type_lun.items():
        food_type_lun[key]=0
    for key, value in food_type_din.items():
        food_type_din[key]=0
    

    for key, value in food_type.items():
        rem= value
        while(rem>0):
            if (turn =="lun"):
                food_type_lun[key] +=1
                turn ="din"
                rem -=1
            elif (turn ="din"):
                food_type_din[key] +=1
                turn ="lun"
                rem -=1


def food_finder(calorie_goal,foods_not_liked, food_file):
    food_type = choose_food_type()
    split_lun_din(food_type)
    breakfast_list =[]
    snack_liat =[]
    snack2_list =[]
    lunch_list=[]
    dinner_list=[]


    if calorie_goal[0]!=0 :
        print("Πρωινό : ")
        breakfast_list =  food_finder(calorie_goal[0],foods_not_liked, "foods_new","breakfast",14)
        #food_finder(calorie_goal[0],foods_not_liked, "foods_new","breakfast") #replace foods with breakfast
    if calorie_goal[1]!=0 :
        print("Δεκατιανό : ")
        snack_list = food_finder(calorie_goal[1], foods_not_liked,"foods_new","snack",14)#replace foods with snack 1
    if calorie_goal[2]!=0 :
        print("Μεσημεριανό : ")
        for key, value in food_type_lun.items():
           lunch_list += food_finder(calorie_goal[2], foods_not_liked,"foods_new",key, value) #replace foods with lunch
    if calorie_goal[3]!=0 :
        print("Απογευματινό : ")
        snack2_list = food_finder(calorie_goal[3], foods_not_liked,"foods_new",14) #replace snack 2 with breakfast
    if calorie_goal[4]!=0 :
        print("Βραδινό : ")
         for key, value in food_type_din.items():
           dinner_list += food_finder(calorie_goal[2], foods_not_liked,"foods_new",key, value) #replace foods with lunch
    
    print(f"breakfast : {breakfast_list}")
    print(f"snack 1 : {snack_liat}")
    print(f"lunch : {lunch_list}")
    print(f"snack 2 : {snack2_list}")
    print(f"dinner : {dinner_list}")

