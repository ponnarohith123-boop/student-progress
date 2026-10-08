import random
while True:
  secret = random.randint(1, 100)
  attempts = 0
  while True:
    guess = int(input("Guess a number b/w 1 to 100: "))
    attempts = attempts + 1
    if(guess > secret):
      print("Your guess is too high")
    elif (guess < secret):
      print("Your guess is too low")
    else:
      print("Congratulations ! ")
      break

  print(f"You got in {attempts} attempts")

  play = input("Do you want to play again (y/n): ")
  if(play.lower() != "y"):
    print("Thanks for playing")
    break
