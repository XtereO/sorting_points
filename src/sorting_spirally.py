from typing import List
import matplotlib.pyplot as plt
import seaborn as sns

from picking_methods_spirally import pick_next_point
from spirally_implementations import sort_points_spirally_Jarvis
from utils import pop_by_value


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

    res = sort_points_spirally_Jarvis(points, number_points, indexed_points, res, pivot_point)

    print(f'\rPoints have been sorted: {len(res)}')

    if (showing_result):
        x_ordered = list(map(lambda i: points[i][0], res))
        y_ordered = list(map(lambda i: points[i][1], res))

        sns.scatterplot(x=x_ordered, y=y_ordered)
        plt.show()

        plt.plot(x_ordered, y_ordered, marker='o')
        plt.show()

    return res
