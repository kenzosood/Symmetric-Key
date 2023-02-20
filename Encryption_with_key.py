from cryptography.fernet import Fernet


print("This Program will create an Encryption for Your Message using the Symmetric Key you have")

k = input("Enter Your Symmetric Key: ")

key = k.encode()

print (key )

f = Fernet(key)

msg = input("Enter Your Message here: ")
message = msg.encode()
enc = f.encrypt(message)


print("Your Encrypted Data is: ")
print(enc)