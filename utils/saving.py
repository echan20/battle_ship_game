from utils.database import db

game_db = db("game_data")

def load_game_data():
    game_db = db("game_data")

    user_boats = game_db.get("user_boats")
    if (not user_boats):
        user_boats = []

    return {
        "user_boats": user_boats
    }

def save_game_data(user_boats):
    game_db.set("user_boats", user_boats)

def wipe_game_data():
    game_db.delete("user_boats")