from typing import List
import matplotlib.pyplot as plt
import seaborn as sns


def sort_points_parallelly_x(points: List[List[float]], max_delta=1, showing_result=False):
    return _sort_points_parallelly(points, max_delta, showing_result, 0)


def sort_points_parallelly_y(points: List[List[float]], max_delta=1, showing_result=False):
    return _sort_points_parallelly(points, max_delta, showing_result, 1)


def _sort_points_parallelly(points: List[List[float]], max_delta=1, showing_result=False, axis=0):
    if (len(points) == 0):
        return []

    first_axis = axis
    second_axis = 1 if axis == 0 else 0

    indexed_points = list(enumerate(points))
    sorted_points_y = sorted(indexed_points, key=lambda ip: (
        ip[1][second_axis], ip[1][first_axis], ip[1][2]))

    res = [[]]
    fp = sorted_points_y[0]
    for p in sorted_points_y:
        if p[1][second_axis]-fp[1][second_axis] < max_delta:
            res[-1].append(p[0])
        else:
            res[-1] = _sort_group_points_axis(res[-1], points, first_axis, second_axis)
            fp = p
            res.append([fp[0]])
    res[-1] = _sort_group_points_axis(res[-1], points, first_axis, second_axis)

    if (showing_result):
        x_groups = []
        y_groups = []
        for group in res:
            x_ordered = list(map(lambda i: points[i][0], group))
            y_ordered = list(map(lambda i: points[i][1], group))
            x_groups.append(x_ordered)
            y_groups.append(y_ordered)

            sns.scatterplot(x=x_ordered, y=y_ordered)
        plt.show()

        for i, x_g in enumerate(x_groups):
            plt.plot(x_g, y_groups[i])
        plt.show()

    return res


def _sort_group_points_axis(indexed_group, points, first_axis=0, second_axis=1):
    return sorted(indexed_group, key=lambda i: (points[i][first_axis], points[i][second_axis], points[i][2]))
