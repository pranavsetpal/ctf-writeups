from Crypto.Util.number import long_to_bytes
from base64 import b64decode

with open("./Challenge.txt", 'r') as f:
    cipher = f.read()

dec_cipher = long_to_bytes(int(cipher, 2)).decode()
hex_cipher = ''.join([chr(int(char)) for char in dec_cipher.split()])
b64_cipher = ''.join([chr(int(char, 16)) for char in hex_cipher.split()])
flag = b64decode(b64_cipher).decode()

print(flag)
