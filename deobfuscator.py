import re
import hashlib

from base64 import b85decode as b85
from pystyle import Center, Colors, Colorate, System, Write
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

System.Clear()
System.Title("pyobfuscate.com deobfuscator by over_on_top")
System.Size(130, 30)

text = '''
______            _      __                     _                            
| ___ \          | |    / _|                   | |                           
| |_/ /   _  ___ | |__ | |_ _   _ ___  ___ __ _| |_ ___   ___ ___  _ __ ___  
|  __/ | | |/ _ \| '_ \|  _| | | / __|/ __/ _` | __/ _ \ / __/ _ \| '_ ` _ \ 
| |  | |_| | (_) | |_) | | | |_| \__ \ (_| (_| | ||  __/| (_| (_) | | | | | |
\_|   \__, |\___/|_.__/|_|  \__,_|___/\___\__,_|\__\___(_)___\___/|_| |_| |_|
       __/ |                                                                 
      |___/                                                                  
'''

print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(text)))

file = Write.Input("insert the name of the file -> ", Colors.red_to_yellow, interval=0.005)

def decrypt_string(value):
    try:
        try:
            def IIlIIIIIllIlllIIII(IIllIlllIllIllIIlI):
                return unpad(AES.new(hashlib.sha256(str(list(value)[0][0] + list(value)[1][0]).encode()).digest()[:24], AES.MODE_CBC, IIllIlllIllIllIIlI[:AES.block_size]).decrypt(IIllIlllIllIllIIlI[AES.block_size:]), AES.block_size).decode()
            return (IIlIIIIIllIlllIIII(value[1][2]))
        except:
            def IIlIIIIIllIlllIIII(IIllIlllIllIllIIlI):
                return unpad(AES.new(hashlib.sha256(str(list(value)[0][0] + list(value)[1][0][:-1]).encode()).digest()[:24], AES.MODE_CBC, IIllIlllIllIllIIlI[:AES.block_size]).decrypt(IIllIlllIllIllIIlI[AES.block_size:]), AES.block_size).decode()
            return (IIlIIIIIllIlllIIII(value[1][2]))
    except:
        def lIIIIIIllIlIIlIlIl(IIllIlllIllIllIIlI, IlllIlllIIIIlIIIll):
            IIllIlllIllIllIIlI = b85(IIllIlllIllIllIIlI)
            (IlllIlllIIIIlIIIll, IlIlllllllIIlIIlII) = llIIIIllIIIllIllIl(IlllIlllIIIIlIIIll, IIllIlllIllIllIIlI[:8])
            return AES.new(IlllIlllIIIIlIIIll, AES.MODE_CFB, IlIlllllllIIlIIlII).decrypt(IIllIlllIllIllIIlI[8:]).decode()

        def llIIIIllIIIllIllIl(lIllIIlIlIlIlIlIll, IlIIlIIIIIIIlIIllI):
            IllIllIllIIllllllI = hashlib.pbkdf2_hmac('sha256', lIllIIlIlIlIlIlIll.encode(), IlIIlIIIIIIIlIIllI, 100000)
            return (IllIllIllIIllllllI[:16], IllIllIllIIllllllI[16:])
        return (lIIIIIIllIlIIlIlIl(list(value.values())[0], list(value.keys())[0][1:-1]))
    
def find_multiline_value(lines, key):
    value_lines = []
    value_found = False
    
    for line in lines:
        if value_found:
            if line.strip() == '' or re.match(r'\w+\s*=', line):
                break
            value_lines.append(line.strip())
        else:
            match = re.search(rf'{key}\s*=\s*(.*)', line)
            if match:
                value_lines.append(match.group(1).strip())
                value_found = True

    if value_lines:
        return ' '.join(value_lines)
    return None

with open(file, "r") as f:
    lines = f.readlines()

    value_str = find_multiline_value(lines, 'pyobfuscate')
    if not value_str:
        value_str = find_multiline_value(lines, 'obfuscate')

    content_deobfuscated = decrypt_string(eval(value_str))

    with open("output.py", "w") as f:
        f.write(content_deobfuscated)
        
Write.Print("your file has been deobfuscated successfully and now the src code is in output.py! \n", Colors.red_to_yellow, interval=0.005)
