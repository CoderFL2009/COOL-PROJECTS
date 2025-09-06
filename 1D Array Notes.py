my_array = [10, 20, 30, 40, 50]

print("First element:", my_array[0])
print("Second element:", my_array[1])

my_array[2] = 60
print("Modified Array: ", my_array)

my_array.append(70)
print("Array after appending 70:", my_array)

my_array.remove(40)
print("Array after removing 40:", my_array)

print("iterating over the array:")
for elements in my_array:
    print(elements)

print("Length of the array:", len(my_array))