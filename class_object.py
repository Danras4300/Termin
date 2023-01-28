import Questions as q
import Answers as a
import Images.Landmark as l
import Images.Celeb as c

class Catagory:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers


Math = Catagory(q.Math_q, a.Math_a)
capital = Catagory(q.Capital_q, a.Capital_a)
celeb = Catagory(q.Celeb_q, a.Celeb_a)
Astronomy_q = Catagory(q.Astronomy_q, a.Astronomy_a)
landmark = Catagory(q.Landmark_q, a.Landmark_a)

runs=0
points=0

grid = [["Math", "Capital", "Celeb", "Astronomy", "Landmark"],
        [100, 100, 100, 100, 100],
        [200, 200, 200, 200, 200],
        [300, 300, 300, 300, 300],
        [400, 400, 400, 400, 400],
        [500, 500, 500, 500, 500],]

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
    print(grid_lines)
    return grid_lines

print("\n".join(get_grid_lines(grid)))