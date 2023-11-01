import re
import ast
import base64
import hashlib

from Crypto.Cipher import AES
from pystyle import Center, Anime, Colors, Colorate, System, Write

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

def derive_key_and_iv(password, salt):
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    key = dk[:16]
    iv = dk[16:]
    return key, iv

def aes_decrypt(encrypted_data, key):
    encrypted_data = base64.b85decode(encrypted_data)
    salt = encrypted_data[:8]
    key, iv = derive_key_and_iv(key, salt)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    data = cipher.decrypt(encrypted_data[8:])
    return data.decode()

with open(file, "r") as f:
    lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        match = re.search(r'obfuscate = (.+)', line)
        if match:
            obfuscate_str = match.group(1)
            line_number = i
            break

    if(".replace('\\n','')]))") in obfuscate_str:
        pass
    else:
        while(".replace('\\n','')]))" not in obfuscate_str):
            obfuscate_str+=lines[line_number]
            line_number+=1
    
    obfuscate = str(eval(obfuscate_str))

    dictionary = ast.literal_eval(obfuscate)

    encrypted_data = list(dictionary.values())[0]
    key = list(dictionary.keys())[0][1:-1]

with open("output.py", "w", encoding="utf-8") as f:
    f.write(aes_decrypt(encrypted_data,key))
    Write.Print("your file has been deobfuscated successfully and now the src code is in output.py! \n", Colors.red_to_yellow, interval=0.005)