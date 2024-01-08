import re

from hashlib import sha256
from pystyle import Center, Colors, Colorate, System, Write
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

System.Clear()
System.Title("Pyobfuscate.com deobfuscator by over_on_top")
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

def decrypt_string(encrypted_data, pyobfuscate_str):
    return unpad(
        AES.new(
            sha256(str(list(pyobfuscate_str)[0][0] + list(pyobfuscate_str)[1][0]).encode()).digest()[:24],
            AES.MODE_CBC,
            encrypted_data[:AES.block_size]
        ).decrypt(encrypted_data[AES.block_size:]),
        AES.block_size
    ).decode()

with open(file, "r") as f:
    lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        match = re.search(r'pyobfuscate = (.+)', line)
        if match:
            pyobfuscate_str = match.group(1)
            break

    pyobfuscate_str = eval(pyobfuscate_str)

    encrypted_data = pyobfuscate_str[1][2]

    content_deobfuscated = decrypt_string(encrypted_data,pyobfuscate_str)

    with open("output.py", "w") as f:
        f.write(content_deobfuscated)
        
Write.Print("your file has been deobfuscated successfully and now the src code is in output.py! \n", Colors.red_to_yellow, interval=0.005)
