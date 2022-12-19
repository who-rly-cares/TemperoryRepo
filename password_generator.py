example = "authn.edx.org"
import random

def encode(text):
    output = str()
    for i1 in text:
        for i2 in str(ord(i1)):
            output += chr(int(random.choice("23456789")+i2))
    return output

print(encode("example"))
