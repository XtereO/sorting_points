from picking_methods_spirally import pick_next_point
from utils import pop_by_value


def sort_points_spirally_Jarvis(points, number_points, indexed_points, res, pivot_point):
    init_prev_point = [pivot_point[0], pivot_point[1]-1, pivot_point[2]]
    pick_loop_Jarvis(points, indexed_points, res, init_prev_point)

    while indexed_points:
        prev_i_index = -2
        prev_point = points[res[prev_i_index]]
        pivot_point = points[res[-1]]
        while prev_point[0] == pivot_point[0] and prev_point[1] == pivot_point[1]:
            prev_i_index -= 1
            if (-prev_i_index >= len(res)):
                prev_point = init_prev_point
                break
            prev_point = points[res[prev_i_index]]

        pick_loop_Jarvis(points, indexed_points, res, prev_point)
        print(
            f'\rSorted points: {len(res)}/{number_points} (left {len(indexed_points)})', end='')

    return res

def pick_loop_Jarvis(points, indexed_points, res, prev_point):
    pivot_point = points[res[-1]]
    next_pivot_point_index = pick_next_point["Jarvis"](
        indexed_points, pivot_point, prev_point)
    pop_by_value(indexed_points, (next_pivot_point_index,
                 points[next_pivot_point_index]))
    res.append(next_pivot_point_index)
