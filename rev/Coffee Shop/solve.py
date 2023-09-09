from base64 import b64decode

encoded_string = "R2FsZUJvZXR0aWNoZXI="
string = b64decode(encoded_string).decode()
flag = f"CACI{{{string}}}"

print(flag)
