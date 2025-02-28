def add_line_to_grid(grid: str, line: str):
    if grid == "":
        grid = line
    else:
        grid += "\n"
        grid += line
    return grid

def generate_grid(x_size: int, y_size: int, values):
    grid = ""
    
    for y in range(y_size):
        line = ""
        line2 = ""
        for x in range(x_size):
            value = ""
            if line != "":
                line += "│"
                line2 += "│"

            line2 += "───"

            try:
                value = values[y][x]
            except:
                value = "   "

            if len(value) == 1:
                value = " " + value + " "
            elif len(value) == 2:
                value = value + " "
            
            line += value

        grid = add_line_to_grid(grid, line)
        if (y + 1) < y_size:
            grid = add_line_to_grid(grid, line2)

    return grid