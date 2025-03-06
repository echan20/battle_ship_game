from utils.output import input_custom
from config import GRID_SIZE_X, GRID_SIZE_Y
import string

LETTER_KEYS = string.ascii_uppercase

def prompt_for_grid_space():
    allowed_x_spaces = []
    allowed_x_spaces_map = {}
    for column_key in range(GRID_SIZE_X):
        letter = LETTER_KEYS[column_key]
        allowed_x_spaces.append(letter)
        allowed_x_spaces_map[letter] = column_key

    allowed_y_spaces = []
    allowed_y_spaces_map = {}
    for row_key in range(GRID_SIZE_Y):
        allowed_y_spaces.append(str(row_key + 1))
        allowed_y_spaces_map[str(row_key + 1)] = row_key

    def validate_grid_input(input_text):
        # Check if input has a valid column and row in either order
        if len(input_text) != 2:
            return False
            
        char1, char2 = input_text[0].upper(), input_text[1].upper()
        
        # Case 1: column then row (e.g: "A1")
        case1_valid = (char1 in allowed_x_spaces and char2 in allowed_y_spaces)
        
        # Case 2: row then column (e.g: "1A")
        case2_valid = (char1 in allowed_y_spaces and char2 in allowed_x_spaces)
        
        # Return true if either case is valid
        return case1_valid or case2_valid
    
    grid_input = input_custom("Enter coordinates (e.g. A1): ", validate_grid_input)
    char1, char2 = grid_input[0].upper(), grid_input[1].upper()
    
    # Determine which format was used (A1 or 1A) and return the correct coordinates
    if char1 in allowed_x_spaces and char2 in allowed_y_spaces:
        # Format is A1 (column then row)
        return allowed_x_spaces_map[char1], allowed_y_spaces_map[char2]
    else:
        # Format is 1A (row then column)
        return allowed_x_spaces_map[char2], allowed_y_spaces_map[char1]

def generate_empty_grid_data(grid_size_x, grid_size_y):
    grid_data = []

    for _ in range(grid_size_x):
        row = []
        for _ in range(grid_size_y):
            row.append("")
        grid_data.append(row)

    return grid_data