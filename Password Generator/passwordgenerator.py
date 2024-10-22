import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Generiere dein neues Passwort!\n")
nr_letters = int(input("Wie viele Buchstaben sollen vorkommen?\n"))
nr_symbols = int(input("Wie viele Symbole sollen vorkommen?\n"))
nr_numbers = int(input("Wie viele Zahlen sollen vorkommen?\n"))


password = ""

for char in range(1, nr_letters + 1):
  password += random.choice(letters)

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)

randompassword = "".join(random.sample(password,len(password)))

print("Dein generiertes Passwort lautet:\n")
print(randompassword)

with open("passwort.txt", "w") as text_file:
  print(f"Dein generiertes Passwort lautet: {randompassword}", file=text_file)