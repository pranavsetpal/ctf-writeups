This challenge was pretty basic as well. The attachments included CT, P, Q and E (in images)

The images all had numbers used in the RSA cipher system!
CT -> Ciphertext
P -> 1st prime number
Q -> 2nd prime number
E -> Public Key

Using P and Q, we were albe to calculate the totient, and on dividing it by E, get the private key. Deciphering the ciphertext gave us the flag
![Flag]("./flag.png")
