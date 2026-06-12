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
            ([[1,1,1], [2, 1, 1], [1,2,1], [2,2,1]], default_max_delta, False, [[0, 1], [2, 3]]),
            ([[2,1,1], [2,2,1], [1,1,1], [1,2,1]], default_max_delta, False, [[2, 0], [3, 1]]),

        ]

    def test_base_cases(self, sorting_points_test_base_cases):
        for points, max_delta, showing_result, expected_groups_ids in sorting_points_test_base_cases:
            groups_ids = sort_points_parallelly_x(points, max_delta, showing_result)
            assert groups_ids == expected_groups_ids
    
    # tests for immutability 
