from config import DEBUG_MODE

_print = print

# Print to Console
def clearConsole():
    print("\n" * 20)

def print(*args):
    return _print(*args)

def debugPrint(*args):
    if (not DEBUG_MODE):
        return
    return _print("[DEBUG]:", *args)

# Input from Console
def inputCustom(prompt: str, validator):
    input_text = input(prompt)
    passed = validator(input_text)
    if (passed):
        return input_text
    else:
        print("Invalid option!")
        return inputCustom(prompt, validator)

def inputOptions(prompt: str, options: list):
    def validate(input_text: str):
        if (input_text in options):
            return True
        return False
    
    return inputCustom(prompt, validate)