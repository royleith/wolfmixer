#  wifictrl V0.2
#  Copyright (C) 2016 Roy Leith
#
#  This program is distributed under the terms of the GNU General Public License V3
#      see http://www.gnu.org/licenses/lgpl.txt
#
#  It turns the Raspberry Pi 3 wlan0 'on' and 'off'. wlan0 should be 'off' if you are 
#  using Bluetooth audio.
#
#  You may need to install the Python module Pmw
#  sudo apt-get install python-pmw

from Tkinter import *
import os, time
root = Tk()
root.title('WiFi')


def wlan0OFF():
	os.system("sudo ifconfig wlan0 down")
	p = os.popen('cat /sys/class/net/wlan0/operstate',"r")
	statusvar.set(p.readline())

def wlan0ON():
	os.system("sudo ifconfig wlan0 up")
	time.sleep(2)
	p = os.popen('cat /sys/class/net/wlan0/operstate',"r")
	statusvar.set(p.readline())

Label (root, text='wlan0 Status:', font=('arial', 12, 'bold')).grid(row=0, column=0)

statusvar = StringVar()
status = Label(root, width = 8, textvariable=statusvar, font=('arial', 16, 'bold'), justify = LEFT).grid(row=1, column=1)

Button(root, text="OFF", borderwidth=2, width=5, command=wlan0OFF).grid(row=2, column=1)
Button(root, text="ON", borderwidth=2, width=5, command=wlan0ON).grid(row=2, column=2)

p = os.popen('cat /sys/class/net/wlan0/operstate',"r")
statusvar.set(p.readline())


root.mainloop()
