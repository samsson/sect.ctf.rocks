#ezdos challenge

import string
import binascii

lista = [0x66,0x79,0x74, 0x79]
keys = [0x53,0x48, 0x45, 0x4c]
val1 = []
string1 = ""

def xor():
    for i in range(len(lista)):
        val1.append(lista[i] ^ keys[i])

xor()
for item in val1:
    string1 = string1 + chr(item)
print("1337-" + string1)

