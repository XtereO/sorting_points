from copy import deepcopy

import pytest
from sorting_parallelly import sort_points_parallelly_x


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
             default_max_delta*2, True, [[2, 3, 0, 1]]),
        ]

    def test_base_cases(self, sorting_points_test_base_cases):
        for points, max_delta, showing_result, expected_groups_ids in sorting_points_test_base_cases:
            groups_ids = sort_points_parallelly_x(
                points, max_delta, showing_result)
            assert groups_ids == expected_groups_ids

    def test_immutable_points(self):
        points = [[-1, 1, 1], [4, 2, 1], [-3, 2, 1], [7, -3, 5]]
        d_points = deepcopy(points)
        groups_ids = sort_points_parallelly_x(points)
        assert points == d_points
