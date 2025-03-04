import config
from utils.grid import generate_grid

grid_data = [["M"]]
grid = generate_grid(config.GRID_SIZE_X, config.GRID_SIZE_Y, grid_data)
print(grid)