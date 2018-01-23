#!/usr/bin/python3

import socket, sys, struct, binascii

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("192.168.88.162", 22222)
print("Connecting to {} port {}".format(*server_address))
sock.connect(server_address)
print("Connected.")


# values = (56, 9, -300, 0, 0) # Find route to specified coordinate
values = (55, 9, 0, 0, 1) # Move to absolute coordinate, using backwards movement
print(values)
packer = struct.Struct(">B H i i B")
packed_data = packer.pack(*values)
print(packed_data)

try:
    print("Sending {!r}".format(binascii.hexlify(packed_data)))
    sock.sendall(packed_data)
finally:
    print("Closing socket")
    sock.close()
