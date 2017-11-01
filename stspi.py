#!/usr/bin/env python
# coding: Latin-1

# import stuff

from inputs import get_gamepad
import explorerhat

# motor things

motorleft = 0
motorright = 0

# the main loop
	
while True:

# see the control stick

	events = get_gamepad()
	for event in events:
		print(event.ev_type, event.code, event.state)

# calibrate the sticks to read zero when in the center and store values in the motorleft/right things above

		if event.code == "ABS_Y":
			motorleft = event.state - 128

		if event.code == "ABS_RZ":
			motorright = event.state - 128

# limit the left motor to + or - 100
		
		if motorleft >= 0:
			if motorleft >= 100:
				motorleft = 100
			
		if motorleft <= 0:
			if motorleft <= -100:
				motorleft = -100

# limit the right motor to  + or - 100
		
		if motorright >= 0:
			if motorright >= 100:
				motorright = 100

		if motorright <= 0:
			if motorright <= -100:
				motorright = -100

# power the motors with the values in the motorleft/right things above

	explorerhat.motor.one.speed(motorleft)
	explorerhat.motor.two.speed(motorright)
