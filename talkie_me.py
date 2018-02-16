__author__ = 'TARSIER'

import sys
import binascii
import os

is_version3 = False
if (sys.version_info > (3, 0)):
    # Python 3 code in this block
    is_version3 = True
    
current_dir = os.getcwd()   #get current directory
wav_file = "message.wav"
fname= os.path.join(current_dir, wav_file)
f = open(fname, "rb")

# start of code variable declaration based from audio filename
code ="const uint8_t sp"+ wav_file[:-4]+"[] PROGMEM ={"
try:
    byte = f.read(1)
    while byte != "":
        # Do stuff with byte.
        byte = f.read(1)
        if is_version3:
            #print ("%s0x%s," % ( code,(binascii.hexlify(byte)).decode("ascii").upper()))
            code = "%s0x%s," % ( code,(binascii.hexlify(byte)).decode("ascii").upper())
        else:
            #print "0x"+(binascii.hexlify(byte))+" ,",
            code = code + "0x"+(binascii.hexlify(byte)) +","
                
except Exception as ex:
    print (ex)
finally:
    f.close()
    code = code[:-4]
    code = code +"};"
    print (code)
    print
    print("voice.say(sp"+wav_file[:-4]+");")
