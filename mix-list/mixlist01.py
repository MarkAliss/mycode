#!/usr/bin/env python3

# my_list items
my_list = ['192.168.0.5', 5060, 'UP']

# print slice 0
print('The first item in the list (IP): ' + my_list[0] )

# print slice 1
print('The second item in the list (port): ' + str(my_list[1]) )

# print slice 2
print('The last item in the list (state):' + my_list[2] )

# given the new list, display only the IP addresses on the screen
iplist = [ 5060, '80', 55, '10.0.0.1', '10.20.30.1', 'ssh' ]

# printing only the IP addresses by slicing
print('The IP addresses are: ' + iplist[3] + ', ' + iplist[4])
