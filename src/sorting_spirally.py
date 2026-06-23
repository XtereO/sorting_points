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
    if (number_points == 1):
        return [0]

    indexed_points = list(enumerate(points))
    pivot_point_index = pop_by_value(indexed_points, min(
        indexed_points, key=lambda ip: (ip[1][0], ip[1][1], ip[1][2])))

    res = [pivot_point_index]
    pivot_point = points[pivot_point_index]
    init_prev_point = [pivot_point[0], pivot_point[1]-1, pivot_point[2]]
    pick_loop(points, indexed_points, res, init_prev_point)

    while indexed_points:
        prev_i_index = -2
        prev_point = points[res[prev_i_index]]
        pivot_point = points[res[-1]]
        while prev_point[0]==pivot_point[0] and prev_point[1]==pivot_point[1]:
            prev_i_index -= 1
            if(-prev_i_index >= len(res)):
                prev_point = init_prev_point
                break
            prev_point = points[res[prev_i_index]]

        pick_loop(points, indexed_points, res, prev_point)
        print(
            f'\rSorted points: {len(res)}/{number_points} (left {len(indexed_points)})', end='')

    print(f'\rPoints have been sorted: {len(res)}')

    if (showing_result):
        x_ordered = list(map(lambda i: points[i][0], res))
        y_ordered = list(map(lambda i: points[i][1], res))

        sns.scatterplot(x=x_ordered, y=y_ordered)
        plt.show()

        plt.plot(x_ordered, y_ordered, marker='o')
        plt.show()

    return res


# this code needs for modifying the behavior of sort_points_spirally function (eg changing pick_next_point method)
def pick_loop(points, indexed_points, res, prev_point):
    pivot_point = points[res[-1]]
    next_pivot_point_index = pick_next_point["Jarvis"](
        indexed_points, pivot_point, prev_point)
    pop_by_value(indexed_points, (next_pivot_point_index,
                 points[next_pivot_point_index]))
    res.append(next_pivot_point_index)
