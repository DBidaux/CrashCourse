# Loops
magos = ["Elena", "Carolina", "David"]
for mago in magos:
    print(f"{mago}, that was a great trick!.")
    print(f"I can't wait to see your next trick, {mago}!.\n")
print("Thanks everyone, that was a really good magic show!.")
print("-----------------------------------------------------------------------------------------------------------")
# 4-1
print("4-1")
pizzas1 = ["Carbonara", "Fugazzetta", "Pepperoni"]
for pizza in pizzas1:
    print(f"I like {pizza} pizza style.")
print("three lines....")

print("-----------------------------------------------------------------------------------------------------------")

# 4-2
print("4-2")
animals = ["Cat", "Tiger", "Lion"]
for animal in animals:
    print(f"A {animal} would be an amazing pet!.")
print("These animals have in common that they are felines!")

print("-----------------------------------------------------------------------------------------------------------")

# 4-3
print("4-3")
for value in range(1, 21):
    print(value)

print("-----------------------------------------------------------------------------------------------------------")

# 4-4
print("4-4")
# for value in range(1, 1000001):
#   print(value)

print("-----------------------------------------------------------------------------------------------------------")

# 4-5
print("4-5")
numbers = []
for value in range(1, 1000001):
    numbers.append(value)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print("-----------------------------------------------------------------------------------------------------------")

# 4-6
print("4-6")
for value in range(1, 21, 2):
    print(value)

print("-----------------------------------------------------------------------------------------------------------")

# 4-7
print("4-7")
triples = []
for value in range(1, 11):
    triples.append(value * 3)
for triple in triples:
    print(triple)

print("-----------------------------------------------------------------------------------------------------------")

# 4-8
print("4-8")
cubes = []
for value in range(1, 11):
    cubes.append(value ** 3)
for cube in cubes:
    print(cube)

print("-----------------------------------------------------------------------------------------------------------")

# 4-9
print("4-9")
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

print("-----------------------------------------------------------------------------------------------------------")

# 4-10
print("4-10")
list = ["bottle", "computer", "table", "station", "star"]
print("The three first items in the list are:")
for item in list[:3]:
    print(item)
print("The three middle items in the list are:")
for item in list[1:4]:
    print(item)
print("The three last items in the list are:")
for item in list[-3:]:
    print(item)

print("-----------------------------------------------------------------------------------------------------------")

# 4-11
print("4-11")
my_pizzas = ["Carbonara", "Fugazzetta", "Margherita"]
friend_pizzas = my_pizzas[:]
print(my_pizzas)
print(friend_pizzas)
my_pizzas.append("Kebab")
friend_pizzas.append("Speciale")
print(my_pizzas)
print(friend_pizzas)
print("My favorites pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("My friend's favorites pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

print("-----------------------------------------------------------------------------------------------------------")

# 4-12
print("4-12")
buffet = ("Macarrones", "Pollo", "Patatas", "Huevos fritos", "Hamburguesas")
for food in buffet:
    print(food)

buffet = ("Spaghetti", "Pollo", "Zanahorias", "Huevos fritos", "Pizzas")
for food in buffet:
    print(food)