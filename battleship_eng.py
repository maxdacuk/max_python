import random  # Importing the module for working with random numbers

def generate_empty_map(size):
    """
    Creates an empty map of the given size.
    :param size: Size of the map (number of cells on one side).
    :return: A two-dimensional list filled with "~" characters.
    """
    return [['~' for _ in range(size)] for _ in range(size)]  # Generating a map filled with "~" (water)

def print_map(game_map):
    """
    Prints the map in a user-friendly format.
    :param game_map: A two-dimensional list (map).
    """
    # Printing column numbers (1, 2, 3, ...)
    print("  " + " ".join(map(str, range(1, len(game_map) + 1))))
    for idx, row in enumerate(game_map):  # Iterating through the rows of the map with their indices
        # Printing the row number (aligned to take up 2 spaces) and its content
        print(f"{idx + 1:2}" + " ".join(row))

def is_area_free(game_map, row, col, ship_size, orientation):
    """
    Checks if the area around the ship is free, including a buffer of 1 cell around it.
    :param game_map: A two-dimensional list (map).
    :param row: Starting row for the ship.
    :param col: Starting column for the ship.
    :param ship_size: Size of the ship.
    :param orientation: Orientation of the ship ('horizontal' or 'vertical').
    :return: True if the area is free, False otherwise.
    """
    size = len(game_map)
    for r in range(row - 1, row + (ship_size if orientation == 'vertical' else 1) + 1):
        for c in range(col - 1, col + (ship_size if orientation == 'horizontal' else 1) + 1):
            if 0 <= r < size and 0 <= c < size and game_map[r][c] != '~':
                return False
    return True

def place_ships(game_map, ship_sizes):
    """
    Places ships on the map.
    :param game_map: A two-dimensional list (map).
    :param ship_sizes: A list of ship sizes.
    """
    size = len(game_map)  # Storing the size of the map
    for ship_size in ship_sizes:  # Iterating through the sizes of the ships
        placed = False  # Flag to check if the ship has been placed
        while not placed:  # Repeat until the ship is placed
            orientation = random.choice(['horizontal', 'vertical'])  # Randomly choose an orientation

            if orientation == 'horizontal':
                row = random.randint(0, size - 1)  # Random row
                col = random.randint(0, size - ship_size)  # Random column (considering the ship's length)
                # Check if the area is free
                if is_area_free(game_map, row, col, ship_size, orientation):
                    # If the area is free, place the ship
                    for i in range(ship_size):
                        game_map[row][col + i] = '×'  # Mark the cell with a ship
                    placed = True  # The ship has been placed

            else:  # Vertical orientation
                row = random.randint(0, size - ship_size)  # Random row (considering the ship's length)
                col = random.randint(0, size - 1)  # Random column
                # Check if the area is free
                if is_area_free(game_map, row, col, ship_size, orientation):
                    # If the area is free, place the ship
                    for i in range(ship_size):
                        game_map[row + i][col] = '×'  # Mark the cell with a ship
                    placed = True  # The ship has been placed

# Main program
map_size = 10  # Setting the map size
ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]  # Ship sizes

# Generate an empty map
sea_map = generate_empty_map(map_size)

# Place the ships on the map
place_ships(sea_map, ships)

# Print the map
print("Map for the Battleship game:")
print_map(sea_map)
