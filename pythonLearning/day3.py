# #booleans-BELLLRINGER

# print(10 > 9) # is this true or false
# # booleans are used to evaluate expressions and conditions in python
# # they are used to check if an experession is true or false
# broughtFood = True
# print(broughtFood)

# is_raining = True
# if is_raining:
#     print("Take an umbrella!")
# else:
#     # print("No umbrella needed.")

#EVERYTHING BELOW IS THE VIDEO TUTORIAL

#lesson-1 booleans
temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

#lesson-2 easier and neater code

age = 12
if age >= 18:
    message = "Eligible"
else: 
    message = "Not Eligible"

message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

#lesson-3 logical operators

#operators are "not" "or" and "and"
high_income = False
good_credit = True
student = True
if high_income or good_credit or not student:
    print("Eligible")
else:
    print("Not Eligible")

#lesson-4 short-circuit evaluation/ ITS THE SAME PARAGRAPH OF CODE, LESSON 3 BUT CONTINUED

#lesson-5 chaining comparision operators
# age should be between 18 and 65
age = 22
if 18 <= age < 65:
    print("Eligible")

#lesson-6 quiz
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

    #the letter c will be printed in the terminal