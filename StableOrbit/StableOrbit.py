import arduinoserial
from time import sleep
from random import randint

"""
for some reason the arduino assigns itself a new serial port number every time 
it gets plugged in. You'll need to make sure this matches. Also, the baud rate 
must be the same on the python side as the arduino side.
"""

arduino = arduinoserial.SerialPort("/dev/cu.usbmodem47", 115200) 

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

	if(pol == True):
		pos += 1
	if(pol == False):
		pos -= 1
	return(pos)

step = 1

while(True):
	# loopstart = raw_input("STARTING THE LOOP!")
	if (step > 14):
		step = 1

	xyzpos = []
	
	if(step != 14):

		xpol = check_pol(xpos, xpol)
		xpos = move_pos(xpos, xpol)
		print("XPOS: " + str(xpos))

		ypol = check_pol(ypos, ypol)
		ypos = move_pos(ypos, ypol)
		print("YPOS: " + str(ypos))

	

	if(step % 2 == 0):
		if(zpos == 5):
			zpol = False
		if(zpos == 1):
			zpol = True
		zpos = move_pos(zpos, zpol)

	xyzpos.append(xpos)
	xyzpos.append(ypos)
	xyzpos.append(zpos)

	xyzout = str(xyzpos[0]) + str(xyzpos[1]) + str(xyzpos[2])
	# writingxyz = raw_input("Time to write!")
	print("WRITE: " + str(xyzout))
	arduino.write(str(xyzpos[0]))
	arduino.write(str(xyzpos[1]))
	arduino.write(str(xyzpos[2]))
	sleep(0.040) #This needs to be significantly higher than the delay times on the Arduino side or else it gets ahead of itself

	step += 1