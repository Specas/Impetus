import numpy as np
import random

from .. numeric.constants import Constants
from .. numeric.operations import Operations
from .. constructs.base import Configuration
from .. planning.base import RRT

# Standard RRT implementations


class rrt_standard(RRT):

    def __init__(self, config=Configuration()):

        super(rrt_standard, self).__init__(config)

    def initialize_random_configuration(self):

        rand_base = np.random.rand(self.config.dim, 1)
        a = self.config.get_lower_limits_arr()
        b = self.config.get_upper_limits_arr()
        return a + rand_base*(b-a)

    def compute_distance(self, x, y):

        pass

    def is_config_in_free(self, x):

        pass

    def is_line_in_free(self, x, y):

        pass
