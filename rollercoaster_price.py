print("Welcome to rollercoaster ride!")
height = float(input("Enter your height in cm: "))
bill = 0
if height > 120:
    print("You can ride")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
    elif age < 18:
        bill = 7
    if age >= 45 and age <= 55:
        print("Enjoy the free Ride.")
    elif age >= 18:
        bill = 12
    wants_photo = input("Do You wants photo. Type y for yes and n for no: ")
    if wants_photo == "y":
        bill += 3

    print(f"You have to pay ${bill}")
else:
    print("Grow up to ride")
