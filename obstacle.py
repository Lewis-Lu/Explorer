import random

# import as matriRange calculation
import numpy as np


def random_obstacle_generate(Range, start, end, n):
    ''' generate random obstacles
    :param Range: search space dimension range
    :param start: start point
    :param end: end point
    :param n: obstacles quantity
    '''
    obstacles = []
    i = 0
    lb = 0

    dim = len(Range)

    while i < n:
        obstacle = []
        # generate left-down point and edge lengths randomly
        # using list comprehensive
        rand_coord = np.array([random.uniform(lb, Range[j]) for j in range(dim)])
        edge_length = np.array([random.uniform(Range[j]/50.0, Range[j]/10.0) for j in range(dim)])
        # calculate right-up coords
        # also called diagonal point
        diagnal_coord = rand_coord + edge_length
        obs_centroid = rand_coord + edge_length/2.0
        # criterion length for an obstacle
        # using 2-norm
        criterion = np.linalg.norm(obs_centroid - rand_coord, 2)
        slength = np.linalg.norm(np.array(start) - obs_centroid, 2)
        elength = np.linalg.norm(np.array(end) - obs_centroid, 2)
        
        # start and end point cannot fall into obstacles
        # sanity check
        if slength < criterion or elength < criterion:
            # skip this iteration
            continue
        coords = tuple(np.append(rand_coord, diagnal_coord))
        
        obstacle.append(i)
        obstacle.append(coords)
        
        obstacles.append(obstacle)
        
        i += 1

    return obstacles
