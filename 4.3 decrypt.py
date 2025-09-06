"""
4.3 decrypt
"""
inName = input("Enter the input file name: ")
outName = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))

inputFile = open(inName, 'r')
code = inputFile.read()

outFile = open(outName, 'w')
plainText = ''
for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < 0:
        cipherValue = 127 - \
                      (distance - (1 - ordValue))
    plainText +=  chr(cipherValue)
outFile.write(plainText)
outFile.close()