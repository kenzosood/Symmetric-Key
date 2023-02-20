from cryptography.fernet import Fernet

key = Fernet.generate_key()

print("This Python Script will Provide you a Symmetric Key Which can be used to Encrypt any Message ")
print("     and this key will also be used to Decrypt the message       ")

input("Hit Enter")

print("your Symmetric Key is " )
print(key)