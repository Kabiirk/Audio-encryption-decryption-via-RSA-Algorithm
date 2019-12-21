# The Algorithm
Select two prime no's. Suppose **P = a** and **Q = b**. 
Now First part of the __Public key : n = P*Q = ab__.

Now take an integer **e** such that , it is an integer and not a factor of **n**
Also , **1 < e < Ф**
[Ф = (a-1)*(b-1)]

Such that **Φ(n) = (a-1)(b-1)**

Calculate Private Key : 
**d = (k*Φ(n) + 1) / e** 

**_For example:_**
Say we have **P = 53** and **Q = 59**
Now First part of the Public key  : **n = P*Q = 3127**

After putting values in the formula
Now we are ready with our **Public Key ( n = 3127)**, **e** and **Private Key (d = 2011)**

# An Example:

Now we will encrypt **“HI”** :

Convert letters to numbers : **H = 8** and **I = 9** 

Thus **Encrypted Data c = 89<sup>e</sup> mod n**. Thus our Encrypted Data comes out to be 1394 Now we will decrypt 1394 .

**Decrypted Data = c<sup>d</sup> mod n**. Thus our Encrypted Data comes out to be 89 

**8 = H** and **I = 9** 

i.e. "HI

And with this we get our original message back !
