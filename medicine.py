age = int(input("Please enter your age: "))
weight = int(input("weight(kg): "))
if age < 15 and weight < 55:
    print("Sorry!This medicine can't be given to you.")
elif weight >= 55 and age >= 15 or 18:
    print("Here is your medicine. Get well soon!")
else:
    print("Sorry!This medicine can't be given to you.")
