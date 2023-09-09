from string import punctuation

alphabet = list(punctuation)
data = "bHEC_T]PLKJ{MW{AdW]Y"
key = '$'
decrypted = ''.join([chr(ord(x) ^ ord(key)) for x in data])
print(decrypted)
