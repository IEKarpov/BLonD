'''
Created on 08.01.2014

@author: Kevin Li
'''


import numpy as np


class PoissonFFT(object):
    '''
    classdocs
    '''

    def __init__(self, n_points):
        '''
        Constructor
        '''
        self.n_points = n_points

        self.fgreen = np.zeros(100)