                               WolfMixer V0.8
                                 11/05/2017
Copyright (C) 2015, 2016, 2017 Roy Leith


This program is distributed under the terms of the 
GNU General Public License V3
See http://www.gnu.org/licenses/lgpl.txt


BACKGROUND

Wolfson produced a sound card for the Raspberry Pi and an SD card 
Raspbian image with the drivers compiled into the kernel. 
The driver controls appeared in the Raspbian 'amixer' program and 
in the 'alsamixer' graphical representation, but included over 400 
controls in total. This defeated the GUI mixer and made it hard to
use the card without using the scripts supplied by Cirrus. 

My first mixer was based on this image and showed that the 'minor' input
volume controls were best set to maximum for lowest noise 
(the default setting in the image) and the 'minor' output volumes to 
'32' (which is around 0dB giving a modest amount of headroom).

WOLFMIXER v0.8

Wolfmixer v0.8 updates the control names and IDs used by
Matthias "Hias" Reichl's updated driver 

http://www.horus.com/~hias/cirrus-driver.html

in the driver tree of kernel 4.9 and later. It uses Hias' procedure of muting 
output ports during re-patching input ports and then unmuting. The SPDIF IN
and SPDIF OUT switches have been removed as the driver manages routing, itself.


WOLFMIXER v0.7

Wolfmixer v0.7 updates the control names used by the driver in the 
driver tree of kernel 3,18 and later. In other respects it is the 
same as v0.6.

WOLFMIXER v0.6

Wolfmixer V0.6 sets the 'minor' volume settings to maximum for the 
input channels (Line In, DMIC and Headset Mic) and to 0dB 
(the highest output channel setting with headroom to spare) 
for the output channels (Line Out, Headset and Speaker). 
There are no controls for these settings in the WolfMixer GUI.

By default, V0.6 inserts a High-pass Filter whenever an output 
channel is connected to DMIC or Headset Mic. 

Note: A filter is not inserted for Line In. If you are using Line In 
with Mic Bias and electret microphones then you should use the scripts 
provided by Cirrus. If there is a demand for it, I will add the feature 
to the next version of the mixer.

THE FUTURE

I may extend Wolfmixer to include the equalisers and the 
dynamic compressors. 

It is less likely that I will add the ability to mix four inputs on one 
output channel because of the required size of the mixer window. 
Technically, it is not a complex addition.

I will also consider a 'precompiled' version to speed the program 
startup.

WHAT YOU GET

* wolfmixer.py, WolfMixer (this is a desktop icon file. Raspbian displays 
it with the icon name and not the file name of wolfmixer.desktop)

* WolfMixer.png (the picture file for the icon)

* WolfMixer (actual filename: wolfmixer.desktop)

* this README.txt file.

SETTING UP

Some of the files need to be copied into protected 'System' folders.
Launch a special version of File Manager which has authority to do this
by typing the following into Terminal.

sudo pcmanfm

Please copy the wolfmixer.py files into a /home/pi/Programs/Wolfmixer 
directory. This file can then be run as follows. Point the file manager 
to this directory and choose 'Open Current Folder in Terminal' 
in the Tools menu. Type the following into Terminal (after the '$' 
prompt),

pi@raspberrypi ~/Programs $ python wolfmixer.py

The program will, probably, report missing modules, in particular the 
Pwm module (The rest are usually installed, by default).

Install the missing module(s) with,

  pi@raspberrypi ~/Programs $ sudo apt-get install python-pmw
   <any other missing modules>

The program 'wolfmixer.py'is a text file. You can open it with Leafpad 
and see which modules are loaded towards the beginning of the file.

  from Tkinter import *
  import Pmw, subprocess, os

In addition to wolfmixer.py, there is a a 'desktop' file, to launch the
program by clicking on an icon.

  wolfmixer.desktop.

As with all desktop files, it appears in the file manager as 'WolfMixer'
although you won't see the correct icon at this stage. Copy this 
file to /usr/share/raspi-ui-overrides.

Copy WolfMixer.png to 
/usr/share/icons/Adwaita/scalable/devices
/usr/share/applications
/home/pi/.local/share/applications


MENU ITEMS

It is convenient to have the program(s) in the Application Menu and
as Application Launcher icons in Panel. Once the files are in the 
correct folders, restart the Raspi. Running Preferences/Main Menu Editor
Should make the program appear under the 'Audio & Video' category.

Make sure that the entry is ticked. Also tick Logout in the Other 
category. Doing this does not guarantee that they appear in the menu!
Sometimes moving them to the top of the list in the menu editor will 
do the trick. Sometimes a restart will do it. It is flakey!
As a final suggestion, try renaming
 
lxde-pi-applications.menu in /home/pi/.config/menus/ to 
lxde-pi-applications.menu.old
and reboot.

I add an Application Launcher at the right-hand end of the Panel and
add Logout to it. Then I put another AL next to the Loudspeaker icon
and add WolfMixer to it.

IN USE

To use the Wolfson or Cirrus audio card in Raspbian, right-click on 
the loudspeaker icon in the System Tray and select RPi-Cirrus.

On startup, WolfMixer collects the settings that it finds in alsamixer 
and adjusts its controls to those settings. If you have not made any 
changes, yourself, the settings in the newly installed Cirrus driver 
are a good place to start. If you have already experimented with 
alsamixer and the amixer command-line scripts then those initial 
settings will have been lost.

Whatever you change in the mixer is saved by alsamixer and will remain 
as the new default setting even if you reboot the Raspi.

When you select DMIC or Headset Mic as an input, the input selection 
button will show those as being set. However, in the background, 
a high-pass filter has been inserted and the next time you start 
WolfMixer it will display LHPF rather than DMIC or Mic. 
The patch has not been changed.

Some controls may not work correctly. This is something to do with the 
driver implementation and its interaction with alsa. If you get no 
sound, try turning the mute button 'on' then 'off'. Sometimes the 
driver or the audio program get in a tizzy. Reboot the Raspi. These
issues may have been resolved in the current driver.

I have given AIF1 and AIF2 explanatory names. The 'RECORD' channel will 
present any connected Cirrus input port to the Raspberry Pi for use in 
an audio recording program such as Audacity. Connecting PLAY to an 
output channel will connect the Raspberry Pi audio playback to that 
output port. The Raspberry Pi playback volume cannot be adjusted by 
WolfMixer or alsamixer. Use the panel app. You may find erroneous 'Mute'
 indications in the app, but it does not seem to affect playback.

README.txt, Version 5, 15/05/2017
