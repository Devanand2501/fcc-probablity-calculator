import copy
import random

class Hat:
    def __init__(self, **variable_arg):
        self.contents = []
        for key, value in variable_arg.items():
            for i in range(value):
                self.contents.append(key)
    def draw(self, no):
        ball_list = []
        if no > len(self.contents):
            return self.contents
        for _ in range(no):
            ch = random.randrange(len(self.contents))
            ball_list.append(self.contents.pop(ch))
        return ball_list
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    n=num_experiments
    exp_no_of_balls = []
    for key in expected_balls:
        exp_no_of_balls.append(expected_balls[key])

    for i in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls = new_hat.draw(num_balls_drawn)
        balls_req = []
        for key in expected_balls:
            balls_req.append(balls.count(key))
        if balls_req >= exp_no_of_balls:
            m += 1
    return m/n