"""
4.3 encrypt
"""
inName = input("Enter the input file name: ")
outName = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))

inputFile = open(inName, 'r')
plainText = inputFile.read()

outFile = open(outName, 'w')
code = ""
for ch in plainText:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > 127:
        cipherValue = distance - (127 - ordValue + 1)
    code +=  chr(cipherValue)
outFile.write(code)
outFile.close()

