# Audio Encryption and Decryption using RSA Algorithm

## What is RSA Algorithm ?
It is an [Asymmetric cryptography algorithm](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/). Asymmetric actually means that it works on two different keys i.e. Public Key and Private Key. As the name describes that the Public Key is given to everyone and Private key is kept private.

#### An example of asymmetric cryptography :
1. Say a _'Person A'_ sends his/her public key to the server and requests for some data.
2. The server encrypts the data using Person A’s public key and sends the encrypted data.
3. Say a _'Person B'_ receives this data and decrypts it.
4. Since this is asymmetric, nobody else except browser can decrypt the data even if a third party has public key of browser.

The Idea Behind RSA Algorithm
------
The main striving force behind effectiveness is that larger the number, more the time taken to prime factorize a number increases exponentially.

The public key consists of two numbers where one number is multiplication of two large prime numbers. And private key is also derived from the same two prime numbers. 
So if somebody can factorize the large number, the private key is compromised.Therefore encryption strength totally lies on the key size and if we double or triple the key size, the strength of encryption increases exponentially.


![alt Text](https://www.javamex.com/tutorials/cryptography/RSADecryptionTime.png "A graph I found on Google")

I believe [this](https://www.khanacademy.org/computing/computer-science/cryptography/modern-crypt/v/the-fundamental-theorem-of-arithmetic-1) tutorial from Khan Academy does a better job of explaining workings of the RSA Algorithm than I ever could. Kudos to Khan Academy on an amazing series of lectures regarding the subject Matter !
