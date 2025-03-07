import config
import string
from utils.grid import generate_grid
from utils.output import print, clear_console
from utils.utility import prompt_for_grid_space, generate_empty_grid_data, generate_place_ships_validator, generate_random_grid_space, check_hit
from utils.saving import load_game_data, save_game_data
from config import AMOUNT_OF_BOATS, GRID_SIZE_X, GRID_SIZE_Y, DEBUG_SHOW_BOT_BOATS

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

def show_game(override_show_grid_mode=None):
    clear_console()

    skip_continue_prompt = False
    show_updated_grid = False

    # Load game data
    game_data = load_game_data()
    user_boats = game_data.get("user_boats")
    user_misses = game_data.get("user_misses")
    bot_boats = game_data.get("bot_boats")
    bot_misses = game_data.get("bot_misses")

    # Show grid
    grid_mode = "bot"
    if len(user_boats) < AMOUNT_OF_BOATS:
        grid_mode = "user"

    if override_show_grid_mode:
        grid_mode = override_show_grid_mode

    grid_data = generate_empty_grid_data(GRID_SIZE_X, GRID_SIZE_Y)

    if grid_mode == "user":
        print(" User's Grid:")
        # Show user's boats on the grid
        for ship in user_boats:
            x = ship[0]
            y = ship[1]
            status = ship[2]
            if status == "alive":
                grid_data[y][x] = "B"
            else:
                grid_data[y][x] = "H"

        # Show bot's misses on the grid
        for miss in bot_misses:
            x = miss[0]
            y = miss[1]
            grid_data[y][x] = "M"
    else:
        print(" Bot's Grid:")
        # [DEBUG] Show bot's boats on the grid
        if DEBUG_SHOW_BOT_BOATS:
            for ship in bot_boats:
                x = ship[0]
                y = ship[1]
                status = ship[2]
                if status == "alive":
                    grid_data[y][x] = "B"
                else:
                    grid_data[y][x] = "H"

        # Show user's misses on the grid
        for miss in user_misses:
            x = miss[0]
            y = miss[1]
            grid_data[y][x] = "M"
    
    transformed_grid_data = inject_border_row(grid_data, GRID_SIZE_X, GRID_SIZE_Y)
    
    grid = generate_grid(GRID_SIZE_X + 1, GRID_SIZE_Y + 1, transformed_grid_data)
    print(grid)

    if (not override_show_grid_mode):
        # Perform Automatic Actions
        while len(bot_boats) < AMOUNT_OF_BOATS:
            x, y = generate_random_grid_space(GRID_SIZE_X, GRID_SIZE_Y)
            bot_boats.append([x, y, "alive"])

        # Perform User Actions
        if len(user_boats) < AMOUNT_OF_BOATS:
            # Let user place boats first
            print(f"Place a ship: ({len(user_boats)}/{AMOUNT_OF_BOATS})")
            x, y = prompt_for_grid_space(generate_place_ships_validator(user_boats))
            user_boats.append([x, y, "alive"])
            skip_continue_prompt = True
        else:
            # Main game
            # Prompt for grid space to hit
            print(f"Target Coordinates:")
            x, y = prompt_for_grid_space()
            boat = check_hit(bot_boats, x, y)
            if boat:
                boat[2] = "Dead"
                print("Hit!")
            else:
                print("Miss!")
                user_misses.append([x, y])

            # Bot's turn to hit
            x, y = generate_random_grid_space(GRID_SIZE_X, GRID_SIZE_Y)
            boat = check_hit(user_boats, x, y)
            if boat:
                boat[2] = "Dead"
            else:
                bot_misses.append([x, y])

            show_updated_grid = True

    # Save game data
    save_game_data(user_boats, user_misses, bot_boats, bot_misses)

    if show_updated_grid:
        return show_game(override_show_grid_mode=grid_mode)

    # Ask for continue
    if (skip_continue_prompt != True):
        continue_key = input("\nPress enter to continue, or X to go back to Main Menu ")
        if continue_key.lower() == "x":
            return ["change_screen", "menu"]
        
    if override_show_grid_mode == "bot":
        return show_game(override_show_grid_mode="user")
    
    return ["game", "continue"]