colors_cube = [
    [#1st layer (Depth 0)
        ["Red", "Green", "Blue"],
        ["Yellow", "Pink", "Cyan"]
    ],
    [#2nd layer (Depth 1)
        ["Orange", "Purple", "Gray"],
        ["Black", "White", "Brown"]
    ],
    [#1st layer (Depth 0)
        ["Violet", "Indigo", "Teal"],
        ["Lime", "Magenta", "Maroon"]
    ]
]

print("Elements at (0, 0, 0):", colors_cube[0][0][0])
print("Elements at (1, 1, 2):", colors_cube[1][1][2])
print("Elements at (2, 0, 1):", colors_cube[2][0][1])

colors_cube[1][0][2] = "Silver"
print("Modified color_grid")
for layer in colors_cube:
    for row in layer:
        print(row)
    print()


new_layer = [
        ["Crimson", "Olive", "Turquoise"],
        ["Gold", "Peach", "Lavender"]
]
colors_cube.append(new_layer)
print("3D array after adding a new layer:")
for layer in colors_cube:
    for row in layer:
        print(row)
    print()

colors_cube.pop(0)
print("3D array after removing the first row:")
for layer in colors_cube:
    for row in layer:
        print(row)
    print()

print("Iterating over each element in the 3D array:")
for layer in colors_cube:
    for row in layer:
        for color in row:
            print(color, end=" ")
        print()
    print()


depth = len(colors_cube)
rows = len(colors_cube[0]) if depth > 0 else 0
columns = len(colors_cube[0][0]) if rows > 0 else 0
print(f"Dimensions of the 3D array: {depth}x{rows}x{columns}")


