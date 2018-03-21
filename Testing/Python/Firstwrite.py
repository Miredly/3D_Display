import serial
from time import sleep
from random import randint

port = "/dev/tty.usbmodem141411"
ard = serial.Serial(port,9600,timeout=5)

print(ard.name)


def set_Coords(x, y, z):
	ret_Coords = []

	ret_Coords.append(int(x))
	ret_Coords.append(int(y))
	ret_Coords.append(int(z))
	return ret_Coords

while(True):
	ard.flush()
	# output = randint(48, 55)
	# outputx = str(randint(49, 50))
	Coords = set_Coords(input("X: "), input("Y: "), input("Z: "))
	print("COORDS: " + str(Coords))

	ard.write(Coords[0])
	ard.write(Coords[1])
	# ard.write(Coords[2])
	print(ard.read(100))