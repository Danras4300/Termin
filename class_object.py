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