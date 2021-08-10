#!/usr/bin/python3
  
# standard, don't need to install!
import argparse

# this object will hold all arguments the user passes in
parser_tool= argparse.ArgumentParser(description="Set hostname and IP address")

# acceptable values
hostnames= ["mtg","cisco"]

# add some arguments!
parser_tool.add_argument("hostname", choices=hostnames, help="This is the value we set for hostname")

# add an optional argument
parser_tool.add_argument("-ip", metavar="IPV4", default="192.1.1.1", help="'IPV4 address', like '127.1.0.1', etc.")

# have the parser obj turn all those arguments into variables
args= parser_tool.parse_args()
print(f"The hostname is {args.hostname}, the ip address is {args.ip} !")