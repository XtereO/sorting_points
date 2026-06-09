from copy import deepcopy
from main import sort_points_spirally


class TestSortingSpirallyAlgorithm:
    def test_empty_points(self):
        points_order = sort_points_spirally([])
        assert points_order == []

    def test_one_point(self):
        points_order = sort_points_spirally([[1, 7, 17]])
        assert points_order == [0]

    def test_picking_pivot_point(self):
        points_order = sort_points_spirally([[-1, 1, 1], [0, 2, 3]])
        assert points_order[0] == 0

        points_order = sort_points_spirally([[0, 2, 3], [-1, 1, 1]])
        assert points_order[0] == 1

        points_order = sort_points_spirally(
            [[-3, 2, 2], [-1, -5, 0], [-3, 1, 5], [7, -3, 5]])
        assert points_order[0] == 2

        points_order = sort_points_spirally(
            [[-3, 2, 2], [-1, -5, 0], [-3, 2, 5], [7, -3, 5]])
        assert points_order[0] == 0

        points_order = sort_points_spirally(
            [[-3, 2, 2], [-1, -5, 0], [-3, 2, 1], [7, -3, 5]])
        assert points_order[0] == 2

        points_order = sort_points_spirally(
            [[-3, 2, 1], [-1, -5, 0], [-3, 2, 1], [7, -3, 5]])
        assert points_order[0] == 0

    def test_two_points(self):
        points_order = sort_points_spirally([[-1, 1, 1], [4, 2, 1]])
        assert points_order == [0, 1]

        points_order = sort_points_spirally([[4, 2, 1], [-1, 1, 1]])
        assert points_order == [1, 0]

    def test_immutable_points(self):
        points = [[-1, 1, 1], [4, 2, 1], [-3, 2, 1], [7, -3, 5]]
        d_points = deepcopy(points)
        points_order = sort_points_spirally(points)
        assert points == d_points

    def test_case_one_simple_square(self):
        p0, p1, p2, p3 = ([-1, -1, 2], [-1, 1, 0], [1, 1, 5], [1, -1, 5])

        points_order = sort_points_spirally([p0, p1, p2, p3])
        assert points_order == [0, 1, 2, 3]

        points_order = sort_points_spirally([p2, p1, p0, p3])
        assert points_order == [2, 1, 0, 3]

    def test_case_two_simple_curve(self):
        p0, p1, p2, p3, p4, p5 = (
            [-2, -1, 1], [-1, 2, 2], [2, 1, 2], [2, -2, 1], [-1, -1, 0], [0, 1, 0])

        points_order = sort_points_spirally([p0, p1, p2, p3, p4, p5])
        assert points_order == [0, 1, 2, 3, 4, 5]

        points_order = sort_points_spirally([p2, p1, p5, p0, p3, p4])
        assert points_order == [3, 1, 0, 4, 5, 2]

    def test_case_three_curve(self):
        p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12 = ([-3, -2, 1], [-2, 3, 0], [-1, 3, 3], [3, 2, -2], [
                                                                 2, -3, 1], [0, -3, 1], [-1, -2, 1], [-2, 2, 1], [0, 2, 7], [2, 2, 1], [1, 0, 0], [0, -1, 2], [0, 0, 0])

        points_order = sort_points_spirally(
            [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12])
        assert points_order == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        points_order = sort_points_spirally(
            [p3, p5, p1, p11, p7, p6, p0, p12, p10, p9, p2, p8, p4])
        assert points_order == [6, 2, 10, 0, 12, 1, 5, 4, 11, 9, 8, 3, 7]

    def test_case_four_square(self):
        p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24 = (
            [-2, -2, 0], [-2, -1, 0], [-2, 0, 0], [-2, 1, 0], [-2,
                                                               2, 0], [-1, 2, 0], [0, 2, 0], [1, 2, 0], [2, 2, 0],
            [2, 1, 0], [2, 0, 0], [2, -1, 0], [2, -2,
                                               0], [1, -2, 0], [0, -2, 0], [-1, -2, 0],
            [-1, -1, 0], [-1, 0, 0], [-1, 1, 0], [0, 1, 0], [1, 1, 0], [1, 0, 0], [1, -1, 0], [0, -1, 0], [0, 0, 0])

        points_order = sort_points_spirally([p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10,
                                            p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24])
        assert points_order == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

        points_order = sort_points_spirally([p12, p3, p19, p7, p1, p22, p0, p15, p8, p20,
                                             p4, p17, p10, p14, p6, p11, p2, p23, p5, p18,
                                             p9, p21, p16, p13, p24])
        assert points_order == [6, 4, 16, 1, 10, 18, 14, 3, 8, 20,
                                12, 15, 0, 23, 13, 7, 22, 11, 19, 2, 9, 21, 5, 17, 24]

    def test_case_five_horizontal_line(self):
        p0, p1, p2, p3, p4 = (
            [-3, 1, 0], [-2, 1, 0], [-1, 1, 0], [0, 1, 0], [1, 1, 1])
        points_order = sort_points_spirally([p0, p1, p2, p3, p4])
        assert points_order == [0, 1, 2, 3, 4]

        points_order = sort_points_spirally([p2, p3, p1, p0, p4])
        assert points_order == [3, 2, 0, 1, 4]

        p0, p1, p2, p3, p4 = (
            [-3, -1, 0], [-2, -1, 0], [-1, -1, 0], [0, -1, 0], [1, -1, 1])
        points_order = sort_points_spirally([p0, p1, p2, p3, p4])
        assert points_order == [0, 1, 2, 3, 4]

        points_order = sort_points_spirally([p3, p2, p4, p0, p1])
        assert points_order == [3, 4, 1, 0, 2]

    def test_case_six_vertical_line(self):
        p0, p1, p2, p3, p4 = ([-2, -3, 0], [-2, -2, 0],
                              [-2, -1, 0], [-2, 0, 0], [-2, 1, 0])
        points_order = sort_points_spirally([p0, p1, p2, p3, p4])
        assert points_order == [0, 1, 2, 3, 4]

        points_order = sort_points_spirally([p3, p1, p2, p0, p4])
        assert points_order == [3, 1, 2, 0, 4]

        p0, p1, p2, p3, p4 = ([2, -2, 0], [2, -1, 0],
                              [2, 0, 0], [2, 1, 0], [2, 2, 0])
        points_order = sort_points_spirally([p0, p1, p2, p3, p4])
        assert points_order == [0, 1, 2, 3, 4]

        points_order = sort_points_spirally([p2, p4, p0, p1, p3])
        assert points_order == [2, 3, 0, 4, 1]

    def test_case_seven_shifted_points(self):
        points = [[-2, -2, 1], [-1.9, -1, 1], [-1.5, 0, 1], [-1, 1, 0], [
            0, 1.2, 0], [1, 0.8, 0], [1.5, 0, 0], [1, -1, 0], [0, -0.7, 0], [0, 0, 0], [0.1, 0, 0]]
        p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 = tuple(points)
        points_order = sort_points_spirally(
            [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
        assert points_order == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        points_order = sort_points_spirally(
            [p3, p1, p10, p5, p6, p2, p0, p7, p8, p4, p9])
        assert points_order == [6, 1, 5, 0, 9, 3, 4, 7, 8, 10, 2]

        shift_x, shift_y = 51, 98
        p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 = tuple(
            map(lambda p: [p[0]+shift_x, p[1]+shift_y, p[2]], points))
        points_order = sort_points_spirally(
            [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
        assert points_order == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        points_order = sort_points_spirally(
            [p7, p2, p1, p0, p8, p10, p4, p3, p6, p5, p9])
        assert points_order == [3, 2, 1, 7, 6, 9, 8, 0, 4, 10, 5]

        shift_x, shift_y = -63, 87
        p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 = tuple(
            map(lambda p: [p[0]+shift_x, p[1]+shift_y, p[2]], points))
        points_order = sort_points_spirally(
            [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
        assert points_order == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        points_order = sort_points_spirally(
            [p4, p1, p8, p9, p2, p10, p3, p0, p6, p5, p7])
        assert points_order == [7, 1, 4, 6, 0, 9, 8, 10, 2, 3, 5]

        shift_x, shift_y = -29, -28
        p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 = tuple(
            map(lambda p: [p[0]+shift_x, p[1]+shift_y, p[2]], points))
        points_order = sort_points_spirally(
            [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
        assert points_order == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        points_order = sort_points_spirally(
            [p7, p2, p1, p8, p10, p0, p6, p3, p5, p4, p9])
        assert points_order == [5, 2, 1, 7, 9, 8, 6, 0, 3, 10, 4]

        shift_x, shift_y = 37, -49
        p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 = tuple(
            map(lambda p: [p[0]+shift_x, p[1]+shift_y, p[2]], points))
        points_order = sort_points_spirally(
            [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
        assert points_order == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        points_order = sort_points_spirally(
            [p10, p2, p7, p6, p0, p1, p9, p5, p4, p8, p3])
        assert points_order == [4, 5, 1, 10, 8, 7, 3, 2, 9, 6, 0]

    def test_case_eight_similar_points_xy(self):
        p0, p1, p2, p3, p4 = ([-1, -1, 0], [-1, 1, 0],
                              [-1, 1, 2], [1, 1, 0], [1, -1, 0])
        points_order = sort_points_spirally([p0, p1, p2, p3, p4])
        assert points_order == [0, 1, 2, 3, 4]

        points_order = sort_points_spirally([p3, p0, p4, p1, p2])
        assert points_order == [1, 3, 4, 0, 2]

        points_order = sort_points_spirally([p3, p0, p4, p2, p1])
        assert points_order == [1, 4, 3, 0, 2]

        p0, p1, p2, p3, p4, p5 = ([-1, -1, 0], [-1, 1, 0], [-1, 1, 1],
                                  [-1, 1, 2], [1, 1, 0], [1, -1, 0])
        points_order = sort_points_spirally([p0, p1, p2, p3, p4, p5])
        assert points_order == [0, 1, 2, 3, 4, 5]

    def test_case_nine_four_grouped_points(self):
        points = [[-6, -2, 0], [-6, 0, 0], [-5, 0, 0], [-5, -2, 0],
                  [-5, 5, 0], [-5, 6, 0], [-3, 6, 0], [-3, 5, 0],
                  [3, 4, 0], [3, 5, 0], [4, 5, 0], [4, 4, 0],
                  [4, 0, 0], [5, 0, 0], [5, -1, 0], [4, -1, 0],
                  [0, -5, 0], [0, -4, 0], [1, -4, 0], [1, -5, 0],
                  [-3, 1, 0], [-3, 2, 0], [-2, 2, 0], [-2, 1, 0],
                  [1, 2, 0], [1, 3, 0], [2, 3, 0], [2, 2, 0],
                  [0, 0, 0], [0, 1, 0], [1, 1, 0], [1, 0, 0]]
        points_order = sort_points_spirally(points)
        assert points_order == [0, 1, 5, 6, 10, 13, 14, 19, 16, 3, 2, 4, 7, 9,
                                11, 12, 15, 18, 17, 20, 21, 8, 27, 31, 28, 23, 22, 25, 26, 30, 29, 24]

    def test_case_ten_spiral_in_one_area(self):
        p0, p1, p2, p3, p4, p5, p6 = ([-5, 0, 3], [-3, 4, 3], [2, 3, 0],
                                      [3, -3, 0], [-2, 0, 0], [-2, 1, 0], [-1, 1, 0])
        points_order = sort_points_spirally([p0, p1, p2, p3, p4, p5, p6])
        assert points_order == [0, 1, 2, 3, 4, 5, 6]

        points_order = sort_points_spirally([p5, p2, p4, p1, p6, p0, p3])
        assert points_order == [5, 3, 1, 6, 2, 0, 4]

    def test_case_eleven_pivot_point_the_highest(self):
        points = [[-4, 4, 1], [-3, 2, 2], [-2, 1, 0], [0, -1, 0], [1, 1, 0], [3, 2, 1],
                  [2, 3, 0], [1, 1, 0], [0, 0, 0], [-0.6, 0.5, 2], [-1, 1, 1], [0, 0.5, 2]]
        points_order = sort_points_spirally(points)
        assert points_order == [0, 6, 5, 3, 2, 1, 4, 7, 8, 9, 10, 11]
