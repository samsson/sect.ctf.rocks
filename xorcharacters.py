import string
import binascii

lista = [0x66,0x79,0x74, 0x79]
keys = [0x53,0x48, 0x45, 0x4c]
val1 = []
string1 = ""
def xor3():
    for i in range(len(lista)):
        #print(i)
        val1.append(lista[i] ^ keys[i])

xor3()
for item in val1:
    string1 = string1 + chr(item)
print("1337-" + string1)

#
#            if d == i:
#                print(d)
#Key = 0x1c 0x33, 0x33, 0x37, 0x53
#Key = 1 + 0x1e + 0x55 + 0x4e + 0x27
# 1337-5115
#
