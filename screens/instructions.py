from utils.output import print, clearConsole
from config import INSTRUCTIONS

def show_instructions():
    clearConsole()

    instructions_text = ("\n").join(INSTRUCTIONS)
    print(instructions_text)
    input("\nPress enter to continue ")

    return ["change_screen", "menu"]