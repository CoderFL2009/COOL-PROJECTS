def main():
    """Tests the functions"""
    lyst = [3,1,7,1,4,10]
    print("List:", lyst)
    print("Mode:", mode(lyst))
    print("Median:", median(lyst))
    print("Mean:", mean(lyst))

def mean(lyst):

    sum = 0
    for number in lyst:
        sum += number
    if len(lyst)== 0:
        return 0
    else:
        return sum / len(lyst)

def mode(lyst):

    theDictionary = {}
    for number in lyst:
        freq = theDictionary.get(number, None)
        if freq == None:
            theDictionary[number] = 1
        else:
            theDictionary[number] = freq + 1

    if len(theDictionary) == 0:
        return 0
    else:
        theMaximum = max(theDictionary.values())
        for key in theDictionary:
            if theDictionary[key] == theMaximum:
                return key

def median(lyst):
    numbers = []
    for number in lyst:
        numbers.append(number)
    numbers.sort()
    if len(numbers) == 0:
        return 0
    else:
        midpoint = len(numbers) // 2
        if len(numbers) % 2 == 1:
            return numbers[midpoint]
        else:
            return (numbers[midpoint] + numbers[midpoint - 1]) / 2

if __name__ == "__main__":
    main()

