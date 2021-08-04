#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginsuccessful = 0 # counter for successes

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            print(line.split(" ")[-1])
        # if above statement is false, then check
        elif "-] Authorization failed" in line:
            loginsuccessful += 1
print("The number of failed log in attempts is", loginfail)
print("The number of successful log ins is", loginsuccessful)
