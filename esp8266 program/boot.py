
from machine import Pin,I2C
from time import *
import socket
import ADXL345
# I2C protocol used for reciveing data from ADXL345 sensor [pin(5) = D1 pin(4) = D2]
i2c = I2C(scl=Pin(5),sda=Pin(4), freq=10000)
adx = ADXL345.ADXL345(i2c)
addr = socket.getaddrinfo('0.0.0.0',4444)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(2)j
cl , addr = s.accept()
# serial connection and data sending
def serial():
	import machine
	from time import*
	import socket
	adc = machine.ADC(0)
	while True:
		z = adx.zValue
		print(z)	
		sleep_ms(400)
# WiFi connection and data sending
while True:
	z = adx.zValue
	cl.send(str(z))
	sleep_ms(400)
	u = cl.recv(1024)
	if u == b'LAN':
		break
serial()
