import time

def read_numbers_from_file(input_file):
    """Read numbers from a text file and return them as a list of integers"""
    with open(input_file, 'r')as file:
        numbers = [int(line.strip()) for line in file.readlines()]
    return numbers


def write_numbers_to_file(output_file, numbers):
    """Write the sorted numbers to a new file"""
    with open(output_file, 'w')as file:
        for number in numbers:
            file.write(f"{number}\n")


def bubble_Sort(numbers):
    n = len(numbers)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if numbers[j]>numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers [j]

def main():
    input_file = '100000Numbers.txt'
    output_file = 'BubbleSorted_output.txt'

    numbers = read_numbers_from_file(input_file)
    start_time = time.time()
    bubble_Sort(numbers)
    end_time = time.time()
    elapsed_time = end_time-start_time
    print(f"Time taken to perform bubble sort: {elapsed_time:.4f} seconds")
    write_numbers_to_file(output_file,numbers)

if __name__== "__main__":
    main()