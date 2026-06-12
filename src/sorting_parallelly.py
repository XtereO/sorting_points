from typing import List
import matplotlib.pyplot as plt
import seaborn as sns

def sort_points_parallelly_x(points: List[List[float]], max_delta=1, showing_result=False) -> List[List[int]]:
    if (len(points) == 0):
        return []
    
    indexed_points = list(enumerate(points))
    sorted_points_y = sorted(indexed_points, key=lambda ip: (ip[1][1], ip[1][0], ip[1][2]))

    res = [[]]
    fp = sorted_points_y[0]
    for p in sorted_points_y:
        if p[1][1]-fp[1][1]<max_delta:
            res[-1].append(p[0])
        else:
            fp = p
            res.append([fp[0]])

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