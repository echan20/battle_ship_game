from utils.output import input_custom
from config import GRID_SIZE_X, GRID_SIZE_Y
import string
import random

LETTER_KEYS = string.ascii_uppercase

def prompt_for_grid_space(validator=None):
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
    x = 0
    y = 0
    if char1 in allowed_x_spaces and char2 in allowed_y_spaces:
        # Format is A1 (column then row)
        x, y = allowed_x_spaces_map[char1], allowed_y_spaces_map[char2]
    else:
        # Format is 1A (row then column)
        x, y = allowed_x_spaces_map[char2], allowed_y_spaces_map[char1]

    # Custom validator
    if (validator):
        valid = validator(x, y)
        if (valid != True):
            return prompt_for_grid_space()
        
    return x, y

def generate_random_grid_space(grid_size_x, grid_size_y):
    x = random.randint(0, grid_size_x - 1)
    y = random.randint(0, grid_size_y - 1)
    return x, y

def generate_empty_grid_data(grid_size_x, grid_size_y):
    grid_data = []

    for _ in range(grid_size_x):
        row = []
        for _ in range(grid_size_y):
            row.append("")
        grid_data.append(row)

    return grid_data

def check_hit(boats, x, y):
    for boat in boats:
        boatX = boat[0]
        boatY = boat[1]
        if (boatX == x and boatY == y):
            return boat
    return None

def generate_place_ships_validator(user_boats):
    def validator(x, y):
        boat = check_hit(user_boats, x, y)
        if boat:
            print("This space has already been taken!")
            return False
        return True

    return validator

def merge_with_offset(str1, str2, offset):
    """Merge two multi-line strings horizontally with an offset.
    
    Args:
        str1: First string (can be multi-line).
        str2: Second string (can be multi-line).
        offset: Number of spaces between the end of str1's lines and str2's lines.
        
    Returns:
        Merged string with aligned lines.
    """
    lines1 = str1.split('\n')
    lines2 = str2.split('\n')
    max_lines = max(len(lines1), len(lines2))
    
    # Pad shorter string with empty lines
    lines1 += [''] * (max_lines - len(lines1))
    lines2 += [''] * (max_lines - len(lines2))
    
    # Merge line-by-line with offset
    merged = [f"{line1}{' ' * offset}{line2}" for line1, line2 in zip(lines1, lines2)]
    return '\n'.join(merged)

def all_boats_dead(boats):
    for boat in boats:
        status = boat[2]
        if status != "dead":
            return False
    return True

ANNOTATE_OPTIONS = [
    ["invert_background", "7"],
    ["bold_text", "1"],
    ["yellow_background", "43"],
    ["green_background", "42"],
    ["red_background", "41"],
]
# uses ANSI to print colored text
def annotate_text(text: str, options):
    annotate_codes = []

    for option_data in ANNOTATE_OPTIONS:
        option = option_data[0]
        code = option_data[1]

        if option in options:
            annotate_codes.append(code)

    if len(annotate_codes) > 0:
        codes = ";".join(annotate_codes)
        annotated_text = f'\033[{codes}m{text}\033[0m'
        return annotated_text
    else:
        return text