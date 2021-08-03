#!/usr/bin/env python3

marvelchars= {
"starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"she-Hulk":
  {"real name": "jennifer walters",
  "powers": "super strength & intelligence",
  "archenemy": "Titania"}
             }

char_name = input(" Which character do you want to know about? (Starlord, Mystique, She-Hulk)").lower()

while marvelchars.get(char_name, "not exist") == "not exist":
  char_name = input(" Which character do you want to know about? (Starlord, Mystique, She-Hulk)").lower()

char_stat = input(" What statistic do you want to know about? (real name, powers, archenemy)")

while marvelchars.get(char_name).get(char_stat, "not exist") == "not exist":
  char_stat = input(" What statistic do you want to know about? (real name, powers, archenemy)")

if char_stat == "real name":
  value = marvelchars.get(char_name).get(char_stat).title()
else:
  value = marvelchars.get(char_name).get(char_stat)
print(f"{char_name.title()}'s {char_stat} is : {value}")
