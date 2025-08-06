from cryptography.fernet import Fernet #type:ignore
import json

with open("C:/Users/Lovevett/Downloads/Programmieren/Irgendwas in HTML/Amsterdam/secret_key.key") as f:
    key = f.read().encode("utf-8")

fernet = Fernet(key)

b = json.load(open("C:/Users/Lovevett/Downloads/Programmieren/Irgendwas in HTML/Amsterdam/user.JSON"))

encrypted_username, encrypted_password = b["user"][0]["username"].encode("utf-8"), b["user"][1]["password"].encode("utf-8")

#print(encrypted_username, encrypted_password)

decrypted_username, decrypted_password = (fernet.decrypt(encrypted_username)).decode("utf-8"), (fernet.decrypt(encrypted_password)).decode("utf-8")

print(decrypted_username, decrypted_password)
