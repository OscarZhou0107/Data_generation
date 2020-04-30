from random import choice
class RandomWalk():
    """random number class"""
    def __init__(self,num_points = 5000):
        """intial """
        self.num_points = num_points
        self.x_vaules = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calucalte all points"""
        while len(self.x_vaules)<self.num_points:
            x_direction =choice ([-1,1])
            x_distance = choice ([1,2,3,4,5])
            x_step = x_direction * x_distance

            y_direction =choice ([-1,1])
            y_distance = choice ([1,2,3,4,5])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_vaules[-1]+x_step
            next_y = self.y_values[-1]+y_step
            self.x_vaules.append(next_x)
            self.y_values.append(next_y)

