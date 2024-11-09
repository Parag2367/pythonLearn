with open("dsa.pdf", "rb") as f:
    data = f.read()

with open("dsa.pdf", "ab") as f:
    f.write(data)
