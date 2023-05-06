def input_gender():
    while True:
        gender = str(input("\nΕισαι άνδρας ή γυναίκα; ")).lower()

        if gender[0] in [ "m", "M", "Α", "α","a","A"]:  
            return "male"

        elif gender[0] in ["Γ", "γ",  "F", "f","g","G"]:  
            return "female"

        else:
            print(f"Λάθος είσοδος: {gender} ")
            continue


def input_stats():
    weight = float(input("\nΔώσε το βάρος σου σε κιλά: "))
    height = float(input("Δώσε το ύψος σου σε εκατοστά: "))
    age = float(input("Δώσε την ηλικία σου σε χρόνια: "))
    weight_lb = weight *2.20462
    height_inch =height /2.54

    stats = [weight_lb, height_inch, age, weight,height]
    return stats

def activity_calories():
    activity_calories = float(input("Δώσε θερμίδες που καίγονται από άσκηση: "))
    return activity_calories

def input_activity():
    print("\n1. Καθιστική ζωή (λίγο ή καθόλου άσκηση)")
    print("2. Ελαφρώς δραστήριος (ελαφριά άσκηση/αθλητισμός 2 με 3 μέρες την βδομάδα)")
    print("3. Μέτρια άσκηση (μέτρια άσκηση/αθλητισμός 3 με 5 μέρες την βδομάδα)")
    print("4. ¨Εντονη άσκηση (έντονη άσκηση/αθλητισμός 6 με 7 μέρες την βδομάδα)")
    print("5. Υπερβολική άσκσησ (παρα πολύ έντονη άσκηση/αθλητισμός και σωματικά κουραστικό επάγγελμα ή γυμναστική 2 φορές την ημέρα)")
    print("6. Συγκεκριμένες θερμίδες την μέρα σε άσκηση)")


    while True:
        activity = input("\nΠόσο δραστήριος είστε; Δωστε τιμή απο 1 ως 6. ")

        if activity.isdigit():
            activity = int(activity)

        else:
            print(
                f"Λάθος είσοδος {activity}. Πρέπει να δώσετε ψηφίο από 1 ως 6")
            continue

        if 1 <= activity <= 5:
            return [int(activity),0]
        elif activity == 6 :
            return [6,activity_calories()]


        else:
            print(
                f"Λάθος είσοδος {activity}. Πρέπει να δώσετε ψηφίο από 1 ως 6")
            continue


def calculate_bmr(gender, stats):
    if gender == "male":
        bmr = 66 + (6.3 * stats[0]) + (12.9 * stats[1]) - (6.8 * stats[2])
        return bmr

    else:
        bmr = 655 + (4.3 * stats[0]) + (4.7 * stats[1]) - (4.7 * stats[2])
        return bmr


def calculate_caloric_needs(bmr, activity):
    if activity[0] == 1:
        caloric_needs = round(bmr * 1.2)
        print(
            f"\nΗ ημερήσια ανάγκη σου σε θερμίδες για να διατηρήσεις το βάρος σου είναι {caloric_needs} θερμίδες.")

    elif activity[0] == 2:
        caloric_needs = round(bmr * 1.365)
        print(
            f"\nΗ ημερήσια ανάγκη σου σε θερμίδες για να διατηρήσεις το βάρος σου είναι {caloric_needs} θερμίδες.")

    elif activity[0] == 3:
        caloric_needs = round(bmr * 1.50)
        print(
            f"\nΗ ημερήσια ανάγκη σου σε θερμίδες για να διατηρήσεις το βάρος σου είναι {caloric_needs} θερμίδες.")

    elif activity[0] == 4:
        caloric_needs = round(bmr * 1.705)
        print(
            f"\nΗ ημερήσια ανάγκη σου σε θερμίδες για να διατηρήσεις το βάρος σου είναι {caloric_needs} θερμίδες.")

    elif activity[0] == 5:
        caloric_needs = round(bmr * 1.9)
        print(
            f"\nΗ ημερήσια ανάγκη σου σε θερμίδες για να διατηρήσεις το βάρος σου είναι {caloric_needs} θερμίδες.")
    else :
        caloric_needs = round(bmr * 1.2 + activity[1])
        print(
            f"\nΗ ημερήσια ανάγκη σου σε θερμίδες για να διατηρήσεις το βάρος σου είναι {caloric_needs} θερμίδες.")



def run_calculator():
    print("\nNOTE: Αυτός ο μετρητής χρησιμοποιεί την μέθοδο του βασικού μεταβολικού ρυθμού.\nSource: http://www.checkyourhealth.org/eat-healthy/cal_calculator.php")

    gender = input_gender()
    stats = input_stats()
    activity = input_activity()
    filo = "Άνδρας" if gender == "male" else "Γυναίκα"
    
    print(
            f"\n{filo}, {stats[2]} ετών, υψους {stats[4]} εκτοστών , βάρους {stats[3]} κιλών , με βαθμίδα άσκησης {activity[0]}")
    bmr = calculate_bmr(gender, stats)

    calculate_caloric_needs(bmr, activity)


run_calculator()