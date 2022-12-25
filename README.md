                               WolfMixer V0.8
                                 25/12/2022
Copyright (C) 2015, 2016, 2017, 2022 Roy Leith


This program is distributed under the terms of the 
GNU General Public License V3
See http://www.gnu.org/licenses/lgpl.txt


BACKGROUND

Wolfson (later, Cirrus Logic) produced a sound card for the Raspberry Pi and an SD card 
Raspbian image with the drivers compiled into the kernel. 
The driver controls appeared in the Raspbian 'amixer' program and 
in the 'alsamixer' graphical representation, but included over 400 
controls in total. This defeated the GUI mixer and made it hard to
use the card without using the scripts supplied by Cirrus. 

My first mixer was based on this image and showed that the 'minor' input
volume controls were best set to maximum for lowest noise 
(the default setting in the image) and the 'minor' output volumes to 
'32' (which is around 0dB giving a modest amount of headroom).

All versions up to 2.8 were written for Python2.7. Version 2.9 is a rewrite for 
Python 3.9 and above.

HISTORY

WOLFMIXER v0.9

Rewritten for Python 3.9 and above. Raspberry Pi OS defaults to Python 3.11 at the time
of this version and so it can be run with python wolfmixer.py or python3 wolfmixer.py.

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

WHAT YOU GET

* wolfmixer.py, the python language program file.

* WolfMixer.png (the picture file for the icon)

* __init__.py (an empty file that may help python to select paths to the program.

* this README.txt file.

SETTING UP

Please create the folder,

    /home/<yourusername>/Programs
    
If your user name is pi then the folder would be,

    /home/pi/Programs
    
Then copy the wolfmixer.py and WolfMixer.png files into the folder.
The wolfmixer.py file can then be run as follows. Navigate the file manager 
into the directory and choose 'Open Current Folder in Terminal' 
in the Tools menu. Type the following into Terminal (after the '$' 
prompt),

    python wolfmixer.py

The program will, probably, report missing modules, in particular the 
Pwm module (The rest are usually installed, by default).

Install the missing module(s) with,

  sudo pip3 install pmw

The program 'wolfmixer.py'is a text file. You can open it with mousepad 
and see which modules are loaded towards the beginning of the file.

  from tkinter import *
  import Pmw, subprocess, os

MENU ITEMS

Create an icon to start the program.

In the applications menu: Preferences/Main Menu Editor choose your Catagory 
on the left (Sound & Video?) and click on New Item.

In 'Name' type 'WolfMixer.

In 'Command' type 

    python /home/<yourusername>/Programs/wolfmixer.py

In 'Comments' type a description, say 'Cirrus Logic Mixer'.

Click on the icon area. You will be asked for an icon file. Browse to 
/home/<yourusername>/Programs and select,

    WolfMixer.png
    
Save the changes and close the editor.

Reboot and then go to Preferences/Main Menu Editor and make sure the entry is in 
Audio & Video. Make sure that the entry is ticked. Also tick Logout in the Other 
category.

You can add the WolfMixer next to the Mic and Volume Control on the panel by 
right-clicking on the panel and choosing 'Add / Remove Panel Items. Click 'Add' 
and choose 'Applications Launch Bar'. Select it at the bottom of the item list. 
Click the up button and watch the blue '+' sign in the panel move left until 
it is just to the right of the volume controls. Click 'Close'.

Click on the blue '+' in the Panel and navigate to the WolfMixer icon in 
'Audio & Video' and select it.

I add an Application Launcher at the right-hand end of the Panel and
add Logout to it.

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

README.txt, Version 9, 25/12/2022
