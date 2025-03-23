def medicine_eligibility(age, weight):
    if age < 18 and weight < 55:
        return  "Sorry,This medicine cannot be given to you."
    elif weight >= 55 and age >= 18:
       return "Here is your medicine. Get well soon!"
    else:
       return "Sorry,This medicine cannot be given to you."
age = int(input("Please enter your age: "))
weight = int(input("weight(kg): "))
result = medicine_eligibility(age, weight)
print(result)
