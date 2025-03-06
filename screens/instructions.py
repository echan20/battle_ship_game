from utils.output import print, clear_console
from config import INSTRUCTIONS

def show_instructions():
    clear_console()

    instructions_text = ("\n").join(INSTRUCTIONS)
    print(instructions_text)
    input("\nPress enter to continue ")

    return ["change_screen", "menu"]