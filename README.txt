                               WolfMixer V0.6
                                  21/02/15
Copyright (C) 2015 Roy Leith


This program is distributed under the terms of the GNU General Public License V3
See http://www.gnu.org/licenses/lgpl.txt


BACKGROUND

Wolfson produced a sound card for the Raspberry Pi and an SD card Raspbian image with the drivers compiled into the kernel. The driver controls appeared in the Raspbian 'amixer' program and in the 'alsamixer' graphical representation, but included over 400 controls in total. The alsa mixer GUI just could not deal with it.

My first mixer was based on this image.

When Cirrus issued a new Raspbian image it came with a new set of alsamixer controls requiring a fair amount of rewriting for my mixer. I included all of the volume controls made available for simple patches (i.e. not including graphic equalisers or High/Low Pass filters).

This version (V0.5) of the mixer showed that,

1) The 'minor' input volume controls were best set to maximum for lowest noise (the default setting in the image) and the 'minor' output volumes to '32' (which is around 0dB giving a modest amount of headroom).

WOLFMIXER v0.6

Wolfmixer V0.6 sets the 'minor' volume settings to maximum for the input channels (Line In, DMIC and Headset Mic) and to 0dB (the highest output channel setting with headroom to spare) for the output channels (Line Out, Headset and Speaker). There are no controls for these settings in the WolfMixer GUI.

By default, V0.6 inserts a High-pass Filter whenever an output channel is connected to DMIC or Headset Mic. 

Note: A filter is not inserted for Line In. If you are using Line In with Mic Bias and electret microphones then you should use the scripts provided by Cirrus. If there is a demand for it, I will add the feature to the next version of the mixer.

THE FUTURE

I am expecting Cirrus to integrate the driver into the standard Raspbian image at some point. At that time I am sure there will be further changes to the way the driver interacts with alsamixer. Both the original Wolfson and the latest Cirrus images include controls that don't appear to function correctly, if at all.

I hope that they will release a mixer GUI that fully supports all the card's features so that mine will be just an interim arrangement. If this does not happen in the near future, I may extend Wolfmixer to include the equalisers and the dynamic compressors. 

It is less likely that I will add the ability to mix four inputs on one output channel because of the required size of the mixer window. Technically, it is not a complex addition.

I will also consider a 'precompiled' version to speed the program startup.

WHAT YOU GET

wolfmixer.py, WolfMixer (this is a desktop icon file. Raspbian displays it with the icon name and not the file name of wolfmixer.desktop), WolfMixer.png (the picture file for the icon) and this README.txt file.


Please copy the files into a /home/pi/Programs directory. Point the file manager to this directory and choose 'Open Current Folder in Terminal' in the Tools menu. Type the following into Terminal (after the '$' prompt),

pi@raspberrypi ~/Programs $ python wolfmixer.py

The program will, probably, report missing modules, in particular the Pwm module (I think the rest are already installed).

Install the missing module(s) with,

  pi@raspberrypi ~/Programs $ sudo apt-get install python-pmw <any other missing
  modules>

The program is a text file. You can open it with Leafpad and see which modules are loaded towards the beginning of the file.

  from Tkinter import *
  import Pmw, subprocess, os

In addition to wolfmixer.py, there is a file for a desktop icon,

  wolfmixer.desktop.

Because it is an icon file, it appears in the file manager as 'WolfMixer'. If you copy this file to /home/pi/Desktop, then you will be able to start the program by clicking on the desktop icon. It should appear on the Raspbian desktop as a howling wolf icon. It's an interpreted program and takes a little time to appear. If Cirrus do not produce a mixer GUI I may produce a 'pre-compiled' form to speed the start-up.

IN USE

On startup, WolfMixer collects the settings that it finds in alsamixer and adjusts its controls to those settings. If you have not made any changes, yourself, the settings in the newly installed Cirrus image are a good place to start. If you have already experimented with alsamixer and the amixer command-line scripts then those initial settings will have been lost.

Whatever you change in the mixer is saved by alsamixer and will remain as the new default setting even if you reboot the Raspi.

When you select DMIC or Headset Mic as an input, the input selection button will show those as being set. However, in the background, a high-pass filter has been inserted and the next time you start WolfMixer it will display LHPF rather than DMIC or Mic. The patch has not been changed.

Not all the controls work correctly. This is something to do with the driver implementation and its interaction with alsa. If you get no sound, try turning the mute button 'on' then 'off'. Sometimes the driver or the audio program get in a tizzy. Reboot the Raspi.

I have given AIF1 and AIF2 explanatory names. The 'RECORD' channel will present any connected Cirrus input port to the Raspberry Pi for use in an audio recording program such as Audacity. Connecting PLAY to an output channel will connect the Raspberry Pi audio playback to that output port. The Raspberry Pi playback volume cannot be adjusted by WolfMixer or alsamixer. Use the panel app. You may find erroneous 'Mute' indications in the app, but it does not seem to affect playback.

README.txt, Version2, 21/02/15