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

grid = [["Math", "Capital", "Celeb", "Astronomy", "Landmark"],
        [100, 100, 100, 100, 100],
        [200, 200, 200, 200, 200],
        [300, 300, 300, 300, 300],
        [400, 400, 400, 400, 400],
        [500, 500, 500, 500, 500],]

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
                row_str += 'XXX'
        grid_lines.append(row_str)
    print(grid_lines)
    return grid_lines

print("\n".join(get_grid_lines(grid)))