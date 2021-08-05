#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# python3 -m pip install crayons
import crayons

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') # fstring with RED
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

#function to loop lists of ips
def devicerboot(iplist):
    for ip in iplist:
        print(f"Connecting to {ip}, REBOOTING NOW!")

# start our main script
def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    iplist = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
    print(f"Welcome to the {crayons.blue('Network')} Device Command Pusher") # welcome message with blue text

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices
    devicerboot(iplist) # call function to iterate the list IPS
# call our main function
main()

