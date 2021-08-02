#!/usr/bin/env python3

# Create a list containing three items
my_list = [ "192.168.0.5", 5060, "UP" ]

# Print IP address(first item) in my_list
print("The first item in the list (IP): " + my_list[0] )

# Print port number(second item) in my_list
print("The second item in the list (port): " + str(my_list[1]) )

# Print the state(third item) in my_list
print("The last item in the list (state): " + my_list[2] )

# Display only the IP addresses to the screen
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print(f"IP addresses: {iplist[3]}, and {iplist[4]}")
