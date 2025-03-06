from config import DEBUG_MODE

_print = print

# Print to Console
def clear_console():
    print("\n" * 20)

def print(*args):
    return _print(*args)

def debugPrint(*args):
    if (not DEBUG_MODE):
        return
    return _print("[DEBUG]:", *args)

# Input from Console
def input_custom(prompt: str, validator):
    input_text = input(prompt)
    passed = validator(input_text)
    if (passed):
        return input_text
    else:
        print("Invalid option!")
        return input_custom(prompt, validator)

def input_options(prompt: str, options: list):
    def validate(input_text: str):
        if (input_text in options):
            return True
        return False
    
    return input_custom(prompt, validate)