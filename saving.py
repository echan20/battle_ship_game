# Imports
import json
import os

# Config
NUMBER_OF_SAVES = 5
SAVES_FOLDER_NAME = "saves"

# Functions
def get_saves_folder_path():
    return f"./{SAVES_FOLDER_NAME}"

def get_save_file_name(key: int):
    return f"save{key}.json"

def get_saves_status():
    save_statuses = []

    for i in range(NUMBER_OF_SAVES):
        save_file_name = f"save{i}.json"

        if os.path.exists(save_file_name):
            save_statuses.append("Exist")
        else:
            save_statuses.append("Empty")

# Load save as JSON
def load_save(key: int):    
    save_file_name = f"{get_saves_folder_path()}/{get_save_file_name(key)}"

    try:
        with open(save_file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None

# Save data to a slot
def overwrite_save(key: int, data):    
    save_file_name = f"{get_saves_folder_path()}/{get_save_file_name(key)}"

    try:
        with open(save_file_name, "w") as file:
            json.dump(data, file)
        return True
    except Exception as e:
        return False