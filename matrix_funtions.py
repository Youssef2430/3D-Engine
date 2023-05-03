import math
import numpy as np


def translate(pos):
    """
    :param pos: position vector
    :return: translation matrix
    """
    tx, ty, tz = pos
    return np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [tx, ty, tz, 1]])

def rotate_x(angle):
    """
    :param a: angle in radians
    :return: rotation matrix
    """
    return np.array([[1, 0, 0, 0],
                        [0, math.cos(angle), math.sin(angle), 0],
                        [0, -math.sin(angle), math.cos(angle), 0],
                        [0, 0, 0, 1]])

def rotate_y(angle):
    """
    :param a: angle in radians
    :return: rotation matrix
    """
    return np.array([[math.cos(angle), 0, -math.sin(angle), 0],
                        [0, 1, 0, 0],
                        [math.sin(angle), 0, math.cos(angle), 0],
                        [0, 0, 0, 1]])

def rotate_z(angle):
    """
    :param a: angle in radians
    :return: rotation matrix
    """
    return np.array([[math.cos(angle), math.sin(angle), 0, 0],
                        [-math.sin(angle), math.cos(angle), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])

def scale(s):
    """
    :param s: scale factor
    :return: scale matrix
    """
    return np.array([[s, 0, 0, 0],
                        [0, s, 0, 0],
                        [0, 0, s, 0],
                        [0, 0, 0, 1]])