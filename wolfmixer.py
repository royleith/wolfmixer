#  WolfMixer V0.8
#  Copyright (C) 2015, 2016, 2017 Roy Leith
#
#
#  This program is distributed under the terms of the GNU General Public License V3
#      see http://www.gnu.org/licenses/lgpl.txt
#
#
#  You may need to install the Python modules Tkinter and Pmw
#  sudo apt-get install python-tk python-pmw

from Tkinter import *
import Pmw, subprocess, os


root = Tk()
root.title('WolfMixer V0.8')
root.option_add('*font', ('verdana', 10, 'bold'))

# Pmw.initialise()
playbackports = {'AIF':'AIF', 'SPDIF':'S/PDIF RX'}
playbackportsID = {'1': 'PLAY', '0':'SPDIF'}
InputPorts = {'None':'None', 'PLAY':'AIF1RX', 'Mic':'IN1', 'DMICs':'IN2', 'Line':'IN3', 'SPDIF':'AIF2RX', '1kHz':"'Tone Generator", 'Noise':"'Noise Generator'"}
InputPortsID = {'0':'None', '16':'PLAY', '9':'Mic', '10':'DMICs', '12':'Line', '24':'SPDIF', '1':'1kHz', '7':'Noise', '48':'LHPF'}

amixer = "amixer -q -Dhw:RPiCirrus cset name='"

# Set IN1, IN2 and IN3 input volumes to optimum (31) and 
for defaultvol in ["IN1L Volume' ", "IN1R Volume' ", "IN2L Volume' ", "IN2R Volume' ", "IN3L Volume' ", "IN3R Volume' "]:
    os.system(amixer + defaultvol + "31")

for defaultvol in ["HPOUT1L Input 1 Volume' ", "HPOUT1R Input 1 Volume' ", "HPOUT2L Input 1 Volume' ", "HPOUT2R Input 1 Volume' ", "SPKOUTL Input 1 Volume' ", "SPKOUTR Input 1 Volume' "]:
    os.system(amixer + defaultvol + "32")

def patch(outportname, inportname):
    prefix1 = "L"
    prefix2 = "R"
    postfix1 = "L"
    postfix2 = "R"
    if inportname == "AIF2RX" or inportname == "AIF1RX":
        prefix1 = "1"
        prefix2 = "2"
    if inportname == "IN1":
        prefix1 = "R"
        prefix2 = "R"
    if inportname == "'Noise Generator'" or inportname == "None":
        prefix1 = ""
        prefix2 = ""
    if inportname == "'Tone Generator":
        prefix1 = " 1'"
        prefix2 = " 1'"
    if outportname == "AIF1TX" or outportname == "AIF2TX":
        postfix1 = "1"
        postfix2 = "2"
    if inportname == "IN1" or inportname == "IN2":
        os.system(amixer + "LHPF1 Mode' High-pass")
        os.system(amixer + "LHPF2 Mode' High-pass")
        hpf = "LHPF1"
        outport = outportname + postfix1 + " Input 1' "
        os.system(amixer + outport + hpf)
        outport = outportname + postfix2 + " Input 1' "
        hpf = "LHPF2"
        os.system(amixer + outport + hpf)
        outportname = "LHPF1"
        inport = inportname + prefix1
        outport = outportname + " Input 1' "
        os.system(amixer + outport + inport)
        outportname = "LHPF2"
        inport = inportname + prefix2
        outport = outportname + " Input 1' "
        os.system(amixer + outport + inport)
    else:
        inport = inportname + prefix1
        outport = outportname + postfix1 + " Input 1' "
        os.system(amixer + outport + inport)
        inport = inportname + prefix2
        outport = outportname + postfix2 + " Input 1' "
        os.system(amixer + outport + inport)
    
def Master_print_vol(val):
    name = "Master' "
    os.system(amixer + name + val)
    
def lineout_print_vol(val):
    name = "HPOUT2 Digital Volume' "
    os.system(amixer + name + val)
    
def lineout2_print_vol(val):
    name = "HPOUT2L Input 1 Volume' "
    os.system(amixer + name + val)
    name = "HPOUT2R Input 1 Volume' "
    os.system(amixer + name + val)
    
def lineout_port(val):
    os.system(amixer + "HPOUT2 Digital Switch' " + "off,off")
    inport = InputPorts[val]
    outport = "HPOUT2"
    patch(outport, inport)
    os.system(amixer + "HPOUT2 Digital Switch' " + "on,on")
    swlinevalue = statusquosw("HPOUT2 Digital Switch")
    lineoutSWvar.set(swlinevalue)

def SPDIF_print_vol(val):
    name = "AIF2TX1 Input 1 Volume' "
    os.system(amixer + name + val)
    name = "AIF2TX2 Input 1 Volume' "
    os.system(amixer + name + val)
        
def SPDIF_port(val):
    inport = InputPorts[val]
    outport = "AIF2TX"
    patch(outport, inport)
 
def Headset_print_vol(val):
    name = "HPOUT1 Digital Volume' "
    os.system(amixer + name + val)

def Headset2_print_vol(val):
    name = "HPOUT1L Input 1 Volume' "
    os.system(amixer + name + val)
    name = "HPOUT1R Input 1 Volume' "
    os.system(amixer + name + val)
    
def Headset_port(val):
    os.system(amixer + "HPOUT1 Digital Switch' " + "off,off")
    inport = InputPorts[val]
    outport = "HPOUT1"
    patch(outport, inport)
    os.system(amixer + "HPOUT1 Digital Switch' " + "on,on")
    swHSvalue = statusquosw("HPOUT1 Digital Switch")
    HeadsetSWvar.set(swHSvalue)

def Speaker_print_vol(val):
    name = "Speaker Digital Volume' "
    os.system(amixer + name + val)

def Speaker2_print_vol(val):
    name = "SPKOUTL Input 1 Volume' "
    os.system(amixer + name + val)
    name = "SPKOUTR Input 1 Volume' "
    os.system(amixer + name + val)
    
def Speaker_port(val):
    os.system(amixer + "Speaker Digital Switch' " + "off,off")
    inport = InputPorts[val]
    outport = "SPKOUT"
    patch(outport, inport)
    os.system(amixer + "Speaker Digital Switch' " + "on,on")
    swSpkvalue = statusquosw("Speaker Digital Switch")
    SpeakerSWvar.set(swSpkvalue)

def RECORD_print_vol(val):
    name = "AIF1TX1 Input 1 Volume' "
    os.system(amixer + name + val)
    name = "AIF1TX2 Input 1 Volume' "
    os.system(amixer + name + val)
       
def RECORD_port(val):
    inport = InputPorts[val]
    outport = "AIF1TX"
    patch(outport, inport)

# Input Volumes

def Headsetin_print_vol(val):
    name = "IN1L Digital Volume' "
    os.system(amixer + name + val)
    name = "IN1R Digital Volume' "
    os.system(amixer + name + val)

def Headsetin2_print_vol(val):
    name = "IN1L Volume' "
    os.system(amixer + name + val)
    name = "IN1R Volume' "
    os.system(amixer + name + val)
     
def DMIC_print_vol(val):
    name = "IN2L Digital Volume' "
    os.system(amixer + name + val)
    name = "IN2R Digital Volume' "
    os.system(amixer + name + val)
    
def DMIC2_print_vol(val):
    name = "IN2L Volume' "
    os.system(amixer + name + val)
    name = "IN2R Volume' "
    os.system(amixer + name + val)

def linein_print_vol(val):
    name = "IN3L Digital Volume' "
    os.system(amixer + name + val)
    name = "IN3R Digital Volume' "
    os.system(amixer + name + val)
    
def linein2_print_vol(val):
    name = "IN3L Volume' "
    os.system(amixer + name + val)
    name = "IN3R Volume' "
    os.system(amixer + name + val)

def Noise_print_vol(val):
    name = "Noise Generator Volume' "
    os.system(amixer + name + val)
    
# Switches
    
def lineoutsw():
    name = "HPOUT2 Digital Switch' "
    if lineoutSWvar.get() == 0:
        os.system(amixer + name + "on,on")
    if lineoutSWvar.get() == 1:
        os.system(amixer + name + "off,off")
#    switchrep()

def Speakersw():
    name = "Speaker Digital Switch' "
    if SpeakerSWvar.get() == 0:
        os.system(amixer + name + "on,on")
    if SpeakerSWvar.get() == 1:
        os.system(amixer + name + "off,off")
#    switchrep()

def Headsetsw():
    name = "HPOUT1 Digital Switch' "
    if HeadsetSWvar.get() == 0:		
        os.system(amixer + name + "on,on")
    if HeadsetSWvar.get() == 1:
        os.system(amixer + name + "off,off")
#    switchrep()        
        
def SpeakerHP():
    name = "Speaker High Performance Switch' "
    if SpeakerHPSWvar.get() == 1:
        os.system(amixer + name + "on")
    if SpeakerHPSWvar.get() == 0:
        os.system(amixer + name + "off")
#    switchrep()
  


def SPDIFinSW():
    name = "SPDIF in Switch' "
    if SPDIFinSWvar.get() == 1:
        os.system(amixer + name + "on")
    if SPDIFinSWvar.get() == 0:
        os.system(amixer + name + "off")
#    switchrep()

    
def lineinHP():
    name = "IN3 High Performance Switch' "
    if lineinHPvar.get() == 1:
        os.system(amixer + name + "on")
    if lineinHPvar.get() == 0:
        os.system(amixer + name + "off")
#    switchrep()



def DMICHPSW():
    name = "IN2 High Performance Switch' "
    if DMICHPSWvar.get() == 1:
        os.system(amixer + name + "on")
    if DMICHPSWvar.get() == 0:
        os.system(amixer + name + "off")
#    switchrep()
    


def HeadsetHP():
    name = "IN1 High Performance Switch' "
    if HeadsetHPSWvar.get() == 1:
        os.system(amixer + name + "on")
    if HeadsetHPSWvar.get() == 0:
        os.system(amixer + name + "off")
#    switchrep()
    

    
def txsource(val):
    if val == 'PLAY':
        os.system(amixer + "Tx Source' " + "AIF")
    if val == 'SPDIF':
        os.system(amixer + "Tx Source' " + "S/PDIF RX")

def switchrep():
    name = ['HPOUT2 Digital Switch', 'HPOUT1 Digital Switch', 'Speaker Digital Switch', 'Speaker High Performance Switch', 'IN2 High Performance Switch', 'IN1 High Performance Switch', 'IN3 High Performance Switch']
    for switch in name:
        print switch, " = ", statusquosw(switch)
#    print "." * 15
    

def statusquo(name):
    result = subprocess.check_output("amixer -Dhw:RPiCirrus cget name='" + name + "'", shell=True)
    lines = result.split("\n")  
    maxvalue = "null"
    minvalue = "null"
    Rvalue = "null"
    para = "Null"
    for line in lines:
        if line.find(",max=") > 0:
            maxvalue = (line[(line.find(",max=") + 5):(line.find(",step="))])
        if line.find(",min=") > 0:
            minvalue = (line[(line.find(",min=") + 5):(line.find(",max="))])
        if (line.find(",values=") > 0):
            para = (line[(line.find(",values=") + 8):(line.find(",min"))])
        if line.find(": values") > 0:
            if para == '1':        
                Rvalue = int(line[(line.find("=") + 1):])
            if para == '2':
                Rvalue = int(line[(line.find(",") + 1):])

    return maxvalue, minvalue, Rvalue

def statusquosw(name):
    Rvalue = "null"
    para = "Null"
    result = subprocess.check_output("amixer -Dhw:RPiCirrus cget name='" + name + "'", shell=True)
    lines = result.split("\n")  
    for line in lines:
        if (line.find(",values=") > 0):
            if(line[(line.find(",values=") + 8):]) == "2":
                para = 2
        if (line.find(",values=") > 0):
            if(line[(line.find(",values=") + 8):]) == "1":
                para = 1
        if line.find(": values")>0:
            if (para == 1):        
                if (line[(line.find("=") + 1):]) == "on":
                    Rvalue = 0
                if (line[(line.find("=") + 1):]) == "off":
                    Rvalue = 1
            if (para == 2):
                if (line[(line.find(",") + 1):]) == "on":
                    Rvalue = 0
                if (line[(line.find(",") + 1):]) == "off":
                    Rvalue = 1 
    return  Rvalue
    
                                       
def statusquopatch(name):
    result = subprocess.check_output("amixer -Dhw:RPiCirrus cget name='" + name + "'", shell=True)
    lines = result.split("\n")  
    Rvalue = "null"
    para = "Null"
    for line in lines:
        if (line.find(": values=") > 0):
            para = (line[(line.find("values=") + 7):])
            Rvalue = InputPortsID[para]


    return Rvalue

def statusquoplay(name):
    result = subprocess.check_output("amixer -Dhw:RPiCirrus cget name='" + name + "'", shell=True)
    lines = result.split("\n")  
    Rvalue = "null"
    para = "Null"
    for line in lines:
        if (line.find(": values=") > 0):
            para = (line[(line.find("values=") + 7):])
            Rvalue = playbackportsID[para]
    return Rvalue


# Outputs Panel
chanwidth = 84
SWy = 0.85
SWy2 = 0.92
chany = 266
rSW = 0.20
lSW = 0.00
menuy = 0.74
menux = 0.01
Outputs = Frame(root, width=800, height=600, relief=FLAT, borderwidth=1)
Outputs.pack(side=TOP, pady=0, padx=0)
Label(Outputs, text='Outputs').pack(side=TOP, pady=0, padx=0)

# lineout channel strip

lineout = Frame(Outputs, width=chanwidth, height=chany, relief=RAISED, borderwidth=1)
lineout.pack(side=LEFT, pady=0, padx=1)
Label(lineout, text='Line Out').place(relx=0.1, rely=0.02)
linename = 'HPOUT2 Digital Volume'
maxvalue, minvalue, Rvalue = statusquo(linename)
lineoutvolvar = IntVar()       
lineoutvolvar.set(Rvalue)
lineoutvol = Scale(lineout, from_=maxvalue, to=minvalue, orient=VERTICAL, length=170, width=10,
    variable=lineoutvolvar, command= lineout_print_vol,).place(relx=0.00, rely=0.08)


# Patcher
patchname = 'HPOUT2L Input 1'
lineoutvar = StringVar()
lineoutvar.set(statusquopatch(patchname))
lineout_opt_menu = Pmw.OptionMenu(lineout, 
    menubutton_textvariable = lineoutvar,
    items=('None', 'PLAY', 'Mic', 'DMICs', 'Line', 'SPDIF', '1kHz', 'Noise'),
    menubutton_width=4,
    command= lineout_port,)
lineout_opt_menu.place(relx=menux, rely=menuy)

lineoutnamesw = 'HPOUT2 Digital Switch'
swvalue = statusquosw(lineoutnamesw)
# print "Lineout =", swvalue

lineoutSWvar = IntVar()
lineoutSWvar.set(swvalue)
lineoutSW = Checkbutton(lineout, text="Mute",
                          variable=lineoutSWvar, command=lineoutsw,).place(relx=lSW, rely=SWy2)

# SPDIF channel strip

SPDIF = Frame(Outputs,  width=chanwidth, height=chany, relief=RAISED, borderwidth=1)
SPDIF.pack(side=LEFT, pady=0, padx=1)
Label(SPDIF, text='SPDIF').place(relx=0.18, rely=0.02)

SPDIFname = 'AIF2TX1 Input 1 Volume'
maxvalue, minvalue, Rvalue = statusquo(SPDIFname)
SPDIFvolvar = IntVar()       
SPDIFvolvar.set(Rvalue)            
SPDIFvol = Scale(SPDIF, from_=maxvalue, to=minvalue, orient=VERTICAL, length=170, width=10,
    variable=SPDIFvolvar, command= SPDIF_print_vol,).place(relx=0.00, rely=0.08)

# Patcher
patchname = 'AIF2TX1 Input 1'
SPDIFvar = StringVar()
SPDIFvar.set(statusquopatch(patchname))
SPDIF_opt_menu = Pmw.OptionMenu(SPDIF, 
    menubutton_textvariable = SPDIFvar,
    items=('None', 'PLAY', 'Mic', 'DMICs', 'Line', '1kHz', 'Noise'),
    menubutton_width=4,
    command= SPDIF_port,)
SPDIF_opt_menu.place(relx=menux, rely=menuy)


# Headset channel strip

Headset = Frame(Outputs,  width=chanwidth, height=chany, relief=RAISED, borderwidth=1)
Headset.pack(side=LEFT, pady=0, padx=1)
Label(Headset, text='Headset').place(relx=0.08, rely=0.02)

HSname = 'HPOUT1 Digital Volume'

maxvalue, minvalue, Rvalue = statusquo(HSname)
Headsetvolvar = IntVar()       
Headsetvolvar.set(Rvalue)
Headsetvolvar.set(Rvalue)
Headsetvol = Scale(Headset, from_=maxvalue, to=minvalue, orient=VERTICAL, length=170, width=10,
    variable=Headsetvolvar, command= Headset_print_vol,).place(relx=0.00, rely=0.08)


# Patcher
patchname = 'HPOUT1L Input 1'
Headsetvar = StringVar()
Headsetvar.set(statusquopatch(patchname))
Headset_opt_menu = Pmw.OptionMenu(Headset, 
    menubutton_textvariable = Headsetvar,
    items=('None', 'PLAY', 'Mic', 'DMICs', 'Line', 'SPDIF', '1kHz', 'Noise'),
    menubutton_width=4,
    command= Headset_port,)
Headset_opt_menu.place(relx=menux, rely=menuy)

Hsoutnamesw = 'HPOUT1 Digital Switch'
swvalue = statusquosw(Hsoutnamesw)
# print "Headset =", swvalue   
HeadsetSWvar = IntVar()
HeadsetSWvar.set(swvalue)
HeadsetSW = Checkbutton(Headset, text="Mute",
                          variable=HeadsetSWvar, command=Headsetsw,).place(relx=lSW, rely=SWy2)

# Speaker channel strip

Speaker = Frame(Outputs,  width=chanwidth, height=chany, relief=RAISED, borderwidth=1)
Speaker.pack(side=LEFT, pady=0, padx=1)
Label(Speaker, text='Speaker').place(relx=0.08, rely=0.02)

Spkname = 'Speaker Digital Volume'
maxvalue, minvalue, Rvalue = statusquo(Spkname)
Speakervolvar = IntVar()       
Speakervolvar.set(Rvalue)            
Speakervol = Scale(Speaker, from_=maxvalue, to=minvalue, orient=VERTICAL, length=170, width=10,
    variable=Speakervolvar, command= Speaker_print_vol,).place(relx=0.00, rely=0.08)


# Patcher
patchname = 'SPKOUTL Input 1'
Speakervar = StringVar()
Speakervar.set(statusquopatch(patchname))
Speaker_opt_menu = Pmw.OptionMenu(Speaker, 
    menubutton_textvariable = Speakervar,
    items=('None', 'PLAY', 'Mic', 'DMICs', 'Line', 'SPDIF', '1kHz', 'Noise'),
    menubutton_width=4,
    command= Speaker_port,)
Speaker_opt_menu.place(relx=menux, rely=menuy)

Spknamesw = 'Speaker Digital Switch'
swvalue = statusquosw(Spknamesw)
# print "Speaker =", swvalue   
SpeakerSWvar = IntVar()
SpeakerSWvar.set(swvalue)
SpeakerSW = Checkbutton(Speaker, text="Mute",
                          variable=SpeakerSWvar, command=Speakersw,).place(relx=lSW, rely=SWy2)


#'Speaker High Performance Switch'
namesw = 'Speaker High Performance Switch'
swvalue = statusquosw(namesw)

SpeakerHPSWvar = IntVar() 
SpeakerHPSWvar.set(swvalue)
SpeakerHPSW = Checkbutton(Speaker, text="HQ",
                          variable=SpeakerHPSWvar, command=SpeakerHP,).place(relx=rSW, rely=SWy)

# RECORD channel strip

RECORD = Frame(Outputs, width=chanwidth, height=chany, relief=RAISED, borderwidth=1)
RECORD.pack(side=LEFT, pady=0, padx=1)
Label(RECORD, text='RECORD').place(relx=0.08, rely=0.02)

Recname = 'AIF1TX1 Input 1 Volume'
maxvalue, minvalue, Rvalue = statusquo(Recname)
RECORDvolvar = IntVar()       
RECORDvolvar.set(Rvalue)            
RECORDvol = Scale(RECORD, from_=maxvalue, to=minvalue, orient=VERTICAL, length=170, width=10,
    variable=RECORDvolvar, command= RECORD_print_vol,).place(relx=0.00, rely=0.08)

# Patcher
patchname = 'AIF1TX1 Input 1'
RECORDvar = StringVar()
RECORDvar.set(statusquopatch(patchname))
RECORD_opt_menu = Pmw.OptionMenu(RECORD, 
    menubutton_textvariable = RECORDvar,
    items=('None', 'PLAY', 'Mic', 'DMICs', 'Line', 'SPDIF', '1kHz', 'Noise'),
    menubutton_width=4,
    command= RECORD_port,)
RECORD_opt_menu.place(relx=menux, rely=menuy)

# Switches and Title Panel

Switches = Frame(root, width=200, height=10, relief=FLAT, borderwidth=1)
Switches.pack(side=TOP, pady=0, padx=1, anchor=W)

                    

Label(Switches, text='                                                Inputs').pack(side=TOP, pady=1, padx=1, anchor=E)




# Input Panel
chanwidth = 84
iSWy = 0.80
iSWy2 = 0.89
ichany = 238
irSW = 0.20
ilSW = 0.00
ipady = 0
Inputs = Frame(root, width=800, height=500, relief=FLAT, borderwidth=1)
Inputs.pack(side=TOP, pady=0, padx=0)

# Master

Master = Frame(Inputs, width=chanwidth, height=160, relief=FLAT, borderwidth=1)
Master.pack(side=LEFT, pady=0, padx=0)

Label(Master, text='TX Source').pack(side=TOP, pady=2, padx=0)

# Source Switch

sourcename = 'Tx Source'
txsourcevar = StringVar()
txsourcevar.set(statusquoplay(sourcename))
txsource_opt_menu = Pmw.OptionMenu(Master, 
    menubutton_textvariable = txsourcevar,
    items=('PLAY', 'SPDIF'),
    menubutton_width=4,
    command=txsource,)
txsource_opt_menu.pack(side=TOP, pady=2, padx=0)

# DMIC

inner = Frame(Inputs, width=chanwidth, height=ichany, relief=RAISED, borderwidth=1)
inner.pack(side=LEFT, padx=1, pady=ipady)
Label(inner, text='DMIC').place(relx=0.2, rely=0.02)

name = 'IN2L Digital Volume'
maxvalue, minvalue, Rvalue = statusquo(name)
DMICvar = IntVar()       
DMICvar.set(Rvalue)
DMIC = Scale(inner, from_=maxvalue, to=minvalue, orient=VERTICAL, length=170, width=10,
    variable=DMICvar, command= DMIC_print_vol,).place(relx=0.00, rely=0.1)


DMICnamesw = 'IN2 High Performance Switch'
swvalue = statusquosw(DMICnamesw)

DMICHPSWvar = IntVar()
DMICHPSWvar.set(swvalue)
DMICHPSW = Checkbutton(inner, text="HQ",
                          variable=DMICHPSWvar, command=DMICHPSW,).place(relx=irSW, rely=iSWy)
                         
# Headset In

Headsetin = Frame(Inputs, width=chanwidth, height=ichany, relief=RAISED, borderwidth=1)
Headsetin.pack(side=LEFT, pady=ipady, padx=1)
Label(Headsetin, text="H'set Mic.").place(relx=0.02, rely=0.02)

name = 'IN1L Digital Volume'
maxvalue, minvalue, Rvalue = statusquo(name)
Headsetinvolvar = IntVar()       
Headsetinvolvar.set(Rvalue)
Headsetinvol = Scale(Headsetin, from_=maxvalue, to=minvalue, orient=VERTICAL, length=170, width=10,
    variable=Headsetinvolvar, command= Headsetin_print_vol,).place(relx=0.00, rely=0.1)


Hsinnamesw = 'IN1 High Performance Switch'
swvalue = statusquosw(Hsinnamesw)

HeadsetHPSWvar = IntVar()
HeadsetHPSWvar.set(swvalue)
HeadsetHPSW = Checkbutton(Headsetin, text="HQ",
                          variable=HeadsetHPSWvar, command=HeadsetHP,).place(relx=irSW, rely=iSWy)
                     
                          
#Line In
linein = Frame(Inputs, width=chanwidth, height=ichany, relief=RAISED, borderwidth=1)
linein.pack(side=LEFT, pady=ipady, padx=1)
Label(linein, text='Line In').place(relx=0.14, rely=0.02)

name = 'IN3L Digital Volume'
maxvalue, minvalue, Rvalue = statusquo(name)
lineinvolvar = IntVar()       
lineinvolvar.set(Rvalue)
lineinvol = Scale(linein, from_=maxvalue, to=minvalue, orient=VERTICAL, length=170, width=10,
    variable=lineinvolvar, command= linein_print_vol,).place(relx=0.00, rely=0.1)


lineinnamesw = 'IN3 High Performance Switch'
swvalue = statusquosw(lineinnamesw)

lineinHPvar = IntVar() 
lineinHPvar.set(swvalue)
lineinHPSW = Checkbutton(linein, text="HQ",
                          variable=lineinHPvar, command=lineinHP,).place(relx=irSW, rely=iSWy)


# Noise
Noise = Frame(Inputs, width=chanwidth, height=ichany, relief=RAISED, borderwidth=1)
Noise.pack(side=LEFT, pady=0, padx=1)
Label(Noise, text='Noise').place(relx=0.2, rely=0.02)

name = 'Noise Generator Volume'
maxvalue, minvalue, Rvalue = statusquo(name)
Noisevolvar = IntVar()       
Noisevolvar.set(Rvalue)
Noisevol = Scale(Noise, from_=maxvalue, to=minvalue, orient=VERTICAL, length=170, width=10,
    variable=Noisevolvar, command= Noise_print_vol,).place(relx=0.00, rely=0.1)


root.mainloop()
