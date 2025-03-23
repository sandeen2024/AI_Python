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

#scores in grade
score=int(input("Enter the score:"))
if(score>=90):
    print("Grade:A")
elif(score>=80):
    print("Grade:B")
elif(score>=70):
    print("Grade:C")
elif(score>=60):
     print("Grade:D")
else:
    print("Grade:E")
