age = int(input("Please enter your age: "))
nationality = input("Are you a citizen? (yes/no): ").lower()
if age < 18:
    print("Wait until you are of 18.")
elif nationality == "yes" and age >= 18:
    print("Congratulations! You have right to vote.")
else:
    print("Sorry, you have not met the requirements.")
