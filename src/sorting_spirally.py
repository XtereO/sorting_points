from typing import List
import matplotlib.pyplot as plt
import seaborn as sns

from picking_methods import pick_next_point
from utils import get_boundaries_indexed_points, pop_by_value


def sort_points_spirally(points: List[List[float]], showing_result=False) -> List[int]:
    """Function sorts a list of points in spiral order.

    Args:
        points (list of lists): A list of (x, y, z) coordinates (must be at least 2 dimensions).

    Returns:
        list of indexes: Indexes of sorted points in spiral order.
    """

    number_points = len(points)
    if (number_points == 0):
        return []

    indexed_points = list(enumerate(points))
    pivot_point = pop_by_value(indexed_points, min(
        indexed_points, key=lambda ip: (ip[1][0], ip[1][1], ip[1][2])))

    res = [pivot_point]

    while indexed_points:
        pivot_point = points[res[-1]]
        pivot_x, pivot_y, _pivot_z = pivot_point

        x_min, x_max, y_min, y_max = get_boundaries_indexed_points(
            [*indexed_points, (res[-1], pivot_point)])
        y_mean = y_min + ((y_max-y_min)/2)
        x_mean = x_min + ((x_max-x_min)/2)
        shifted_pivot_x = pivot_x - x_mean
        shifted_pivot_y = pivot_y - y_mean

        next_pivot_point_index = pick_next_point["rotated_atan2"](
            points, indexed_points, (shifted_pivot_x, shifted_pivot_y, pivot_x, pivot_y))
        pop_by_value(indexed_points, (next_pivot_point_index,
                     points[next_pivot_point_index]))
        res.append(next_pivot_point_index)
        print(
            f'\rSorted points: {len(res)}/{number_points} (left {len(indexed_points)})', end='')
    print(f'\rPoints have been sorted: {len(res)}') # these spaces are required to refresh left part of the last print 

    if (showing_result):
        x_ordered = list(map(lambda i: points[i][0], res))
        y_ordered = list(map(lambda i: points[i][1], res))

        sns.scatterplot(x=x_ordered, y=y_ordered)
        plt.show()

        plt.plot(x_ordered, y_ordered, marker='o')
        plt.show()

    return res
