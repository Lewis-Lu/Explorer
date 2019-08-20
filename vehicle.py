
class lidar_car(object):
    def __init__(self, location, orientation):
        ''' initialize a car
        # TODO think about whether to add X
        :param X: search space
        :param location: coords of location
        :param orientation: orientation angle
        '''
        self.location = location
        self.angle = orientation

        # lidar param
        self.lidar_length = 10.0 # cover length
        self.lidar_range = 120.0 # cover angle
        self.lidar_theta = [self.angle, self.angle + self.lidar_range]

    # TODO how to model lidar whether know obstacles,
    # use index.count() !
    def lidar_check(self, X):
        '''lidar check the environment
        :param X: search space
        '''
        