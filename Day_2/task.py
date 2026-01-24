#CLASS EXERCISES

# Substring
#print("Hello"[-1])

# String
#print("123" + "345")

# Integer = Whole Number
#print(123 + 345)

# Large Integers
#print(123_456_789)

# Float = Floating Point Number
#print(3.12349)

# Boolean
#print(True)
#print(False)

# Types
#print(type(True))

# Type Casting
#print("123" + "456")
#print(int("123") + int("456"))

# name_of_the_user = input("Enter your name: ")
# lenght_of_name = len(name_of_the_user)
# print("Number of letters in your name: " + str(lenght_of_name))

# print(3 * 3 + 3 / 3 - 3)
# print(3 * (3 + 3) / 3 - 3)

# height = 1.65 
# weight = 84
# bmi = weight / (height ** 2)
# print(int(bmi))
# print(round(bmi, 2))

# score = 0
# height = 1.8
# is_winning = True
# print(f"Your score is = {score}, your height is = {height}. You are winning is {is_winning}")

# DAY 2 - PROJECT
print("Welcome to the tip calculator!\n")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_to_split_bill = int(input("How many people to split the bill? "))
tip_percentage = (tip / 100) + 1
calculation = (total_bill / people_to_split_bill) * tip_percentage
final_result = round(calculation, 2)

print(f"Each person sould pay: ${final_result}")
