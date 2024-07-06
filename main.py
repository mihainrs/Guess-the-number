import random

random_number = random.choice(range(0,10))

print("Welcome to the random guesser! The game's fairly simple; guess any number from 0 to 9 and win!")

start = True

while start:
   answer= input("Choose a number between 0 to 9: ")
   if answer.isdigit():
    if answer < "0" and answer > "9":
      print("Be sure to type any number between 0 and 9")
    else:
      if answer == random_number:
         print("CORRECT!")
         print("\n")
         print("You win!")
         start=False
      else:
         print("WRONG!")
         print("\n")
         print("You lost!")
         start=False
      replay = input("Would you like to play again? ")
      if replay == "yes":
         start=True
      elif replay == "no":
         print("Game over!")
         break
      else:
         try_again = input("Please type either 'yes' or 'no' ")
         if try_again == "yes":
            start = True
         else:
          print("Game over!")
          break
   else:
      print("Please input a number!")
