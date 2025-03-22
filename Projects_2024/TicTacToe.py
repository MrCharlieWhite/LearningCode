grid = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

def get_x_coordinate(num): 
    return (num-1) % 3

def get_y_coordinate(num): 
    return int(int(num - 1) / 3)

def updateValue(cellNum, userInput): 
    x = get_x_coordinate(cellNum)
    y = get_y_coordinate(cellNum)
    grid[y][x] = userInput


updateValue(5, 'X')

print(grid[6][3])