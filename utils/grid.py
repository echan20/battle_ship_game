from utils.utility import annotate_text

# Grid Configuration
TOP_BORDER = "─"
TOP_MIDDLE_BORDER = "┬"
TOP_LEFT_BORDER = "┌"
TOP_RIGHT_BORDER = "┐"

MIDDLE_STRAIGHT_BORDER = "│"
MIDDLE_BORDER = "─"
MIDDLE_CROSS_BORDER = "┼"
MIDDLE_LEFT_BORDER = "├"
MIDDLE_RIGHT_BORDER = "┤"

BOTTOM_BORDER = "─"
BOTTOM_MIDDLE_BORDER = "┴"
BOTTOM_LEFT_BORDER = "└"
BOTTOM_RIGHT_BORDER = "┘"

BOX_SIZE = 3

# Functions
def add_line_to_grid(grid: str, line: str):
    # If grid is empty, set it to the line. Otherwise, append the line below it.
    if grid == "":
        grid = line
    else:
        grid += "\n"
        grid += line
    return grid

def generate_grid(x_size: int, y_size: int, values, has_borders: bool = True, title: str = None, special_boxes: list = None):
    grid = ""
    
    # Calculate total width
    total_width = (x_size * BOX_SIZE) + (x_size - 1) + (2 if has_borders else 0)
    
    if special_boxes is None:
        special_boxes = []
    
    # Add title if provided
    if title:
        centered_title = title.center(total_width)
        grid = add_line_to_grid(grid, centered_title)

    # Generate Top Border
    if (has_borders):
        border_line = TOP_LEFT_BORDER
        for i in range(x_size):
            border_line += TOP_BORDER * BOX_SIZE
            if i < x_size - 1:
                border_line += TOP_MIDDLE_BORDER
        border_line += TOP_RIGHT_BORDER
        grid = add_line_to_grid(grid, border_line)
    
    # Generate Boxes
    for y in range(y_size):
        # Create Line
        line = ""
        # Create Border Line
        line2 = ""

        # Add left borders
        if (has_borders):
            line += MIDDLE_STRAIGHT_BORDER
            line2 += MIDDLE_LEFT_BORDER

        # Create each boxes
        for x in range(x_size):
            # If this isn't the first box, add a separator to it before continuing.
            if x != 0:
                line += MIDDLE_STRAIGHT_BORDER
                line2 += MIDDLE_CROSS_BORDER

            # Add a border to the bottom
            line2 += (MIDDLE_BORDER * BOX_SIZE)

            # Get value and add it.
            value = ""
            try:
                value = values[y][x]
            except:
                value = " " * BOX_SIZE

            # Center the value and add padding
            value = value.center(BOX_SIZE, " ")

            # Check if this box should be highlighted
            for box in special_boxes:
                target_x = box[0]
                target_y = box[1]
                modes = box[2]

                if (target_x == x and target_y == y):
                    value = annotate_text(value, modes)
                    break

            # Add the value to line
            line += value

        # Add right borders
        if (has_borders):
            line += MIDDLE_STRAIGHT_BORDER
            line2 += MIDDLE_RIGHT_BORDER

        # Add the line to grid
        grid = add_line_to_grid(grid, line)

        # If it is not the last line, add the border line
        if (y + 1) < y_size:
            grid = add_line_to_grid(grid, line2)

    # Generate Bottom Border
    if (has_borders):
        border_line = BOTTOM_LEFT_BORDER
        for i in range(x_size):
            border_line += BOTTOM_BORDER * BOX_SIZE
            if i < x_size - 1:
                border_line += BOTTOM_MIDDLE_BORDER
        border_line += BOTTOM_RIGHT_BORDER
        grid = add_line_to_grid(grid, border_line)

    return grid