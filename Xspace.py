from rtree import index

class Xspace(object):
    def __init__(self, dim_range, Obs=None):
        ''' Initialize Search Space
        dim_range:  upper bound of each dimension, lower bound is defaultly set as 0
        Obs: default value=None
        '''
        self.dim_range = dim_range
        self.dim = len(dim_range)
        
        # sanity process
        if self.dim < 2:
            raise Exception('at least initialize 2D map.')
        if self.dim > 3:
            raise Exception('at most initialize 3D map.')
        
        self.obs = Obs
        if Obs is not None:
            # empty initialize self.obs
            # index member: interleaved=True xmin, ymin, ..., kmin, xmax, ymax, ..., kmax
            self.obs = index.Index(interleaved=True)
            for i in Obs:
                self.obs.insert(i[0],i[1])
          