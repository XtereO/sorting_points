from math import acos, sin, cos, atan2, log
from typing import List, Tuple

from utils import shift_point

def pick_next_point_rotated_atan2(points: List[List[float]], indexed_points: List[Tuple], indexed_pivot_point: Tuple[float]) -> int:
    pivot_x, pivot_y, pivot_z_ = indexed_pivot_point[1]
    shifted_pivot_x, shifted_pivot_y = shift_point(indexed_points, indexed_pivot_point)

    unsigned_alpha = 0 if shifted_pivot_x == 0 else acos(
        (-shifted_pivot_x) / ((shifted_pivot_x**2 + shifted_pivot_y**2)**0.5))
    alpha = -unsigned_alpha if (shifted_pivot_y < 0) else unsigned_alpha
    s = sin(alpha)
    c = cos(alpha)

    unsorted_indexed_angles = []
    for i, p in indexed_points:
        angle = round(
            atan2(c*(p[0]-pivot_x) + s*(pivot_y-p[1]), c*(p[1]-pivot_y)+s*(p[0]-pivot_x)), 4)
        unsorted_indexed_angles.append({"angle": angle, "index": i})

    indexed_angles = [ip for ip in unsorted_indexed_angles if ip["angle"]>=-1.5708]
    min_indexed_angle = min(indexed_angles,
                            key=lambda ia: (ia["angle"], (points[ia["index"]][0]*s + points[ia["index"]][1]*c),
                                            (points[ia["index"]][0]*c - points[ia["index"]][1]*s), points[ia["index"]][2]))

    next_pivot_point_index = min_indexed_angle["index"]

    return next_pivot_point_index


def pick_next_point_shifted_scalar_product(points: List[List[float]], indexed_points: List[Tuple], indexed_pivot_point: Tuple[float]) -> int:
    pivot_x, pivot_y, pivot_z_ = indexed_pivot_point[1]
    shifted_pivot_x, shifted_pivot_y = shift_point(indexed_points, indexed_pivot_point)
    x_mean, y_mean = pivot_x - shifted_pivot_x, pivot_y - shifted_pivot_y
    pivot_sign = 1 if (-1*shifted_pivot_x + 1*shifted_pivot_y) >= 0 else -1

    unsorted_indexed_angles = []
    for i, p in indexed_points:
        sign = 1 if -shifted_pivot_y * (p[0]-x_mean) + shifted_pivot_x*(p[1]-y_mean) > 0 else -1
        scalar_product = (-pivot_x*(p[0]-pivot_x)-pivot_y*(p[1]-pivot_y))/(
            (pivot_x**2+pivot_y**2)**0.5 * ((p[0]-pivot_x)**2+(p[1]-pivot_y)**2)**0.5 + 1e-32)
        angle = round(sign*acos(max(min(scalar_product, 1), -1)), 4)
        unsorted_indexed_angles.append(
            {"angle": angle, "index": i, "sign": sign})

    # there's a problem to understand when we need to take the max/min x and y coordinate at the case when angles are the same
    min_indexed_angle = min(unsorted_indexed_angles, key=lambda ia: (
        ia["angle"], -pivot_sign*(points[ia["index"]][0]-x_mean), pivot_sign*(points[ia["index"]][1]-y_mean), points[ia["index"]][2]))

    print(f"{pivot_sign}, {min_indexed_angle}" if pivot_x == -
          2 and pivot_y == -1 else "")

    return min_indexed_angle["index"]


def pick_next_point_Jarvis(indexed_points: List[Tuple], pivot_point: List[float], prev_point: List[float]) -> int:
    current_vector = [pivot_point[0]-prev_point[0], pivot_point[1]-prev_point[1]]

    unsorted_indexed_cosines = [] 
    for i, p in indexed_points:
        new_vector = [p[0] - pivot_point[0], p[1] - pivot_point[1]]
        len_nv = (new_vector[0]**2 + new_vector[1]**2)**0.5
        cross = -(new_vector[0]*current_vector[1]-new_vector[1]*current_vector[0])
        dot = (new_vector[0]*current_vector[0] + new_vector[1]*current_vector[1]) #/(len_cd*len_nv + 1e-32)
        angle = atan2(cross, dot)
        unsorted_indexed_cosines.append({"angle": angle, "len_nv": len_nv, "z": p[2], "index": i})

    max_indexed_cos = max(unsorted_indexed_cosines, key=lambda ic: (ic["angle"], -ic["len_nv"], -ic["z"]))

    return max_indexed_cos["index"]


pick_next_point = {
    "rotated_atan2": pick_next_point_rotated_atan2,
    "shifted_scalar_product": pick_next_point_shifted_scalar_product,
    "Jarvis": pick_next_point_Jarvis
}
