#!/usr/bin/env python3

import random

icecream = ["flavors", "salty"]

tlgclass= ["Adrian","Bikash","Chas","Chathula","Chris","Hongyi","Jauric","Joe L.","Joe V.","Josh","Justin","Karlo","Kerri-Leigh","Jason","Nicholas","Peng","Philippe","Pierre","Stephen","Yun"]

random.shuffle(tlgclass)

icecream.append(99)

user_input = input("Please enter a number between 0 to 19: ")

if user_input.isdigit():

  input_int = int(user_input)
  print(f"{icecream[-1]} {icecream[0]}, and {tlgclass[input_int]} chooses to be {icecream[1]}.")
else:
   print(f"{icecream[-1]} {icecream[0]}, and {user_input} chooses to be {icecream[1]}.")
