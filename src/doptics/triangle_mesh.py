import numpy as np
from attrs import define
from typing import Tuple
import scipy.integrate as sci
import scipy as sp
from typing import Callable, List, Union
from numpy.typing import ArrayLike, NDArray
import matplotlib.pyplot as plt
from icecream import ic


@define
class Triangle:
    """

    """
    points: {'a': Tuple[float], 'b': Tuple[float], 'c': Tuple[float]}


@define
class Mesh:
    points: List[Tuple[float]]  # NDArray(dtype=Tuple[float])
    cells: NDArray([3, 3])  # i want shape (:,3)  -> unspecified rows, three cols


def transform(triangle: Triangle, target: Triangle = {'a': (0, 0), 'b': (1, 0), 'c': (0, 1)}):
    """

    :param triangle:
    :param target:
    :return:
    """
    A_T = np.array([[(triangle.points['b'][0] - triangle.points['a'][0]), (triangle.points['c'][0] - triangle.points['a'][0])],
                    [(triangle.points['b'][1] - triangle.points['a'][1]), (triangle.points['c'][1] - triangle.points['a'][1])]]
                   )
    b_T = np.array([[triangle.points['a'][1]],
                    [triangle.points['a'][1]]
                    ])
    ic(A_T)
    ic(b_T)
    ic(np.linalg.det(A_T))


if __name__ == '__main__':
    trg = Triangle({'a': (5, 1), 'b': [-7, 3], 'c': (4, 4)})
    ic(trg)
    transform(trg)
