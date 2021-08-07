#!/usr/bin/python3

import random

fuel_level = 20
#an rocksack, which is initially empty
rocksack = []
# unnecessary item list pool
item_list = ['water','coffee','rifle','camelbak','knife',
            'alexa echo','boots','tent','key','laptop',
            'asu','flashlight','food', 'pfizer vaccine','sword',
            'radio station']
# all required items
f_list = ['cac card', 'mre', 'ignition key', 'space suit', 'diaper']
new_list = f_list.copy()

#a dictionary linking a city to other cities
cities = {
            'Seattle' : {
                  'south' : 'Tacoma',
                  'east'  : 'Bellevue',
                  'north' : 'Lynwood',
                  'west'  : 'Bremerton',
                  'item'  : []
                },
            'Tacoma' : {
                  'north' : 'Seattle',
                  'south'  : 'JBLM',
                  'item'  : []
                },
            'Bellevue' : {
                  'west' : 'Seattle',
                  'item' : []
               },
            'Lynwood' : {
                  'south' : 'Seattle',
                  'item' : []
            },
            'Bremerton' : {
                  'east' : 'Seattle',
                  'item' : []
            },
           'JBLM' : {
                  'north' : 'Tacoma',
                  'item' : []
            },
         }

def showInstructions():
  #print a main menu and the commands
  print('''
F you COVID! Let's go to Mars!
In this game, you need to go to different cities to collect items to launch the rocket locate at JBLM to go to Mars. Your fuel level start at 20, each movement between cities will cost 1 point of fuel. If the fuel level is 0, game will be terminated. You can collect at most 10 items. You need 5 necessary items to launch the rocket. Good luck!! 
========
Commands:
  go [direction]
  get [item]
  drop [item]
  map
''')

def showStatus():
  print('---------------------------')
  getMap()
  print('Your fuel level is ' + str(fuel_level))
  print('You are in the ' + currentCity)
  print('Rocksack : ' + str(rocksack))
  #print an item if there is one
  if "item" in cities[currentCity]:
    print(f"You see a {cities[currentCity]['item']}")
  print("---------------------------")

def itemInit(city):
  random.shuffle(item_list)
  random.shuffle(new_list)
  
  for i in range(3):
    cities[city]['item'].append(item_list.pop())
  cities[city]['item'].append(new_list.pop())
  random.shuffle(cities[city]['item'])

def launch():
  
  for item in f_list:

    if item in rocksack:
      continue
    else:
      return False  
  return True

def show_map():
  for key in cities[currentCity]:
    if key != "item":
      print(f"{key} : {cities[currentCity][key]}")

def getMap():
  map = {
    "Lynwood": "              ",
    "Seattle": "               ",
    "Bellevue": "              ",
    "Bremerton": "                ",
    "Tacoma": "              ",
    "JBLM": "              "
  }
  for key in map:
    if key == currentCity:
      map[key] = "You are Here!"
  
  print(f"""
                                             N
                                             ↑
                                         W ← + → E
                                             ↓
                   LYNWOOD                   S
                 {map["Lynwood"]}

BREMERTON          SEATTLE       BELLEVUE  
{map["Bremerton"]}{map["Seattle"]}{map["Bellevue"]}

                   TACOMA            
                {map["Tacoma"]}             

                    JBLM           
                {map["JBLM"]}
  
  """)

def spaceship():
  print("""
           
     |    
    / \   
   |--o|
   |---|  
  /     \ 
 | U     |
 | S     |
 | A     | 
 |_______| 
  |@| |@|  
 ./@\./@\.
  ||| |||
  ||| |||
  """)

def dead():
    print("""
          .---.
        ./     \.
        ( () () )
         \  M  / 
          |HHH|
          '---'
Sucker... you run out of fuel!
💀💀💀💀GAME OVER!💀💀💀💀
""")

  
showInstructions()

itemInit('Seattle')
itemInit('Tacoma')
itemInit('Bellevue')
itemInit('Bremerton')
itemInit('Lynwood')

#start the player in the 'Seattle'
currentCity = 'Seattle'

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')
   
  move = move.lower().split(" ", 1)

  if (move[0] != 'go' or move[0] != 'get' or move[0] != 'drop') and len(move) == 1:
    print('Bad input, please use a legit command')
  #if they type 'go' first
  elif move[0] == 'go':
    if move[1] in cities[currentCity]:
      currentCity = cities[currentCity][move[1]]
      fuel_level -= 1
    else:
        print('You can\'t go that way!')

  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if len(rocksack) > 10:
      print('Full rocksack, Can\'t get ' + move[1] + '!' + 'drop something first')

    elif "item" in cities[currentCity] and move[1] in cities[currentCity]['item']:
      #add the item to their rocksack
      rocksack += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      cities[currentCity]['item'].remove(move[1])
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  if move[0] == 'drop':
    if move[1] in rocksack:
      cities[currentCity]['item'].append(move[1])
      print(move[1] + ' drop!')
      rocksack.remove(move[1])
    else:
      #tell them they can't get it
      print('Can\'t drop ' + move[1] + '!')
      

  if move[0] == 'map':
    show_map()
  ## Define how a player can win

  if currentCity == 'JBLM':
    launchable = launch()
    if launchable == True:
      spaceship()
      print('Congratulations! You collected all the items you need to go to Mars!! Enjoy the trip!! ')
      break
    else:
      print("You don't have all the necessary items to launch the rocket")

  elif fuel_level == 0:
    dead()
    break