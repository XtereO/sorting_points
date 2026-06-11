from typing import List
import matplotlib.pyplot as plt
import seaborn as sns

def sort_points_parallelly_x(points: List[List[float]], showing_result=False) -> List[List[int]]:
    res = []
    indexed_points = list(enumerate(points))
    sorted_points_y = sorted(indexed_points, key=lambda ip: (ip[1][1], ip[1][0], ip[1][2]))

    if (showing_result):
        x_groups = []
        y_groups = []
        for group in res:
            x_ordered = list(map(lambda i: points[i][0], group))
            y_ordered = list(map(lambda i: points[i][1], group))
            x_groups.append(x_ordered)
            y_groups.append(y_groups)

            sns.scatterplot(x=x_ordered, y=y_ordered)
        plt.show()

        for i, x_g in enumerate(x_groups):
            plt.plot(x_g, y_groups[i], marker='o')
        plt.show()
    
    return res