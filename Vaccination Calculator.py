# Covid vaccination program
import datetime
from datetime import date, time, timedelta
print("THIS PROGRAM CALCULATES WHEN YOU COULD BE FULLY VACCINATED FOR COVID-19.")
status = str(input("Have you been received a Covid-19 vaccination? Yes/No: "))
if status == "No":
    print("We recommend that you get vaccinated.")
if status == "Yes":
    Vaccine = str(input("Which vaccine did you recieve? Moderna or Pfizer: "))
    Second_Vaxx_Q = str(input("Have you received your second vaccination? Yes/No: "))
    if Second_Vaxx_Q == "No" and Vaccine == "Moderna":
        First_Vaccine = int(input("How many days ago did you receive your first vaccine? "))
        current_date = datetime.datetime.now()
        x = 28 - First_Vaccine
        y = First_Vaccine
        days = (current_date + timedelta(days=x)).strftime('%m-%d-%Y')
        days2 = (current_date - timedelta(days=y)).strftime('%m-%d-%Y')
        z = 42 - First_Vaccine 
        days3 = (current_date + timedelta(days=z)).strftime('%m-%d-%Y')
        print("You received your first vaccine on ", days2)
        print("You can receive your second vaccine as early as ", days)
        print("You can be fully vaccinated as early as", days3)
    elif Second_Vaxx_Q == "No" and Vaccine == "Pfizer":
        First_Vaccine = int(input("How many days ago did you receive your first vaccine? "))
        current_date = datetime.datetime.now()
        x = 21 - First_Vaccine
        y = First_Vaccine
        days = (current_date + timedelta(days=x)).strftime('%m-%d-%Y')
        days2 = (current_date - timedelta(days=y)).strftime('%m-%d-%Y')
        z = 35 - First_Vaccine 
        days3 = (current_date + timedelta(days=z)).strftime('%m-%d-%Y')
        print("You received your first vaccine on", days2)
        print("You can receive your second vaccine as early as", days)
        print("You can be fully vaccinated as early as", days3)
    elif Second_Vaxx_Q == "Yes":
        age = str(input("Are you 18 or older? Yes/No: "))
        if age == "No":
            Second_Vaccine = int(input("How many days ago did you receive your second vaccine? "))
            z = 14 - Second_Vaccine
            current_date = datetime.datetime.now()
            VaccinationDate = (current_date + timedelta(days=z)).strftime('%m-%d-%Y')
            print("You are fully vaccinated as of", VaccinationDate)
            print("You cannot receive the booster until you are 18 years old.")
        elif age == "Yes":
            booster = str(input("Have you received your booster? Yes/No: "))
            if booster == "No":
                Second_Vaccine = int(input("How many days ago did you receive your second vaccine? "))
                x = 183 - Second_Vaccine
                current_date = datetime.datetime.now()
                days = (current_date + timedelta(days=x)).strftime('%m-%d-%Y')
                z = 14 - Second_Vaccine
                VaccinationDate = (current_date + timedelta(days=z)).strftime('%m-%d-%Y')
                print("You are fully vaccinated as of", VaccinationDate)
                print("You can receive the booster as early as", days)
            elif booster == "Yes":
                print("Congratulations, you have received all vaccinations possible for Covid-19")
            else:
                print("Error, format is wrong, make sure you use capital Y, lowercase e, lowercase s; capital N, lowercase o.")
        else:
            print("Error, format is wrong, make sure you use capital Y, lowercase e, lowercase s; capital N, lowercase o.")
    else:
        print("Error, format is wrong. Please try again.")
else:
    print("Error, format is wrong, make sure you use capital Y, lowercase e, lowercase s; capital N, lowercase o.")