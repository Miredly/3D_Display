import arduinoserial
from time import sleep
from random import randint


arduino = arduinoserial.SerialPort("/dev/cu.usbmodem141411", 115200)
# print arduino.read_until('\n')

xpol = True
ypol = True
zpol = True

xpos = 0
ypos = 3
zpos = 2

def check_pol(pos, pol):
	if(pos == 7):
		pol = False
	if(pos == 0):
		pol = True
	return(pol)


def move_pos(pos, pol):
	# print("POL: " + str(pol))
	# print("POS: " + str(pos))
	if(pol == True):
		pos += 1
	if(pol == False):
		pos -= 1
	# print("NEW POS: " + str(pos))
	return(pos)

while(True):
	# loopstart = raw_input("STARTING THE LOOP!")
	xyzpos = []
	print("XPOS: " + str(xpos))
	xpol = check_pol(xpos, xpol)
	xpos = move_pos(xpos, xpol)

	print("YPOS: " + str(ypos))
	ypol = check_pol(ypos, ypol)
	ypos = move_pos(ypos, ypol)

	xyzpos.append(xpos)
	xyzpos.append(ypos)
	xyzpos.append(zpos)

	xyzout = str(xyzpos[0]) + str(xyzpos[1]) + str(xyzpos[2])
	# writingxyz = raw_input("Time to write!")
	print("WRITE: " + str(xyzout))
	# arduino.write("2 2 2")
	arduino.write(str(xyzpos[0]))
	# sleep(0.1)
	arduino.write(str(xyzpos[1]))
	# sleep(0.1)
	arduino.write(str(xyzpos[2]))
	sleep(0.2)
	# print("READ: " + str(arduino.read_until('\n')))
	# readingxyz = raw_input("Time to read!")
	