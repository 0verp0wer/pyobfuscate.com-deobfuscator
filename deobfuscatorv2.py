import re
import hashlib

from base64 import b85decode
from pystyle import Center, Colors, Colorate, System, Write
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

System.Clear()
System.Title("pyobfuscate.com deobfuscator v2 by over_on_top")
System.Size(130, 30)

def deobfuscate(pyc, pye, httpspyobfuscatecom):
    def d(b, p):
        c = b85decode(b.encode('utf-8'))
        r = AES.new(PBKDF2(p, c[:16], dkLen=32, count=1000000), AES.MODE_GCM, nonce=c[16:32])
        return r.decrypt_and_verify(c[48:], c[32:48]).decode('utf-8')
    return(d(pyc + pye, httpspyobfuscatecom.replace('"', '')))

text = '''
                               _      __                     _                            
             _ __  _   _  ___ | |__  / _|_   _ ___  ___ __ _| |_ ___   ___ ___  _ __ ___  
            | '_ \| | | |/ _ \| '_ \| |_| | | / __|/ __/ _` | __/ _ \ / __/ _ \| '_ ` _ \ 
            | |_) | |_| | (_) | |_) |  _| |_| \__ \ (_| (_| | ||  __/| (_| (_) | | | | | |
            | .__/ \__, |\___/|_.__/|_|  \__,_|___/\___\__,_|\__\___(_)___\___/|_| |_| |_|
            |_|    |___/                   ____ 
                                    __   _|___ \ 
                                    \ \ / / __) |
                                     \ V / / __/ 
                                      \_/ |_____|                                                  
'''

print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(text)))

file = Write.Input("insert the name of the file -> ", Colors.red_to_yellow, interval=0.005)

with open(file, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.strip().startswith("pyobfuscate("):
        pyobfuscate_value = lines[i]
        
        pyc_value = re.search(r"'pyc'\s*:\s*\"\"\"(.*?)\"\"\"", pyobfuscate_value, re.DOTALL).group(1)
        pye_value = re.search(r"'pye'\s*:\s*\"\"\"(.*?)\"\"\"", pyobfuscate_value, re.DOTALL).group(1)
        httpspyobfuscatecom = re.search(r"['\"]([lI]+)['\"]", pyobfuscate_value, re.DOTALL).group(0)
        content = deobfuscate(pyc_value, pye_value, httpspyobfuscatecom)
        break
    
with open("out.py", "w") as f:
    f.write(content)
    
Write.Print("your file has been deobfuscated successfully and now the src code is in out.py! \n", Colors.red_to_yellow, interval=0.005)
