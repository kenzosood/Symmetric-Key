from cryptography.fernet import Fernet

print("This Program will create a symmetric key to encrypt the data")
print("Enter a Message you want to Encrypt") 

print("This Program will Display original message from Your Encrypted Data using the Symmetric Key you have ")


num = input("enter you Symmetric Key")

key = num.encode()
f = Fernet(key)


msg = input("Enter Your encryption here: ")
message = msg.encode()
enc = f.decrypt(message)

print(enc )
print(" is your Message behind Encrypted Data")