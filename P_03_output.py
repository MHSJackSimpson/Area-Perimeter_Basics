# ask the user for their name
username = input("What's your name?")
print()
# ask the user for their favourite number (integer)
fav_num = int(input("What's your favourite number?"))
print()
# Double, halve and square the user's favourite number
double = fav_num * 2
Halve = fav_num / 2
Square = fav_num ** 2

# Greet the user
print(f"Hello, {username}! Your favourite number is {fav_num}")
print()

# Output the results of doubling, halving and
# squaring their favourite number
print(f"{fav_num} Doubled is {double}, ")
print(f"Halve of {fav_num} is {Halve} and ")
print(f"{fav_num} Squared is {Square}!")
print()
print(f"Have a nice day, {username}!")