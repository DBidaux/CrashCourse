# Variables
message = "Hello world"
print(message)

message = "Hello world 2"
print(message)

# Name errors
mesage = "Hello world 3"
print(mesage)
print("-----------------------------------------------------------------------------------------------------------")
# Strings
"String"
'Also a string'

# Method
name = "jada lovepace"
print(name.title())  # First letter will become capital
name = "Kimmy Stewart"
print(name)
print(name.upper())
print(name.lower())  # For storing data

# Variables in strings
f_name = "jada"
l_name = "lovepace"
full_name = f"{f_name} {l_name}"  # F-strings
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"  # F-strings with variable
print(message)
print("-----------------------------------------------------------------------------------------------------------")
# Whitespace
print("Python")
print("\tPython")

# Newline
print("Languages:\nPython\nC\nJavaScript")

# Both things
print("Languages:\n\tPython\n\tC\n\tJavascript")
print("-----------------------------------------------------------------------------------------------------------")
# Stripping extra spaces
fav_lang = "Python "
print(fav_lang)
print(fav_lang.rstrip())  # Space at right
fav_lang = fav_lang.rstrip()
print(fav_lang)

fav_lang = " JavaScript"
print(fav_lang)
print(fav_lang.lstrip())  # Space at left
fav_lang = fav_lang.lstrip()
print(fav_lang)
print("-----------------------------------------------------------------------------------------------------------")
# Avoiding syntax errors with strings
message = "One of Python's strengths is its diverse community."
print(message)
# message = 'One of Python's strengths is its diverse community.'
# print(message)
print("-----------------------------------------------------------------------------------------------------------")
# Mini-exercises

# 2-1
print("2-1")
f_name = "Didier"
l_name = "Bidaux"
print(f"Hello {f_name} {l_name}, would you like to learn some Python today?")
print("-----------------------------------------------------------------------------------------------------------")

# 2-2
print("2-2")
f_name = "didier"
l_name = "bidaux"
print(f"{f_name} {l_name}".lower())
print(f"{f_name} {l_name}".upper())
print(f"{f_name} {l_name}".title())
print("-----------------------------------------------------------------------------------------------------------")

# 2-3
print("2-3")
print(
    "Orland Oxford once said " + "'Manners maketh men'" + "," + " making me to understand the importance of the good manners.")
print("-----------------------------------------------------------------------------------------------------------")

# 2-4
print("2-4")
famous_person = "Orland Oxford"
quote = "'Manners maketh men'"
message = f"{famous_person} once said " + f"{quote}" + "," + " making me to understand the importance of the good manners."
print(message)
print("-----------------------------------------------------------------------------------------------------------")

# 2-5
print("2-5")
name = " \tDidier \nBidaux "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
print("-----------------------------------------------------------------------------------------------------------")
