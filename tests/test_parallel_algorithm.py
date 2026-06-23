from copy import deepcopy

import pytest
from sorting_parallelly import sort_points_parallelly_x, sort_points_parallelly_y


class TestSortingParallellyYAlgorithm:
    @pytest.fixture
    def sorting_points_test_base_cases(self):
        default_max_delta = 1
        return [
            # (input points, showing result, output groups of points ids)
            ([], default_max_delta, False, []),
            ([[2, 2, 3]], default_max_delta, False, [[0]]),
            ([[1, 1, 1], [2, 1, 1], [1, 2, 1], [2, 2, 1]],
             default_max_delta, False, [[0, 2], [1, 3]]),
            ([[1, 1, 1], [2, 1.5, 1], [3, 1, 1], [4, 1.5, 1], [1, 2, 1],
             [3, 2, 1]], default_max_delta, False, [[0, 4], [1], [2, 5], [3]]),
            ([[2, 1, 1], [2, 2, 1], [1, 1, 1], [1, 2, 1]],
             default_max_delta*2, False, [[2, 0, 3, 1]]),
            ([[1, 1, 1], [1.5, 1.3, 1], [2, 1, 1], [2.5, 1.5, 1], [3, 1, 1],
              [1, 2, 1], [1.5, 2.5, 1], [2, 2, 1], [2.5, 2.3, 1], [3, 2, 1],
              [2, 3, 1], [2.5, 3.5, 1], [3, 3, 1], [3.5, 3.5, 1], [4, 3, 1]],
             default_max_delta, False, [[0, 1, 5, 6], [2, 3, 7, 8, 10, 11], [4, 9, 12, 13], [14]])
        ]

    def test_base_cases(self, sorting_points_test_base_cases):
        for points, max_delta, showing_result, expected_groups_ids in sorting_points_test_base_cases:
            groups_ids = sort_points_parallelly_y(
                points, max_delta, showing_result)
            assert groups_ids == expected_groups_ids

    def test_immutable_points(self):
        points = [[-1, 1, 1], [4, 2, 1], [-3, 2, 1], [7, -3, 5]]
        _check_immutability_input(points, sort_points_parallelly_y)

class TestSortingParallellyXAlgorithm:
    @pytest.fixture
    def sorting_points_test_base_cases(self):
        default_max_delta = 1
        return [
            # (input points, showing result, output groups of points ids)
            ([], default_max_delta, False, []),
            ([[2, 2, 3]], default_max_delta, False, [[0]]),
            ([[1, 1, 1], [2, 1, 1], [1, 2, 1], [2, 2, 1]],
             default_max_delta, False, [[0, 1], [2, 3]]),
            ([[2, 1, 1], [2, 2, 1], [1, 1, 1], [1, 2, 1]],
             default_max_delta, False, [[2, 0], [3, 1]]),
            ([[1, 1, 1], [2, 1.5, 1], [3, 1, 1], [4, 1.5, 1], [1, 2, 1],
             [3, 2, 1]], default_max_delta, False, [[0, 1, 2, 3], [4, 5]]),
            ([[2, 1, 1], [2, 2, 1], [1, 1, 1], [1, 2, 1]],
             default_max_delta*2, False, [[2, 3, 0, 1]]),
            ([[1, 1, 1], [1.5, 1.3, 1], [2, 1, 1], [2.5, 1.5, 1], [3, 1, 1],
              [1, 2, 1], [1.5, 2.5, 1], [2, 2, 1], [2.5, 2.3, 1], [3, 2, 1],
              [2, 3, 1], [2.5, 3.5, 1], [3, 3, 1], [3.5, 3.5, 1], [4, 3, 1]],
             default_max_delta, False, [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]),
            ([[2, 2, 1], [1.5, 1.5, 1], [4, 3, 1], [2.5, 1.5, 1], [3, 1, 1],
              [1, 2, 1], [1.5, 2.5, 1], [1, 1, 1], [2.5, 2.5, 1], [3, 2, 1],
              [2, 3, 1], [2.5, 3.5, 1], [3, 3, 1], [3.5, 3.5, 1], [2, 1, 1]],
             default_max_delta, False, [[7, 1, 14, 3, 4], [5, 6, 0, 8, 9], [10, 11, 12, 13, 2]])
        ]

    def test_base_cases(self, sorting_points_test_base_cases):
        for points, max_delta, showing_result, expected_groups_ids in sorting_points_test_base_cases:
            groups_ids = sort_points_parallelly_x(
                points, max_delta, showing_result)
            assert groups_ids == expected_groups_ids

    def test_immutable_points(self):
        points = [[-1, 1, 1], [4, 2, 1], [-3, 2, 1], [7, -3, 5]]
        _check_immutability_input(points, sort_points_parallelly_x)

def _check_immutability_input(arr, callback):
    d_arr = deepcopy(arr)
    callback(d_arr)
    assert d_arr == arr