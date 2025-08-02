import json

a = open("C:/Users/Lovevett/Downloads/Programmieren/Irgendwas in HTML/Amsterdam/user.JSON")

b = json.load(a)

h = b["user"][0]["username"]

print(h)