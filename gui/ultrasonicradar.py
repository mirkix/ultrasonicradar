import numpy as np
import matplotlib.pyplot as plt
import serial

# Open serial interface
ser = serial.Serial('/dev/ttyACM0', 115200)

# 8 bars
N = 8

# Create 8 bars, 45 degrees each
theta = np.linspace(0.0 - (np.pi / 8), 2 * np.pi - (np.pi / 8), N, endpoint=False)

# Result 0cm
radii = [0, 0, 0, 0, 0, 0, 0, 0]
width = np.pi / 4

# Create plot
ax = plt.subplot(111, projection='polar')

while 1:
	# Start measurement
	ser.write(b'p')

	# Read result
	line = ser.readline()

	# Split string into values
	sonicrange = line.split(',')
	for i in xrange(len(sonicrange)):
		radii[i] = float(sonicrange[i])

	# Clear plot
	ax.clear()

	# Create new plot
	ax = plt.subplot(111, projection='polar')
	
	# North up	
	ax.set_theta_zero_location('N')

	# Theta increases in the clockwise direction
	ax.set_theta_direction(-1)

	# Set range 0 to 256 cm	
	ax.set_ylim(0, 256)

	# Create bars for 0, 45, 90, 135, 180, 225, 270, 315 degrees
	ax.bar(theta, radii, width=width, bottom=0.0)
	
	# Wait
	plt.pause(0.01)

	# Draw
	plt.draw()
