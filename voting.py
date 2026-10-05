age = int(input("Enter your age: "))

if age < 0 or age > 100:
    print("Invalid age")

elif age >= 18:
    print("You are eligible for voting")

else:
    print("You are not eligible for voting")