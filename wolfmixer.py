#  WolfMixer V0.9
#  Copyright (C) 2015, 2016, 2017, 2022 Roy Leith
#  For Python 3.X
#
#  This program is distributed under the terms of the GNU General Public License V3
#      see http://www.gnu.org/licenses/lgpl.txt
#
#
#  You may need to install the Python modules tkinter and Pmw
#  see the README.TXT file that came with this program file


from tkinter import *
import Pmw, subprocess, os


root = Tk()
root.title('WolfMixer V0.9')
root.option_add('*font', ('verdana', 10, 'bold'))

# Pmw.initialise()
playbackports = {'AIF': 'AIF', 'SPDIF': 'S/PDIF RX'}
playbackportsID = {b'1': 'PLAY', b'0': 'SPDIF'}
InputPorts = {b'None': 'None', b'PLAY': 'AIF1RX', b'Mic': 'IN1', b'DMICs': 'IN2', b'Line': 'IN3', b'SPDIF': 'AIF2RX', b'1kHz': "'Tone Generator", b'Noise': "'Noise Generator'"}
InputPortsID = {b'0': 'None', b'16': 'PLAY', b'9': 'Mic', b'10': 'DMICs', b'12': 'Line', b'24': 'SPDIF', b'1': '1kHz', b'7': 'Noise', b'48': 'LHPF'}

amixer = b"amixer -q -Dhw:RPiCirrus cset name='"
amixerstr = "amixer -q -Dhw:RPiCirrus cset name='"

# Set IN1, IN2 and IN3 ++input++ volumes to optimum (31) and HPOUT1, HPOUT2 and SPKOUT ++input++ volumes to optimum(32)
for defaultvol in [b"IN1L Volume' ", b"IN1R Volume' ", b"IN2L Volume' ", b"IN2R Volume' ", b"IN3L Volume' ", b"IN3R Volume' "]:
    os.system(amixer + defaultvol + b"31")

for defaultvol in [b"HPOUT1L Input 1 Volume' ", b"HPOUT1R Input 1 Volume' ", b"HPOUT2L Input 1 Volume' ", b"HPOUT2R Input 1 Volume' ", b"SPKOUTL Input 1 Volume' ", b"SPKOUTR Input 1 Volume' "]:
    os.system(amixer + defaultvol + b"32")

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
        os.system(amixerstr + "LHPF1 Mode' High-pass")
        os.system(amixerstr + "LHPF2 Mode' High-pass")
        hpf = "LHPF1"
        outport = outportname + postfix1 + " Input 1' "
        os.system(amixerstr + outport + hpf)
        outport = outportname + postfix2 + " Input 1' "
        hpf = "LHPF2"
        os.system(amixerstr + outport + hpf)
        outportname = "LHPF1"
        inport = inportname + prefix1
        outport = outportname + " Input 1' "
        os.system(amixerstr + outport + inport)
        outportname = "LHPF2"
        inport = inportname + prefix2
        outport = outportname + " Input 1' "
        os.system(amixerstr + outport + inport)
    else:
        inport = inportname + prefix1
        outport = outportname + postfix1 + " Input 1' "
        os.system(amixerstr + outport + inport)
        inport = inportname + prefix2
        outport = outportname + postfix2 + " Input 1' "
        os.system(amixerstr + outport + inport)
    
def Master_print_vol(val):
    val = val.encode('utf8')
    name = b"Master' "
    os.system(amixer + name + val)
    
def lineout_print_vol(val):
    val = val.encode('utf8')
    name = b"HPOUT2 Digital Volume' "
    os.system(amixer + name + val)
    
def lineout2_print_vol(val):
    val = val.encode('utf8')
    name = b"HPOUT2L Input 1 Volume' "
    os.system(amixer + name + val)
    name = b"HPOUT2R Input 1 Volume' "
    os.system(amixer + name + val)
    
def lineout_port(val):
    val = val.encode('utf8')
    os.system(amixer + b"HPOUT2 Digital Switch' " + b"off,off")
    inport = InputPorts[val]
    outport = "HPOUT2"
    patch(outport, inport)
    os.system(amixer + b"HPOUT2 Digital Switch' " + b"on,on")
    swlinevalue = statusquosw(b"HPOUT2 Digital Switch")
    lineoutSWvar.set(swlinevalue)

def SPDIF_print_vol(val):
    val = val.encode('utf8')
    name = b"AIF2TX1 Input 1 Volume' "
    os.system(amixer + name + val)
    name = b"AIF2TX2 Input 1 Volume' "
    os.system(amixer + name + val)
        
def SPDIF_port(val):
    val = val.encode('utf8')
    inport = InputPorts[val]
    outport = "AIF2TX"
    patch(outport, inport)
 
def Headset_print_vol(val):
    val = val.encode('utf8')
    name = b"HPOUT1 Digital Volume' "
    os.system(amixer + name + val)

def Headset2_print_vol(val):
    val = val.encode('utf8')
    name = b"HPOUT1L Input 1 Volume' "
    os.system(amixer + name + val)
    name = b"HPOUT1R Input 1 Volume' "
    os.system(amixer + name + val)
    
def Headset_port(val):
    val = val.encode('utf8')
    os.system(amixer + b"HPOUT1 Digital Switch' " + b"off,off")
    inport = InputPorts[val]
    outport = "HPOUT1"
    patch(outport, inport)
    os.system(amixer + b"HPOUT1 Digital Switch' " + b"on,on")
    swHSvalue = statusquosw(b"HPOUT1 Digital Switch")
    HeadsetSWvar.set(swHSvalue)

def Speaker_print_vol(val):
    val = val.encode('utf8')
    name = b"Speaker Digital Volume' "
    os.system(amixer + name + val)
    
def Speaker_port(val):
    val = val.encode('utf8')
    os.system(amixer + b"Speaker Digital Switch' " + b"off,off")
    inport = InputPorts[val]
    outport = "SPKOUT"
    patch(outport, inport)
    os.system(amixer + b"Speaker Digital Switch' " + b"on,on")
    swSpkvalue = statusquosw(b"Speaker Digital Switch")
    SpeakerSWvar.set(swSpkvalue)

def RECORD_print_vol(val):
    val = val.encode('utf8')
    name = b"AIF1TX1 Input 1 Volume' "
    os.system(amixer + name + val)
    name = b"AIF1TX2 Input 1 Volume' "
    os.system(amixer + name + val)
       
def RECORD_port(val):
    val = val.encode('utf8')
    inport = InputPorts[val]
    outport = "AIF1TX"
    patch(outport, inport)

# Input Volumes

def Headsetin_print_vol(val):
    val = val.encode('utf8')
    name = b"IN1L Digital Volume' "
    os.system(amixer + name + val)
    name = b"IN1R Digital Volume' "
    os.system(amixer + name + val)

def Headsetin2_print_vol(val):
    val = val.encode('utf8')
    name = b"IN1L Volume' "
    os.system(amixer + name + val)
    name = b"IN1R Volume' "
    os.system(amixer + name + val)
     
def DMIC_print_vol(val):
    val = val.encode('utf8')
    name = b"IN2L Digital Volume' "
    os.system(amixer + name + val)
    name = b"IN2R Digital Volume' "
    os.system(amixer + name + val)
    
def DMIC2_print_vol(val):
    val = val.encode('utf8')
    name = b"IN2L Volume' "
    os.system(amixer + name + val)
    name = b"IN2R Volume' "
    os.system(amixer + name + val)

def linein_print_vol(val):
    val = val.encode('utf8')
    name = b"IN3L Digital Volume' "
    os.system(amixer + name + val)
    name = b"IN3R Digital Volume' "
    os.system(amixer + name + val)
    
def linein2_print_vol(val):
    val = val.encode('utf8')
    name = b"IN3L Volume' "
    os.system(amixer + name + val)
    name = b"IN3R Volume' "
    os.system(amixer + name + val)

def Noise_print_vol(val):
    val = val.encode('utf8')
    name = b"Noise Generator Volume' "
    os.system(amixer + name + val)
    
# Switches
    
def lineoutsw():
    name = b"HPOUT2 Digital Switch' "
    if lineoutSWvar.get() == 0:
        os.system(amixer + name + b"on,on")
    if lineoutSWvar.get() == 1:
        os.system(amixer + name + b"off,off")
#    switchrep()

def Speakersw():
    name = b"Speaker Digital Switch' "
    if SpeakerSWvar.get() == 0:
        os.system(amixer + name + b"on,on")
    if SpeakerSWvar.get() == 1:
        os.system(amixer + name + b"off,off")
#    switchrep()

def Headsetsw():
    name = b"HPOUT1 Digital Switch' "
    if HeadsetSWvar.get() == 0:
        os.system(amixer + name + b"on,on")
    if HeadsetSWvar.get() == 1:
        os.system(amixer + name + b"off,off")
#    switchrep()        
        
def SpeakerHP():
    name = b"Speaker High Performance Switch' "
    if SpeakerHPSWvar.get() == 1:
        os.system(amixer + name + b"on")
    if SpeakerHPSWvar.get() == 0:
        os.system(amixer + name + b"off")
#    switchrep()

def SPDIFinSW():
    name = b"SPDIF in Switch' "
    if SPDIFinSWvar.get() == 1:
        os.system(amixer + name + b"on")
    if SPDIFinSWvar.get() == 0:
        os.system(amixer + name + b"off")
#    switchrep()

def lineinHP():
    name = b"IN3 High Performance Switch' "
    if lineinHPvar.get() == 1:
        os.system(amixer + name + b"on")
    if lineinHPvar.get() == 0:
        os.system(amixer + name + b"off")
#    switchrep()

def DMICHPSW():
    name = b"IN2 High Performance Switch' "
    if DMICHPSWvar.get() == 1:
        os.system(amixer + name + b"on")
    if DMICHPSWvar.get() == 0:
        os.system(amixer + name + b"off")
#    switchrep()

def HeadsetHP():
    name = b"IN1 High Performance Switch' "
    if HeadsetHPSWvar.get() == 1:
        os.system(amixer + name + b"on")
    if HeadsetHPSWvar.get() == 0:
        os.system(amixer + name + b"off")
#    switchrep()
    
def txsource(val):
    val = val.encode('utf8')
    if val == b'PLAY':
        os.system(amixer + b"Tx Source' " + b"AIF")
    if val == 'SPDIF':
        os.system(amixer + b"Tx Source' " + b"S/PDIF RX")

def switchrep():
    name = [b'HPOUT2 Digital Switch', b'HPOUT1 Digital Switch', b'Speaker Digital Switch', b'Speaker High Performance Switch', b'IN2 High Performance Switch', b'IN1 High Performance Switch', b'IN3 High Performance Switch']
    for switch in name:
        print(switch, b" = ", statusquosw(switch))
#    print b"." * 15
    

def statusquo(name):
    result = subprocess.check_output("amixer -Dhw:RPiCirrus cget name='" + name + "'", shell=True)
    lines = result.splitlines()
    maxvalue = b"null"
    minvalue = b"null"
    Rvalue = 0
    para = b"Null"
    for line in lines:
        if line.find(b",max=") > 0:
            maxvalue = (line[(line.find(b",max=") + 5):(line.find(b",step="))])
        if line.find(b",min=") > 0:
            minvalue = (line[(line.find(b",min=") + 5):(line.find(b",max="))])
        if (line.find(b",values=") > 0):
            para = (line[(line.find(b",values=") + 8):(line.find(b",min"))])
        if line.find(b": values") > 0:
            if para == b'1':        
                Rvalue = int(line[(line.find(b"=") + 1):])
            if para == b'2':
                Rvalue = int(line[(line.find(b",") + 1):])
    return maxvalue, minvalue, Rvalue

def statusquosw(name):
    Rvalue = 0
    para = b"Null"
    result = subprocess.check_output(b"amixer -Dhw:RPiCirrus cget name='" + name + b"'", shell=True)
    lines = result.splitlines()
    for line in lines:
        if (line.find(b",values=") > 0):
            if(line[(line.find(b",values=") + 8):]) == b"2":
                para = b'2'
        if (line.find(b",values=") > 0):
            if(line[(line.find(b",values=") + 8):]) == b"1":
                para = b'1'
        if line.find(b": values")>0:
            if (para == b'1'):        
                if (line[(line.find(b"=") + 1):]) == b"on":
                    Rvalue = 0
                if (line[(line.find(b"=") + 1):]) == b"off":
                    Rvalue = 1
            if (para == b'2'):
                if (line[(line.find(b",") + 1):]) == b"on":
                    Rvalue = 0
                if (line[(line.find(b",") + 1):]) == b"off":
                    Rvalue = 1 
    return  Rvalue
                         
def statusquopatch(name):
    result = subprocess.check_output("amixer -Dhw:RPiCirrus cget name='" + name + "'", shell=True)
    lines = result.splitlines()
    Rvalue = "Null"
    para = b"Null"
    for line in lines:
        if (line.find(b": values=") > 0):
            para = (line[(line.find(b"values=") + 7):])
            Rvalue = InputPortsID[para]
    return Rvalue

def statusquoplay(name):
    result = subprocess.check_output("amixer -Dhw:RPiCirrus cget name='" + name + "'", shell=True)
    lines = result.splitlines()
    Rvalue = b'0'
    para = b"Null"
    for line in lines:
        if (line.find(b": values=") > 0):
            para = (line[(line.find(b"values=") + 7):])
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
maxvalueHPOUT2, minvalueHPOUT2, RvalueHPOUT2 = statusquo(linename)
lineoutvolvar = IntVar()       
lineoutvolvar.set(RvalueHPOUT2)
lineoutvol = Scale(lineout, from_=maxvalueHPOUT2, to=minvalueHPOUT2, orient=VERTICAL, length=170, width=10, variable=lineoutvolvar, command= lineout_print_vol,).place(relx=0.00, rely=0.08)

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

lineoutnamesw = b'HPOUT2 Digital Switch'
swvalue = statusquosw(lineoutnamesw)

lineoutSWvar = IntVar()
lineoutSWvar.set(swvalue)
lineoutSW = Checkbutton(lineout, text="Mute", variable=lineoutSWvar, command=lineoutsw,).place(relx=lSW, rely=SWy2)

# SPDIF channel strip

SPDIF = Frame(Outputs,  width=chanwidth, height=chany, relief=RAISED, borderwidth=1)
SPDIF.pack(side=LEFT, pady=0, padx=1)
Label(SPDIF, text='SPDIF').place(relx=0.18, rely=0.02)

SPDIFname = 'AIF2TX1 Input 1 Volume'
maxvalueAIF2TX1, minvalueAIF2TX1, RvalueAIF2TX1 = statusquo(SPDIFname)
SPDIFvolvar = IntVar()       
SPDIFvolvar.set(RvalueAIF2TX1)            
SPDIFvol = Scale(SPDIF, from_=maxvalueAIF2TX1, to=minvalueAIF2TX1, orient=VERTICAL, length=170, width=10, variable=SPDIFvolvar, command= SPDIF_print_vol,).place(relx=0.00, rely=0.08)

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

maxvalueHPOUT1, minvalueHPOUT1, RvalueHPOUT1 = statusquo(HSname)
Headsetvolvar = IntVar()       
Headsetvolvar.set(RvalueHPOUT1)
Headsetvol = Scale(Headset, from_=maxvalueHPOUT1, to=minvalueHPOUT1, orient=VERTICAL, length=170, width=10, variable=Headsetvolvar, command= Headset_print_vol,).place(relx=0.00, rely=0.08)

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

Hsoutnamesw = b'HPOUT1 Digital Switch'
swvalue = statusquosw(Hsoutnamesw)
# print "Headset =", swvalue   
HeadsetSWvar = IntVar()
HeadsetSWvar.set(swvalue)
HeadsetSW = Checkbutton(Headset, text="Mute", variable=HeadsetSWvar, command=Headsetsw,).place(relx=lSW, rely=SWy2)

# Speaker channel strip

Speaker = Frame(Outputs,  width=chanwidth, height=chany, relief=RAISED, borderwidth=1)
Speaker.pack(side=LEFT, pady=0, padx=1)
Label(Speaker, text='Speaker').place(relx=0.08, rely=0.02)

Spkname = 'Speaker Digital Volume'
maxvalueSDV, minvalueSDV, RvalueSDV = statusquo(Spkname)
Speakervolvar = IntVar()       
Speakervolvar.set(RvalueSDV)            
Speakervol = Scale(Speaker, from_=maxvalueSDV, to=minvalueSDV, orient=VERTICAL, length=170, width=10, variable=Speakervolvar, command= Speaker_print_vol,).place(relx=0.00, rely=0.08)

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

Spknamesw = b'Speaker Digital Switch'
swvalue = statusquosw(Spknamesw)
# print "Speaker =", swvalue   
SpeakerSWvar = IntVar()
SpeakerSWvar.set(swvalue)
SpeakerSW = Checkbutton(Speaker, text="Mute", variable=SpeakerSWvar, command=Speakersw,).place(relx=lSW, rely=SWy2)

#'Speaker High Performance Switch'
namesw = b'Speaker High Performance Switch'
swvalue = statusquosw(namesw)

SpeakerHPSWvar = IntVar() 
SpeakerHPSWvar.set(swvalue)
SpeakerHPSW = Checkbutton(Speaker, text="HQ", variable=SpeakerHPSWvar, command=SpeakerHP,).place(relx=rSW, rely=SWy)

# RECORD channel strip

RECORD = Frame(Outputs, width=chanwidth, height=chany, relief=RAISED, borderwidth=1)
RECORD.pack(side=LEFT, pady=0, padx=1)
Label(RECORD, text='RECORD').place(relx=0.08, rely=0.02)

Recname = 'AIF1TX1 Input 1 Volume'
maxvalueAIF1TX1, minvalueAIF1TX1, RvalueAIF1TX1 = statusquo(Recname)
RECORDvolvar = IntVar()       
RECORDvolvar.set(RvalueAIF1TX1)            
RECORDvol = Scale(RECORD, from_=maxvalueAIF1TX1, to=minvalueAIF1TX1, orient=VERTICAL, length=170, width=10, variable=RECORDvolvar, command= RECORD_print_vol,).place(relx=0.00, rely=0.08)

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

nameIN2L = 'IN2L Digital Volume'
maxvalueIN2L, minvalueIN2L, RvalueIN2L = statusquo(nameIN2L)
DMICvar = IntVar()       
DMICvar.set(RvalueIN2L)
DMIC = Scale(inner, from_=maxvalueIN2L, to=minvalueIN2L, orient=VERTICAL, length=170, width=10, variable=DMICvar, command= DMIC_print_vol,).place(relx=0.00, rely=0.1)

DMICnamesw = b'IN2 High Performance Switch'
swvalue = statusquosw(DMICnamesw)

DMICHPSWvar = IntVar()
DMICHPSWvar.set(swvalue)
DMICHPSW = Checkbutton(inner, text="HQ", variable=DMICHPSWvar, command=DMICHPSW,).place(relx=irSW, rely=iSWy)
                         
# Headset In

Headsetin = Frame(Inputs, width=chanwidth, height=ichany, relief=RAISED, borderwidth=1)
Headsetin.pack(side=LEFT, pady=ipady, padx=1)
Label(Headsetin, text="H'set Mic.").place(relx=0.02, rely=0.02)

nameIN1L = 'IN1L Digital Volume'
maxvalueIN1L, minvalueIN1L, RvalueIN1L = statusquo(nameIN1L)
Headsetinvolvar = IntVar()       
Headsetinvolvar.set(RvalueIN1L)
Headsetinvol = Scale(Headsetin, from_=maxvalueIN1L, to=minvalueIN1L, orient=VERTICAL, length=170, width=10, variable=Headsetinvolvar, command= Headsetin_print_vol,).place(relx=0.00, rely=0.1)

Hsinnamesw = b'IN1 High Performance Switch'
swvalue = statusquosw(Hsinnamesw)

HeadsetHPSWvar = IntVar()
HeadsetHPSWvar.set(swvalue)
HeadsetHPSW = Checkbutton(Headsetin, text="HQ", variable=HeadsetHPSWvar, command=HeadsetHP,).place(relx=irSW, rely=iSWy)

#Line In
linein = Frame(Inputs, width=chanwidth, height=ichany, relief=RAISED, borderwidth=1)
linein.pack(side=LEFT, pady=ipady, padx=1)
Label(linein, text='Line In').place(relx=0.14, rely=0.02)

nameIN3L = 'IN3L Digital Volume'
maxvalueIN3L, minvalueIN3L, RvalueIN3L = statusquo(nameIN3L)
lineinvolvar = IntVar()       
lineinvolvar.set(RvalueIN3L)
lineinvol = Scale(linein, from_=maxvalueIN3L, to=minvalueIN3L, orient=VERTICAL, length=170, width=10, variable=lineinvolvar, command= linein_print_vol,).place(relx=0.00, rely=0.1)

lineinnamesw = b'IN3 High Performance Switch'
swvalue = statusquosw(lineinnamesw)

lineinHPvar = IntVar() 
lineinHPvar.set(swvalue)
lineinHPSW = Checkbutton(linein, text="HQ", variable=lineinHPvar, command=lineinHP,).place(relx=irSW, rely=iSWy)

# Noise
Noise = Frame(Inputs, width=chanwidth, height=ichany, relief=RAISED, borderwidth=1)
Noise.pack(side=LEFT, pady=0, padx=1)
Label(Noise, text='Noise').place(relx=0.2, rely=0.02)

nameNGV = 'Noise Generator Volume'
maxvalueNGV, minvalueNGV, RvalueNGV = statusquo(nameNGV)
Noisevolvar = IntVar()       
Noisevolvar.set(RvalueNGV)
Noisevol = Scale(Noise, from_=maxvalueNGV, to=minvalueNGV, orient=VERTICAL, length=170, width=10, variable=Noisevolvar, command= Noise_print_vol,).place(relx=0.00, rely=0.1)

root.mainloop()
