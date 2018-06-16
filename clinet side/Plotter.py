import matplotlib.pyplot as plt
import serial
import sys, os, traceback, types
from Tkinter import *
import pylab

fig = pylab.gcf()
fig.canvas.set_window_title('Pulse')
master = Tk()
master.title("Pulse")
v = IntVar()


def LAN():
    ser = serial.Serial(str(e2.get()), 115200, timeout=5)
    import socket
    s = socket.socket()
    s.connect(('192.168.4.1', 4444))
    s.send("LAN")
    a1 = []
    a2 = []
    i = 0
    plt.ylabel('VOLTAG(1024=3.3V)')
    plt.xlabel('Time')
    for a in range(int(e1.get())):
        i = i + 1
        x = 1
        print(ser.readline())
        s.send("NOT")
        a1.append([int(ser.readline())])
        a2.append([i])
        plt.plot(a2, a1, 'b')
        plt.pause(0.0000001)

    plt.show()
    s.close()


def NET():
    import socket
    s = socket.socket()
    s.connect(('192.168.4.1', int(e2.get())))
    a1 = []
    a2 = []
    i = 0
    plt.ylabel('VOLTAG(1024=3.3V)')
    plt.xlabel('Time')
    for a in range(int(e1.get())):
        i = i + 1
        x = 1
        u = s.recv(1024)
        s.send("NOT")
        a1.append([int(u)])

        plt.plot(a2, a1, 'b')
        plt.pause(0.0000001)

    plt.show()


Label(master, text="time :").grid(row=3, column=0)
Label(master, text="Port :").grid(row=4, column=0)
Label(master, text="Choose Option :").grid(row=5, column=0)
Radiobutton(master, text="WIFI", variable=v, value=1, command=NET).grid(row=6, columns=1)
Radiobutton(master, text="Serial", variable=v, value=2, command=LAN).grid(row=6, columns=2)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=3, column=1)
e2.grid(row=4, column=1)

Button(master, text='Start', command=NET).grid(row=3, column=2, ipadx=2, ipady=2, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=3, column=3, ipadx=2, ipady=2, sticky=W)

mainloop()


