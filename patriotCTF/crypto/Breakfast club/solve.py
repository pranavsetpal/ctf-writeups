# from Crypto.Hash import *
from string import ascii_letters, digits

with open("attachments/BreakfastPasswords.txt", 'r') as f:
    lines = [ line[:-1] for line in f.readlines() ]

password = ""

for line in lines:
    alg_type, ct = line.split()

    for c in [
        *"{}_!@#$%^&*()",
        *ascii_letters,
        *digits
    ]:
        exec(f"from Crypto.Hash import {alg_type} as alg")
        c_hash = alg.new()
        c_hash.update(c.encode())
        c_hash = c_hash.hexdigest()
        if c_hash == ct:
            password += c
            break
    else:
        password += '.'

print(password)
