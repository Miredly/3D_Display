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
		# zpol = check_pol(zpos, zpol)
		zpos = move_pos(zpos, zpol)

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
	sleep(0.040) #This needs to be significantly higher than the delay times on the Arduino side or else it gets ahead of itself
	# print("READ: " + str(arduino.read_until('\n')))
	# readingxyz = raw_input("Time to read!")
	# breakpoint = raw_input("BREAK " + str(step))
	step += 1