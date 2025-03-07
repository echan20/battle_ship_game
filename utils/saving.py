from utils.database import db

game_db = db("game_data")

def load_game_data():
    game_db = db("game_data")

    user_boats = game_db.get("user_boats")
    if (not user_boats):
        user_boats = []

    user_misses = game_db.get("user_misses")
    if (not user_misses):
        user_misses = []

    bot_boats = game_db.get("bot_boats")
    if (not bot_boats):
        bot_boats = []

    bot_misses = game_db.get("bot_misses")
    if (not bot_misses):
        bot_misses = []

    return {
        "user_boats": user_boats,
        "user_misses": user_misses,
        "bot_boats": bot_boats,
        "bot_misses": bot_misses
    }

def save_game_data(user_boats, user_misses, bot_boats, bot_misses):
    game_db.set("user_boats", user_boats)
    game_db.set("user_misses", user_misses)

    game_db.set("bot_boats", bot_boats)
    game_db.set("bot_misses", bot_misses)

def wipe_game_data():
    game_db.delete("user_boats")
    game_db.delete("user_misses")

    game_db.delete("bot_boats")
    game_db.delete("bot_misses")