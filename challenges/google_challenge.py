#!usr/bin/python3

import os
import subprocess

os.system("sudo apt install sl")

directory = "slappy"

parent_dir = "/home/student/mycode"

path = os.path.join(parent_dir, directory)
if not os.path.exists("/home/student/mycode/slappy"):
    os.mkdir(path)
f = open("/home/student/mycode/slappy/chad_stop_using_that_word.txt", "a")
f.close()
print("Directory '% s' created" % directory)

