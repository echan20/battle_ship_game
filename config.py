# Main
DEBUG_MODE = False
DEBUG_SHOW_BOT_BOATS = False

# Grid
GRID_SIZE_X = 8
GRID_SIZE_Y = 8

# Game
AMOUNT_OF_BOATS = 5

# Screens
MENU_OPTIONS = [
    ["New Game"],
    ["Resume Game"],
    ["Instructions"],
    ["Quit"]
]

INSTRUCTIONS = [
    "--- INSTRUCTIONS ---",
    f"Each player has a {GRID_SIZE_X}x{GRID_SIZE_Y} grid",
    f"First, you have to place {AMOUNT_OF_BOATS} boats on the grid.",
    "Then, the game starts.",
    "Every round, you can enter a coordinates on the grid to fire a bomb.",
    "If the bomb hit, the box would show 'H', if not, the box would show 'M' for miss.",
    f"You win when you hit all {AMOUNT_OF_BOATS} of the opponent's boats!"
]