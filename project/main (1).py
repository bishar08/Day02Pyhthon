#Data Types
print("Welcome to the tip Calculator.")
total_bill = float(input("what was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give 10, 12, 15? "))
number_of_people = int(input("How many people to split the bill? "))
tip_per = tip_percentage / 100
_total_bill = total_bill * tip_per
new_total_bill = total_bill + _total_bill
each_person = new_total_bill / number_of_people
final_amount = round(each_person, 2)
final_amount = "{:.2f}".format(each_person)
print(f"Each person should pay: {final_amount}")
