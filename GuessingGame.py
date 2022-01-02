import random

top_of_range = input("Type an number: ")

if top_of_range.isdigit():
  top_of_range = int(top_of_range)

  if top_of_range <= 0:   
    print("Type an number larger than 0 next time -_-")
    quit()
else:
  print("Type an number next time -_-")
  quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
  guesses += 1
  user_guess = input("Make a guess (type da random number): ")
  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:
    print("Type an number next time -_-")
    continue
  
  if user_guess == random_number:
    print("You got it ma boah!")
    break
  else:
    if user_guess > random_number:
      print("You were above da number!")
    else:
      print("You were below da number!")

print("My Boah you got it in", guesses, "guesses")