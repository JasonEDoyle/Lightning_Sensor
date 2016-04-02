#!/usr/bin/python

import smbus


bus = smbus.SMBus(1)

ADDRESS = 0x03

# Regester Addresses
DISTANCE = 0x07


def lightning_distance():
	dist = bus.read_byte(ADDRESS, DISTANCE)
	return dist

if __name__ == '__main__':
	print lightning_distance()
	