import config
import string
from utils.grid import generate_grid
from utils.output import print, clear_console
from utils.utility import prompt_for_grid_space, generate_empty_grid_data
from utils.saving import load_game_data, save_game_data
from config import AMOUNT_OF_BOATS

LETTER_KEYS = string.ascii_uppercase

def inject_border_row(grid_data, rows, columns):
    row_num = 0

    for row_id in range(rows):
        if row_id in grid_data:
            pass
        else:
            grid_data.append([])

        row_num += 1

        row = grid_data[row_id]
        row.insert(0, str(row_num))

    key_row = []
    for column_id in range(columns + 1):
        # First column is reserved for Row IDs
        column_key = column_id - 1
        if column_key >= 0 and LETTER_KEYS[column_key]:
            column_key = LETTER_KEYS[column_key]
        else:
            column_key = "F"

        key_row.append(column_key)
    grid_data.insert(0, key_row)

    return grid_data

def show_game():
    clear_console()

    # Load game data
    game_data = load_game_data()
    user_boats = game_data.get("user_boats")

    # Show grid and let user perform actions
    grid_mode = "bot"
    if len(user_boats) < AMOUNT_OF_BOATS:
        grid_mode = "user"

    grid_data = generate_empty_grid_data(config.GRID_SIZE_X, config.GRID_SIZE_Y)

    if grid_mode == "user":
        # Show user's boats on the grid
        for ship in user_boats:
            x = ship[0]
            y = ship[1]
            grid_data[y][x] = "B"
    
    transformed_grid_data = inject_border_row(grid_data, config.GRID_SIZE_X, config.GRID_SIZE_Y)
    
    grid = generate_grid(config.GRID_SIZE_X + 1, config.GRID_SIZE_Y + 1, transformed_grid_data)
    print(grid)

    if len(user_boats) < AMOUNT_OF_BOATS:
        print(f"Place a ship: ({len(user_boats)}/{AMOUNT_OF_BOATS})")
        x, y = prompt_for_grid_space()
        user_boats.append([x, y, "alive"])

    # Save game data
    save_game_data(user_boats)

    # Ask for continue
    continue_key = input("\nPress enter to continue, or X to go back to Main Menu ")
    if continue_key.lower() == "x":
        return ["change_screen", "menu"]
    return ["game", "continue"]