#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)

# this line will add "dns" to the end of our list
proto.append("dns")

# this line will add "dns" to the end of our list
protoa.append("dns")
print(proto)

# a list of common ports
proto2 = [ 22, 80, 443, 53 ]

# pass proto2 as an argument to the extend method
proto.extend(proto2)
print(proto)

# pass proto2 as an argument to the append method
protoa.append(proto2)
print(protoa)

# insert element into proto and protoa lists
extra_proto = ["FTP", "SFTP"]
proto.insert(0, extra_proto[0])
print(proto)

protoa.insert(4, extra_proto[1])
print(protoa)
