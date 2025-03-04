from screens.menu import show_menu
from screens.instructions import show_instructions
from utils.output import debugPrint

current_screen = "menu"

while True:
    full_operation = None
    if (current_screen == "menu"):
        full_operation = show_menu()
    elif (current_screen == "instructions"):
        full_operation = show_instructions()

    if (full_operation):
        operation_type = full_operation[0]
        operation_data = full_operation[1]

        if operation_type == "change_screen":
            current_screen = operation_data
        elif operation_type == "game":
            if operation_data == "end":
                break
    else:
        debugPrint("Invalid instruction!")
        break