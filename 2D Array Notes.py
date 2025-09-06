color_grid = [
    ["Red", "Green", "Blue"],
    ["Yellow", "Purple", "Cyan"],
    ["Orange", "Pink", "Gray"],
]

print("Elements at (0, 0):", color_grid[0][0])
print("Elements at (1, 2):", color_grid[1][2])

color_grid[2][1]= "Magenta"
print("Modified color-grid")
for row in color_grid:
    print(row)

new_row = ["Black", "White", "Brown"]
color_grid.append(new_row)
print("2D array after adding a new row:")
for row in color_grid:
    print(row)

color_grid.pop(1)
print("2D array after removing the second row:")
for row in color_grid:
    print(row)



print("Iterating over each element in the 20 array:")
for row in color_grid:
    for color in row:
        print(color, end=" ")
    print()



rows = len(color_grid)
columns = len(color_grid[0]) if rows > 0 else 0
print(f"Dimensions of the 2D array: {rows}x{columns}")