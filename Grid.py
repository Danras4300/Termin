import Questions as q
import Answers as a
import Images.Landmark as l
import Images.Celeb as c

#Used by the bot to determind question type (question or answer)
runs=0
#used by the bot to know the amount of points for the question asked
points=0

grid = [["Math", "Capital", "Celeb", "Astronomy", "Landmark"],
        [100, 100, 100, 100, 100],
        [200, 200, 200, 200, 200],
        [300, 300, 300, 300, 300],
        [400, 400, 400, 400, 400],
        [500, 500, 500, 500, 500],]

#used to edit the grid from a number to xxx
def edit_grid(grid, points, cat):
    if cat == "!Math":
        if points == 100:
            grid[1][0] = "xxx"
        elif points == 200:
            grid[2][0] = "xxx"
        elif points == 300:
            grid[3][0] = "xxx"
        elif points == 400:
            grid[4][0] = "xxx"
        elif points == 500:
            grid[5][0] = "xxx"
    elif cat == "!Capital":
        if points == 100:
            grid[1][1] = "xxx"
        elif points == 200:
            grid[2][1] = "xxx"
        elif points == 300:
            grid[3][1] = "xxx"
        elif points == 400:
            grid[4][1] = "xxx"
        elif points == 500:
            grid[5][1] = "xxx"
    if cat == "!Celeb":
        if points == 100:
            grid[1][2] = "xxx"
        elif points == 200:
            grid[2][2] = "xxx"
        elif points == 300:
            grid[3][2] = "xxx"
        elif points == 400:
            grid[4][2] = "xxx"
        elif points == 500:
            grid[5][2] = "xxx"
    if cat == "!Astronomy":
        if points == 100:
            grid[1][3] = "xxx"
        elif points == 200:
            grid[2][3] = "xxx"
        elif points == 300:
            grid[3][3] = "xxx"
        elif points == 400:
            grid[4][3] = "xxx"
        elif points == 500:
            grid[5][3] = "xxx"
    if cat == "!Landmark":
        if points == 100:
            grid[1][4] = "xxx"
        elif points == 200:
            grid[2][4] = "xxx"
        elif points == 300:
            grid[3][4] = "xxx"
        elif points == 400:
            grid[4][4] = "xxx"
        elif points == 500:
            grid[5][4] = "xxx"
    
#used by the bot to proint the grid in lines when sent in discord or printed in the prompt
def get_grid_lines(grid):
    grid_lines = []
    for row in grid:
        row_str = ''
        for value in row:
            if value == "Math":
                row_str += 'Math   '
            elif value == "Capital":
                row_str += 'Capital   '
            elif value == "Celeb":
                row_str += '  Celeb  '
            elif value == "Astronomy":
                row_str += 'Astronomy '
            elif value == "Landmark":
                row_str += 'Landmark'
            elif value == 100:
                row_str += '100           '
            elif value == 200:
                row_str += '200          '
            elif value == 300:
                row_str += '300          '
            elif value == 400:
                row_str += '400          '
            elif value == 500:
                row_str += '500          '
            else:
                row_str += 'XXX          '
        grid_lines.append(row_str)
    return grid_lines