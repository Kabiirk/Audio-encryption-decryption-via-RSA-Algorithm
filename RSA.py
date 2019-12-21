from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt


#Reading the audio file if it is in the same directory
fs, data = wavfile.read('boing2.wav')
plt.plot(data)
plt.title("Original Audio Plot")
k = np.asarray(data, dtype = np.int32)


#Generating Public and Private Key
p1 = int(input("Enter first prime number: "))
p2 = int(input("Enter second prime number: "))

n = p1*p2
print("n = p1*p2 = ",n)

e = int(input("Enter a small, odd number, co-prime with n: "))
k = int(input("Enter value of k:"))

phi = (p1-1)*(p2-1)
print("phi = ",phi)

d = int((k*phi+1)/e)

print("d= ",d)

public_key = n,e
private_key = n,d

print("Public Key = ", public_key)
print("Private Key = ",private_key)


#Encrypting message via public Key
encrypted = (k**e)%n
plt.plot(encrypted)
plt.title("Encrypted Audio Plot")


#Writing the encrypted file into an audio file and plotting it
encrypted = np.asarray(encrypted,dtype=np.int16)
wavfile.write('encrypted.wav',fs,encrypted)
print("A file titled 'encrypted.wav' is generated which is the encrypted audio to be communicated")
fs, Data = wavfile.read('encrypted.wav')
plt.plot(Data)


#Decrypting the file and plotting it for comparison
ke = np.asarray(Data, dtype = np.int32)
decrypted = (encrypted**d)%n
plt.plot(k)
plt.title('Decrypted Audio Plot')


#Writing the decrypted file into an audio file and plotting it
encrypted = np.asarray(encrypted,dtype=np.int16)
wavfile.write('decrypted.wav',fs,encrypted)
print("A file titled 'decrypted.wav' is generated which is analog of the audio")