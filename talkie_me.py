__author__ = 'TARSIER'

import sys
import binascii
import os

def non_alphanumeric(string):
    return ''.join(ch for ch in string if ch.isalnum())
    
is_version3 = False
if (sys.version_info > (3, 0)):
    # Python 3 code in this block
    is_version3 = True
    
current_dir = os.getcwd()   #get current working directory
wav_file = "message.wav" #set as default audio file
if len(sys.argv) > 1:
    #cmd_args = str(sys.argv)
    #print (cmd_args)
    if sys.argv[1].strip():
        wav_file = str(sys.argv[1])
        
#print (wav_file)
extension = os.path.splitext(wav_file)[1].strip()
#print(extension)
if extension == '.wav':
    variable_name = non_alphanumeric(wav_file[:-4]).upper()
    fname= os.path.join(current_dir, wav_file)
    if os.path.isfile(fname):    
        # start of code variable declaration based from audio filename
        code ="const uint8_t sp"+ variable_name+"[] PROGMEM ={\n"
        try:
            with open(fname, "rb") as f:
                while True:
                    byte = f.read(1)
                    if not byte:
                        break
                    if is_version3:
                        #print ("%s0x%s, " % ( code,(binascii.hexlify(byte)).decode("ascii").upper()))
                        code = ("%s0x%s, " % (
                                        code, (binascii.hexlify(byte)).decode("ascii").strip().upper()))
                    else:
                        #print ("%s0x%s, " % (code,(binascii.hexlify(byte))))
                        code = ("%s0x%s, " %
                                            (code, (binascii.hexlify(byte)).strip().upper()))
        except Exception as ex:
            print (ex)
        finally:
            code = code[:-1] #remove last chars (comma)
            code = code +"\n};"
            print (code)
            print
            print("voice.say(sp"+variable_name+");")
    else:
        print ("%s file not found" % wav_file)
else:
    print ("Please select WAV file only.")
