#Loops that count through a range of numbers are also called count-controll
product = 1

for count in range(4):
    print(count, product)
    product = product * (count +1)
    print(count, product)