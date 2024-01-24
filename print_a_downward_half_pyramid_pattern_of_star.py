# Print a downward half-pyramid pattern of stars

def print_downward_half_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

# Number of rows for the downward half-pyramid
num_rows = 5

# Print the pattern
print_downward_half_pyramid(num_rows)