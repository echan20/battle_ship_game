import string
from utils.grid import generate_grid
from utils.output import print, clear_console
from utils.utility import prompt_for_grid_space, generate_empty_grid_data, generate_place_ships_validator, generate_random_grid_space, check_hit, merge_with_offset, all_boats_dead, annotate_text
from utils.saving import load_game_data, save_game_data
from config import AMOUNT_OF_BOATS, GRID_SIZE_X, GRID_SIZE_Y, DEBUG_SHOW_BOT_BOATS

LETTER_KEYS = string.ascii_uppercase

def inject_border_row(grid_data, rows, columns, special_boxes=None):
    row_num = 0

    for row_id in range(rows):
        if row_id in grid_data:
            pass
        else:
            grid_data.append([])

        row_num += 1

        row = grid_data[row_id]
        row.insert(0, str(row_num))

        if special_boxes:
            special_boxes.append([0, row_id + 1, "bold_text"])

    key_row = []
    for column_id in range(columns + 1):
        # First column is reserved for Row IDs
        column_key = column_id - 1
        if column_key >= 0 and LETTER_KEYS[column_key]:
            column_key = LETTER_KEYS[column_key]
        else:
            column_key = "F"

        key_row.append(column_key)

        if special_boxes:
            special_boxes.append([column_id, 0, "bold_text"])

    grid_data.insert(0, key_row)

    return grid_data

grid_instructions = "\n".join([
    annotate_text(" Green Text shows alive boats. ", ["green_background"]),
    annotate_text(" Red Text shows sunk boats. ", ["red_background"]),
    annotate_text(" White text shows last target. ", ["invert_background"]),
])

def show_game(override_show_grid_mode=None, user_grid_special_boxes=None, bot_grid_special_boxes=None):
    clear_console()

    # Initialize variables needed
    skip_continue_prompt = False
    show_updated_grid = False

    # Cannot define up there, the references are reused in the next function call, which is not ideal.
    if (not user_grid_special_boxes):
        user_grid_special_boxes = []
    if (not bot_grid_special_boxes):
        bot_grid_special_boxes = []

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

    user_grid_data = generate_empty_grid_data(GRID_SIZE_X, GRID_SIZE_Y)
    bot_grid_data = generate_empty_grid_data(GRID_SIZE_X, GRID_SIZE_Y)

    # User's Grid
    # Show user's boats on the grid
    for ship in user_boats:
        x = ship[0]
        y = ship[1]
        status = ship[2]
        if status == "alive":
            user_grid_data[y][x] = "B"
            user_grid_special_boxes.append([x + 1, y + 1, "green_background"])
        else:
            user_grid_data[y][x] = "H"
            user_grid_special_boxes.append([x + 1, y + 1, "red_background"])

    # Show bot's misses on the grid
    for miss in bot_misses:
        x = miss[0]
        y = miss[1]
        user_grid_data[y][x] = "M"
    
    # Bot's Grid
    # [DEBUG] Show bot's boats on the grid
    for ship in bot_boats:
        x = ship[0]
        y = ship[1]
        status = ship[2]
        if status == "alive":
            # Show bot's boats only if debug mode is enabled
            if DEBUG_SHOW_BOT_BOATS:
                bot_grid_data[y][x] = "B"
                bot_grid_special_boxes.append([x + 1, y + 1, "green_background"])
        else:
            # Show bot's sunk boats even when debug is off
            bot_grid_data[y][x] = "H"
            bot_grid_special_boxes.append([x + 1, y + 1, "red_background"])

    # Show user's misses on the grid
    for miss in user_misses:
        x = miss[0]
        y = miss[1]
        bot_grid_data[y][x] = "M"
    
    # Inject border rows & render grids
    transformed_user_grid_data = inject_border_row(user_grid_data, GRID_SIZE_X, GRID_SIZE_Y, user_grid_special_boxes)
    transformed_bot_grid_data = inject_border_row(bot_grid_data, GRID_SIZE_X, GRID_SIZE_Y, bot_grid_special_boxes)

    user_grid = generate_grid(GRID_SIZE_X + 1, GRID_SIZE_Y + 1, transformed_user_grid_data, title="User's Grid", special_boxes=user_grid_special_boxes)
    bot_grid = generate_grid(GRID_SIZE_X + 1, GRID_SIZE_Y + 1, transformed_bot_grid_data, title="Bot's Grid", special_boxes=bot_grid_special_boxes)

    # Reset the special boxes after rendering the grid
    user_grid_special_boxes = []
    bot_grid_special_boxes = []

    # Merge grids and print to console
    grids = merge_with_offset(user_grid, bot_grid, 2)
    if grid_mode == "bot":
        grids = merge_with_offset(bot_grid, user_grid, 2)
    print(grid_instructions + "\n\n" + grids + "\n")

    # Check win
    won = False
    if len(bot_boats) > 0 and all_boats_dead(bot_boats):
        print("🎉 Congratulations, you won!")
        won = True
    
    if len(user_boats) > 0 and all_boats_dead(user_boats):
        print("🎉 Bot won, better luck next time!")
        won = True

    if won:
        input("Press enter to return to menu: ")
        return ["change_screen", "menu"]
    
    # Actions
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
                boat[2] = "dead"
                print("Hit!")
            else:
                print("Miss!")
                user_misses.append([x, y])
            
            bot_grid_special_boxes.append([x + 1, y + 1, "invert_background"])

            # Bot's turn to hit
            x, y = generate_random_grid_space(GRID_SIZE_X, GRID_SIZE_Y)
            boat = check_hit(user_boats, x, y)
            if boat:
                boat[2] = "dead"
            else:
                bot_misses.append([x, y])

            user_grid_special_boxes.append([x + 1, y + 1, "invert_background"])

            show_updated_grid = True

    # Save game data
    save_game_data(user_boats, user_misses, bot_boats, bot_misses)

    if show_updated_grid:
        return show_game(
            override_show_grid_mode=grid_mode,
            user_grid_special_boxes=user_grid_special_boxes,
            bot_grid_special_boxes=bot_grid_special_boxes
        )

    # Ask for continue
    if (skip_continue_prompt != True):
        continue_key = input("\nPress enter to continue, or X to go back to Main Menu ")
        if continue_key.lower() == "x":
            return ["change_screen", "menu"]
    
    return ["game", "continue"]