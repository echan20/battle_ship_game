from utils.database import db
from utils.output import input_options
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

    x = input_options("Select a column: ", allowed_x_spaces)
    y = input_options("Select a row: ", allowed_y_spaces)
    return allowed_x_spaces_map.get(x), allowed_y_spaces_map.get(y)

def load_game_data():
    game_db = db("game_data")

    user_boats = game_db.get("user_boats")
    if (not user_boats):
        user_boats = []

    return {
        "user_boats": user_boats
    }