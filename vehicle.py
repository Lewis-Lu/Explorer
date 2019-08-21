import math

class lidar_car(object):
    def __init__(self, location, orientation):
        ''' initialize a car
        # TODO think about whether to add X
        :param X: search space
        :param location: coords of location
        :param orientation: orientation angle
        '''
        self.location = location
        self.orientation = orientation

        # lidar param
        self.lidar_length = 10.0 # cover length
        self.lidar_range = 120.0 # cover angle
        self.lidar_theta = [self.orientation, self.orientation + self.lidar_range]

    # FIXME how to model lidar whether know obstacles,
    # use index.count() !
    def lidar_check(self, X, lr, pr):
        '''lidar check the environment
        :param X: search space
        :param lr: line interval (degree)
        :param pr: point interval (m)
        :return data: list of range data
        '''
        # for each line using r to select point
        # and judge whether this point is within rectangle
        l = int(self.lidar_range / lr)
        p = int(self.lidar_length / pr) 
        data = []
        for i in range(l):
            theta = ((self.orientation + i*lr)/180.0)*math.pi # radius
            for j in range(1, p):
                length = j*pr
                coordx = math.cos(theta)*length + self.location[0]
                coordy = math.sin(theta)*length + self.location[1]
                data.append([coordx, coordy])
        return data
                