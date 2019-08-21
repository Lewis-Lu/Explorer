import matplotlib.patches as mpatches
import matplotlib.collections

class Plot(object):
    def __init__(self, X):
        ''' create a plot
        :param X: search space
        '''
        self.dim = X.dim
        self.range = X.dim_range
        self.obs = X.obs
    

    def plot_2D(self, ax, obstacles, start, end):
        '''plot 2D map
        :param ax: axes created passed in
        :param obstacles: list of obs
        :param start: start point
        :param end: end point
        '''
        ax = self.plot_2D_obstacles(ax, obstacles)
        ax = self.plot_2D_start_end(ax, start, end)
        # TODO add plot vehicle
        return ax


    def plot_2D_obstacles(self, ax, obstacles):
        ''' plot 2D map
        :param ax: axes created
        :param obstacles: list of obstacle
        '''
        
        rectangles = []
        for o in obstacles:
            coords = o[1]

            rect = mpatches.Rectangle(
                [coords[0], coords[1]], 
                abs(coords[0] - coords[2]), 
                abs(coords[1] - coords[3])
            )

            rectangles.append(rect)

        collection = matplotlib.collections.PatchCollection(rectangles, facecolor='r', alpha=0.4)
        ax.add_collection(collection)

        return ax
    

    def plot_2D_start_end(self, ax, start, end):
        '''plot start and end points
        '''
        len = 2

        sp = mpatches.Rectangle(
            [start[0], start[1]],
            len, len, fc='b'
        )

        ep = mpatches.Rectangle(
            [end[0], end[1]],
            len, len, fc='b'
        )
        ax.add_patch(sp)
        ax.add_patch(ep)

        return ax


    def plot_2D_vehicle(self, ax, vehicle):
        '''plot vehicle
        '''
        
        lidar = mpatches.Wedge(
            (vehicle.location[0], vehicle.location[1]),
            vehicle.lidar_length,
            vehicle.lidar_theta[0],
            vehicle.lidar_theta[1],
            width=None,
            fc='g',
            alpha=0.3
        )

        loc = mpatches.Rectangle(
            (vehicle.location[0], vehicle.location[1]),
            1, 1, fc='k'
        )

        ax.add_patch(lidar)
        ax.add_patch(loc)

        return ax
