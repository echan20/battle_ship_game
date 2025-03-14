from config import MENU_OPTIONS
from utils.output import print, input_options, clear_console
from utils.saving import wipe_game_data

def show_menu():
    clear_console()

    menu_lines = []
    menu_lines.append("--- Battleships Game ---")

    valid_inputs = []

    for option_id, option_data in enumerate(MENU_OPTIONS):
        option_key = (option_id + 1)
        option_text = option_data[0]
        menu_lines.append(f'{option_key}: {option_text}')
        valid_inputs.append(str(option_key))

    menu_text = ("\n").join(menu_lines)
    print(menu_text)

    option_chosen = input_options("\nEnter an option: ", valid_inputs)

    play_game = False
    if (option_chosen == "1"):
        wipe_game_data()
        play_game = True
    elif (option_chosen == "2"):
        play_game = True
    elif (option_chosen == "3"):
        return ["change_screen", "instructions"]
    elif (option_chosen == "4"):
        return ["game", "end"]
    
    if play_game:
        return ["change_screen", "game"]
    return ["game", "continue"]