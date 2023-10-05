print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇

print("Welcome to Treasure Island.Your mission is to find the treasure.")

choice1 = input('We have come across a junction with two dark caves to the left and the right and you need to decide where you want to go by typing "Left" or "Right" ').lower()
if choice1 == "left":
#Continue in the game.
  choice2 = input('You\'ve come to a lake. There is an Island in the middle of the lake. Type\"wait" to wait for a boat. Type "Swim" to swim across').lower()
  if choice2 == "wait":
  #Game will continue
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
    if choice3 == "red":
      print("Its a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You win you've found the treasure")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
  else:
    print("You got attacked by a shark.")
else:
  print("Fall into a hole.Game Over.")
  