import pytest
from sorting_parallelly import sort_points_parallelly_x

class TestSortingParallellyXAlgorithm:
    @pytest.fixture
    def sorting_points_test_base_cases(self):
        """Fixture providing test cases for calculate_discount."""
        return [
        # (input points, showing result, output groups of points ids)
            ([], False, []),
            ([[2, 2]], False, [[0]])
        ]

    def test_base_cases(self, sorting_points_test_base_cases):
        """Test calculate_discount with multiple cases."""
        for points, showing_result, expected_groups_ids in sorting_points_test_base_cases:
            groups_ids = sort_points_parallelly_x(points, showing_result)
            assert groups_ids == expected_groups_ids
    
    # tests for picking pivot point, immutability 
