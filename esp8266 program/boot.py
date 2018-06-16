
from machine import Pin,I2C
from time import *
import socket
import ADXL345

i2c = I2C(scl=Pin(5),sda=Pin(4), freq=10000)
adx = ADXL345.ADXL345(i2c)
addr = socket.getaddrinfo('0.0.0.0',4444)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(2)j
cl , addr = s.accept()
# serial connection data sending
def serial():
	import machine
	from time import*
	import socket
	adc = machine.ADC(0)
	while True:
		z = adx.zValue
		print(z)	
		sleep_ms(400)
# WiFi connectio data sending
while True:
	z = adx.zValue
	cl.send(str(z))
	sleep_ms(400)
	u = cl.recv(1024)
	if u == b'LAN':
		break
serial()
