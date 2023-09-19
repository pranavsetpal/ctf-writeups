This challenge was pretty straight-forward.

Our challenge consisted of binary. On converting into a string, we got a string of ascii numbers.
![Decimal Cipher](./decimal_cipher.png)

Converting these ascii values to their characters gives us another set of ascii numbers, this time in hex.
![Hex Cipher](./hex_cipher.png)

Converting these values to their characters reveals a base64 text. Decoding that finally gives us the flag!
![Base64 Cipher](./base64_cipher.png)
![Flag](./flag.png)
