print("Metal Gear Solid" )
print('Snake has to carry out a stealth mission by getting to the elevator without being seen by the enemy. He must not kill the guard through fear another guard might discover the body. There will be many obstacles he will need to overcome along the way' )

print("Welcome to Shadow moses This is a Black ops stealth mission no one will be coming to assist you ")

print("Theres a guard up ahead")

choice1 = str(input("Please confirm which turn you want to take by typing left or right ")).lower()

if choice1 == "left":
  print("Nice found a cardboard box to hide in!")
else:
    print("Alert discovered by the guard SNAKE SNNNAAAKEEE! Game Over")

choice2 = str(input("Should I Crawl or hide to sneak past the enemy up ahead? Please type crawl or hide ")).lower()

if choice2 == "crawl":
  print("Phew got past the guard")
else:
  print("Huh was that box moving? Lifts up box ALert Whos that! SNAKE SNNNNAAAKKKE Game Over!")

choice3 = input("The Elevators just ahead theres two rooms to enter. Which one should i enter? Please type left or right ").lower()

if choice3 == "left":
  print("Whats this? A Socom with a silencer this wil sure come in handy")
else:
  print("Huh whos that! Alert Game Ovver you were discovered!")

  print(" Alert Alert The elevator has just arrived!")

print("Oh no theres a guard in direct path to the elevator")

choice4 = str(input("Should I shoot him or should knock on the wall to distract him? Please type shoot or knock  ")).lower()

if choice4 == "knock":
  print("Guard moves towards knocking noise. Huh what was that noise? hmm must be my mind playing games with me")
else:
  print("Guard down! Take him out. Game Over")

print("Path is now clear towards Elevator. But i can hear someone closely approaching")

choice5 = str(input("Should I dart for the lift before he comes? Please type enter or wait ")).lower()

if choice5 == "enter":
  print("Im in the lift now progressing to the next level. Well Done Level complete ")
else:
  print("Huh WHOS THAT! SNAKE SNNNAAAKEE! Game over!")

