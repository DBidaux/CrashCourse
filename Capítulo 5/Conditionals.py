cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

print("-----------------------------------------------------------------------------------------")

requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")

print("-----------------------------------------------------------------------------------------")

# Numerical comparison

answer = 17
if answer != 42:
    print("That is not the correct answer!")

print("-----------------------------------------------------------------------------------------")
# Multiple comparison
# AND Comparator
age_1 = 22
age_2 = 18
print(age_1 >= 21 and age_2 >= 21)
age_2 = 25
print(age_1 >= 21 and age_2 >= 21)

print("-----------------------------------------------------------------------------------------")

# OR Comparator
age_1 = 22
age_2 = 18
print(age_1 >= 21 or age_2 >= 21)
age_1 = 18
print(age_1 >= 21 or age_2 >= 21)

print("-----------------------------------------------------------------------------------------")

# Check value in list
requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toppings)
print("pepperoni" in requested_toppings)

print("-----------------------------------------------------------------------------------------")

# Check value not in list
banned_users = ["Andrew", "Carolina", "David"]
user = "Marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# 5-1
print("5-1")
car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Not reassigning the variable car
print("-----------------------------------------------------------------------------------------")

# 5-2
print("5-2")
bev = "Water"
print("Is the beverage == 'water'?")
print(bev.lower() == 'water')
print("Is the beverage =! 'tea'?")
print(bev != 'tea')

print("-----------------------------------------------------------------------------------------")

age = 19
if age > 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("You are too young to vote, sorry.")
    print("Please register to vote when you turn 18!")

age = 17
if age > 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("You are too young to vote, sorry.")
    print("Please register to vote when you turn 18!")

print("-----------------------------------------------------------------------------------------")

age = 17
if age < 4:
    print("Your admission cost is 0€")
elif age < 18:
    print("Your admission cost is 25€")
else:
    print("Your admission cost is 40€")

# More readable, can omit the last catchall else statement
age2 = 65
if age2 < 4:
    price = 0
elif age2 < 18:
    price = 25
elif age2 < 65:
    price = 40
elif age2 >= 65:
    price = 20
print(f"Your admission cost is {price}€.")

print("-----------------------------------------------------------------------------------------")

requested_toppings = ["Mushrooms", "Extra cheese", "Bacon"]
if "Mushrooms" in requested_toppings:
    print("Adding mushrooms")
if "Extra cheese" in requested_toppings:  # If use elif statement, doesn't work correctly
    print("Adding extra cheese")
if "Bacon" in requested_toppings:
    print("Adding bacon")
if "Pepperoni" in requested_toppings:
    print("Adding pepperon")
print("Your pizza is ready!.")

print("-----------------------------------------------------------------------------------------")

# 5-3
print("5-3")
alien_color = "green"
if alien_color == "green":
    print("You earned 5 points!")
if alien_color == "red":
    print("You earned 5 points!")

print("-----------------------------------------------------------------------------------------")

# 5-4
print("5-4")
alien_color = "yellow"
if alien_color == "green":
    print("You earned 5 points!.")
else:
    print("You earned 10 points!.")

alien_color = "green"
if alien_color == "green":
    print("You earned 5 points!.")
else:
    print("You earned 10 points!.")

print("-----------------------------------------------------------------------------------------")

# 5-5
print("5-5")
alien_color = "red"
if alien_color == "green":
    print("5 points!")
elif alien_color == "yellow":
    print("10 points!")
else:
    print("15 points!")

alien_color = "yellow"
if alien_color == "green":
    print("5 points!")
elif alien_color == "yellow":
    print("10 points!")
else:
    print("15 points!")

alien_color = "green"
if alien_color == "green":
    print("5 points!")
elif alien_color == "yellow":
    print("10 points!")
else:
    print("15 points!")

print("-----------------------------------------------------------------------------------------")

# 5-6
print("5-6")
age = 66
if age <= 2:
    print("It's a baby.")
elif 2 <= age <= 4:
    print("It's a toddler.")
elif 4 <= age <= 13:
    print("It's a kid.")
elif 13 <= age <= 20:
    print("It's teenager.")
elif 20 <= age <= 65:
    print("It's an adult.")
elif age > 65:
    print("It's an elder.")

print("-----------------------------------------------------------------------------------------")

# 5-7
print("5-7")
fav_fruits = ["kiwi", "banana", "mango"]
if "kiwi" in fav_fruits:
    print("You really love kiwis!")
if "orange" in fav_fruits:
    print("You really love oranges!")
if "banana" in fav_fruits:
    print("You really love bananas!")
if "mango" in fav_fruits:
    print("You really love mangos!")
if "apple" in fav_fruits:
    print("You really love apples!")

print("-----------------------------------------------------------------------------------------")








