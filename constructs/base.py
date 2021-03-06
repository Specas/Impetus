import numpy as np
import math

from Impetus.kinematics.rotmat import RotMat
from Impetus.numeric.constants import Physical, Units, Struct, Matrices, RenderObjects
from Impetus.numeric.operations import Operations
# Class that deals with creating base construct classes for kinematics, dynamcics and planning


class Frame(object):

    def __init__(
            self, base=None,
            x=Matrices.std_axis_x,
            y=Matrices.std_axis_y,
            z=Matrices.std_axis_z,
            origin=Matrices.std_origin,
            is_std=True):

        self.base = base
        self.x = Operations.normalize_vector(x)
        self.y = Operations.normalize_vector(y)
        self.z = Operations.normalize_vector(z)
        self.origin = origin
        self.is_std = is_std

        self.render_object = RenderObjects.frame

    def compute_world_origin(self):

        world_origin = Matrices.vector_zero
        tmp_frame = self

        while tmp_frame.base is not None:

            world_origin += tmp_frame.origin
            tmp_frame = tmp_frame.base

        return world_origin


class Vector(object):

    def __init__(self, x=0, y=0, z=0, base_frame=Frame()):

        self.x = x
        self.y = y
        self.z = z
        self.v = np.array([[self.x], [self.y], [self.z]])
        self.base_frame = base_frame

        self.render_object = RenderObjects.vector

    def compute_norm(self):

        return Operations.normalize_vector(self.v)

    def get_vector_hom(self):

        return np.concatenate((self.v, np.array([[1]])), axis=0)

    def compute_world_v(self):

        rm = RotMat.gen_rm_all_frame(self.base_frame)
        return np.dot(rm, self.v)

class Axis(Vector):

    def __init__(self, x=0, y=0, z=0, base_frame=Frame()):

        super(Axis, self).__init__(x, y, z, base_frame)
        self.v = Operations.normalize_vector(np.array([[self.x], [self.y], [self.z]]))

    @classmethod
    def gen_global_x(self):

        return Axis(1, 0, 0)

    @classmethod
    def gen_global_y(self):

        return Axis(0, 1, 0)

    @classmethod
    def gen_global_z(self):

        return Axis(0, 0, 1)


    def compute_world_v(self):

        rm = RotMat.gen_rm_all_frame(self.base_frame)
        return np.dot(rm, self.v)


class Configuration(object):

    def __init__(self, dim):

        self.dim = dim
        self.lower_limits = [Units.ninfinity]*self.dim
        self.upper_limits = [Units.infinity]*self.dim
        self.value = np.zeros([self.dim, 1])

    def set_value(self, value):

        for i, el in enumerate(value):
            self.value[i] = el


    def get_lower_limits_arr(self):

        return np.array(self.lower_limits).reshape(self.dim, 1)

    def get_upper_limits_arr(self):

        return np.array(self.upper_limits).reshape(self.dim, 1)

    def clip(self):

        self.value = Operations.clip_bound(
            self.value, self.lower_limits, self.upper_limits)
