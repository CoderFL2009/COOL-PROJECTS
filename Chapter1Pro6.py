"""
Programmer: Sidd
Program: List
Output
A report in tabular format. Each line has the form (last name, hours worked, totalwages)
"""
fileName = input("Enter the file name: ")

inputFile = open(fileName, 'r')

print("%-15s%6s%15s" % ("Name", "Hours", "Total Pay"))
for line in inputFile:
    dataList = line.split()
    name = dataList[0]
    hours = int(dataList[1])
    payRate = float(dataList[2])
    totalPay = hours * payRate
    print("%-15s%6s%15s.2" % (name, hours, totalPay))