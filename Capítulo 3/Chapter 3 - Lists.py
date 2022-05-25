# Lists
bikes = ["Trek", "Cannondale", "Redline", "Specialized"]
print(bikes)  # Print the whole list, even with the brackets
print("-----------------------------------------------------------------------------------------------------------")

print(bikes[0])  # Index starts at 0, not 1. Index -1 shows last item

print("-----------------------------------------------------------------------------------------------------------")

print(bikes[0].lower())  # Can use the methods (not usable with the full list, only items)

print("-----------------------------------------------------------------------------------------------------------")

message = f"My first bicycle was a {bikes[0].title()}"
print(message)

print("-----------------------------------------------------------------------------------------------------------")

for item in bikes:
    print(item)
print("-----------------------------------------------------------------------------------------------------------")

# 3-1
print("3-1")
friends = ["Jesús", "Alejandro", "Mariano"]  # With a loop for, less typing
for i in friends:
    print(f"Hello, {i}, I'm glad to see you!")
print("-----------------------------------------------------------------------------------------------------------")

# 3-2
print("3-2")
print(f"Hello, {friends[0]}, I'm glad to see you!")
print(f"Hello, {friends[1]}, I'm glad to see you!")
print(f"Hello, {friends[2]}, I'm glad to see you!")
print("-----------------------------------------------------------------------------------------------------------")

# 3-3
print("3-3")
motorbikes = ["Honda", "Yamaha", "Kawasaki"]
message = f"I'd love to own a {motorbikes[1]}, but my favorite is {motorbikes[2]}"
print(message)
print("-----------------------------------------------------------------------------------------------------------")

# Change, Add and Remove
# Change
print(motorbikes)
motorbikes[0] = "Ducati"
print(motorbikes)
print("-----------------------------------------------------------------------------------------------------------")
# Add
print(motorbikes)
motorbikes.append("Honda")
print(motorbikes)
print("-----------------------------------------------------------------------------------------------------------")

motorcycles = []
motorcycles.append("Honda")
motorcycles.append("Yamaha")
motorcycles.append("Kawasaki")
motorcycles.append("Ducati")
print(motorcycles)
print("-----------------------------------------------------------------------------------------------------------")

# Insert
print(motorcycles)
motorcycles.insert(0, "Suzuki")
print(motorcycles)
print("-----------------------------------------------------------------------------------------------------------")

# Remove
print(motorcycles)
del motorcycles[0]  # Del statement
print(motorcycles)
print("-----------------------------------------------------------------------------------------------------------")

print(motorbikes)
pop_motorbike = motorbikes.pop()  # Pop method delete the last item in the call-stake
print(motorbikes)
print(pop_motorbike)  # Can modify the popped item, with the index number
motorbikes.remove("Yamaha")
print(motorbikes)
print("-----------------------------------------------------------------------------------------------------------")

# 3-4
print("3-4")
people = ["Albert Einstein", "Ayrton Senna", "Christopher Nolan"]
for i in people:
    print(f"Hello dear {i}, would you like to join me this night to take a beer?")

print("-----------------------------------------------------------------------------------------------------------")

# 3-5
print("3-5")
print(people)
cant_come = people.pop(0)
print(cant_come)
people.insert(0, "Charles Darwin")
print(people)
for i in people:
    print(f"Hello dear {i}, you are cordially invited to take a beer tonight.")
print("-----------------------------------------------------------------------------------------------------------")

# 3-6
print("3-6")
print(f"Hello, I've found a bigger table, so I invite a few more.")
print(people)
people.insert(0, "Marie Curie")
people.insert(1, "Lidia Valentín")
people.append("Emily Blunt")
print(people)
for i in people:
    print(f"Hello dear {i}, you are cordially invited to take a beer tonight.")

print("-----------------------------------------------------------------------------------------------------------")

# 3-7
print("3-7")
print("Unfortunately, only two can come to have a beer, due to an overbooking")
print(people)
uninvited = people.pop()
print(f"I'm sorry, {uninvited}, the pub messed up the booking.")
print(people)
uninvited = people.pop()
print(f"I'm sorry, {uninvited}, the pub messed up the booking.")
print(people)
uninvited = people.pop()
print(f"I'm sorry, {uninvited}, the pub messed up the booking.")
print(people)
uninvited = people.pop()
print(f"I'm sorry, {uninvited}, the pub messed up the booking.")
print(people)
for i in people:
    print(f"Hello, my dear {i}, you are still invited to take a beer.")
del people[0]
print(people)
del people[0]
print(people)

print("-----------------------------------------------------------------------------------------------------------")

# Organizing a list
cars = ["BMW", "Audi", "Subaru", "Toyota", "Seat"]
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print("-----------------------------------------------------------------------------------------------------------")

# Temporarily sort w/ sorted() function

cars = ["BMW", "Audi", "Subaru", "Toyota", "Seat"]
print("Original list:")
print(cars)
print("\nHere is a sorted list:")
print(sorted(cars))
print("\nOriginal list again")
print(cars)
print("-----------------------------------------------------------------------------------------------------------")

# Reverse order
cars = ["BMW", "Audi", "Subaru", "Toyota", "Seat"]
print(cars)
cars.reverse()
print(cars)
print("-----------------------------------------------------------------------------------------------------------")

# Length
cars = ["BMW", "Audi", "Subaru", "Toyota", "Seat"]
print(len(cars))
print("-----------------------------------------------------------------------------------------------------------")

# 3-8
print("3-8")
places = ["Tokio", "Amsterdam", "New York", "Madagascar", "Noruega"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
print(places.reverse())
print(places)
print(places.reverse())
print(places)
print(places.sort())
print(places)
print(places.sort(reverse=True))
print(places)

print("-----------------------------------------------------------------------------------------------------------")

# 3-9
print("3-9")
people = ["Albert Einstein", "Ayrton Senna", "Christopher Nolan"]
print(len(people))
for i in people:
    print(f"Hello dear {i}, would you like to join me this night to take a beer?")

print("-----------------------------------------------------------------------------------------------------------")

# 3-10
moto = ["Suzuki", "Yamaha", "Honda"]
# print(moto[3])
print(moto[2])















