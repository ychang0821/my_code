#!usr/bin/python3

import os
import subprocess

os.system("sudo apt install sl")

directory = "slappy"

parent_dir = "/home/student/mycode"

path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)

