"""
Encrypts an input string of the ASCII characters and prints the result
"""

plainText = input("Enter a message")
distance = int(input("Enter the distance value"))
code = ""
for ch in plainText:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > 127:
        cipherValue = distance - (127 - ordValue + 1)
    code +=  chr(cipherValue)
print(code)