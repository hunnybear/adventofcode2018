# the one about the points and the expansion.
#
"""
What I'm thinking, is, there's probably a function for a pair of curves that describe
an area kinda looking like an iscosoles triangle with the even sides 'deflated' a
bit, and the altitude being a vector that is [1|-1],0  or 0, [1|-1]. if there are no
points inside that area, we're good (the curve because the determinant is nearness to
the point, and so if we just shot a 45 degree ray out, that wouldn't work, because if
a point is right outside that 45 90 units away, then it doesn't work, but if it's 91
units outside 90 [manhattan] units away, we're good)
"""

import copy

X = 0
Y = 1


class NotCalculated(object):
    def __str__(self):
        return('(*, *)')

NOT_CALCULATED = NotCalculated()

def print_grid(grid):
    for row in grid:
        print(' '.join("{:^8s}".format(str(cell)) for cell in row))


def get_point_owner(grid, point, points_of_interest):
    # TODO
    pass

def _get_manhattan_distance(point_a, point_b):

    return abs(point_a[X] - point_b[X]) + abs(point_a[Y] - point_b[Y])


def _get_midpoint(point_a, point_b):
    return ((point_a[X] + point_b[X]) / 2., (point_a[Y] + point_b[Y]) / 2.)


def _get_boundary_function(point_a, point_b):
    # This could be done a bit more intelligently (figure out a deterministic
    # Function to define the boundary as a function (a polyline definin))
    midpoint = _get_midpoint(point_a, point_b)
    if midpoint - int(midpoint):
        # the midpoint occurs between two points, thus it is a "clean" boundary
        # (no unclaimed tiles)
        # TODO
        pass

    else:
        # TODO
        pass


def just_generate_the_fucking_thing(points_of_interest):
    """
    I've been trying to be Too Clever(tm)
    """

    sorted_x = sorted(points_of_interest)
    sorted_y = sorted(points_of_interest, key=lambda poi: tuple(reversed(poi)))

    min_x = sorted_x[0][X]
    min_y = sorted_y[0][Y]
    max_x = sorted_x[-1][X]
    max_y = sorted_y[-1][Y]

    grid = [[NOT_CALCULATED for _j in range(max_y + 2)] for _i in range(max_x + 2)]

    center = (
        (min_x + max_x) / 2,
        (min_y + max_y) / 2
    )

    points_from_center = sorted(points_of_interest, key=lambda poi:_get_manhattan_distance(center, poi))

    print('debug output:')
    print(center)
    print(sorted_x)
    print(sorted_y)
    print(points_from_center)


    for point in points_from_center:
        assert points_of_interest.count(point) == 1
        try:
            grid[point[X]][point[Y]] = point
        except  IndexError:
            import pdb
            pdb.set_trace()

    range = 1
    active_points = copy.copy(points_from_center)
    for point in points_from_center:
    print_grid(grid)





def _check_occludes(x, y):
    """
    x and y are relative to the ray that is imagined shot from the 'source'
    point 'outwards', with y along the axis, positive y being along the ray
    originating from y = 0 at the origin of the ray, and positive x being
    perpendicular to that ray in the direction that makes it most approach the
    position of the possible occluder
    """

    return abs(x) * 2 >= abs(y)


def zone_occludes(source, occluder):
    """
    Check whether the zone from point `occluder` occludes the zone from point
    `source` (meaning it blocks the infinite expansion of zone created by
    `source`).

    ## INPUTS: ##

        * source    <`tuple<int, int>`> source point
        * occluder  <`tuple<int, int>`> occluder point

    ## RETURNS: ##

        *   <`bool`>            True if `occluder`'s zone occludes
                                        `source`'s zone

    ## AUTHOR: ##

        * Tyler Jachetta, me@tylerjachetta.net

    """

    occludes_pos_x = False
    occludes_neg_x = False
    occludes_pos_y = False
    occludes_neg_y = False

    x = 0
    y = 1

    rel_vector = (source[x] - occluder[x], source[y] - occluder[y])

    # Normalized, cardinal directional vector components
    cardinal_x = int(rel_vector[x] / abs_rel_vector[x])
    cardinal_y = int(rel_vector[y] / abs_rel_vector[y])

    assert cardinal_x in [-1, 0, 1]
    assert cardinal_y in [-1, 0, 1]

    if abs(rel_vector[x]) > abs(rel_vector[y]):
        occludes = _check_occludes(rel_vector[y], rel_vector[x])
    elif abs(rel_vector[x]) < abs(rel_vector[y]):
        occludes = _check_occludes(rel_vector[x], rel_vector[y])
    else:
        occludes = False

    assert constrained_vector[x] or constrained_vector[y]

    if constrained_vector[x]:

        if cardinal_y == 0:
            # Points are stacked, excludes vertically and totally in
            # one direction
            assert cardinal_x != 0

            if cardinal_x == 1:
                occludes_pos_x = True
            else:
                # cardinal_y == -1
                occludes_neg_x = True

        elif occluder[x] > source[x]:
            # TODO
            pass
        elif source[x] > occluder[x]:
            # TODO
            pass
        else:
            assert False

    if constrained_vector[y]:

        if cardinal_x == 0:
            # points are stacked, occludes exclusively and totally
            # in exactly one direction

            assert cardinal_y != 0

            if cardinal_y == 1:
                occludes_pos_y = True

            else:
                # cardinal_y == -1
                occludes_neg_y = True

        elif occluder[y] > source[y]:
            # cardinal_x == 0 might be true
            # TODO
            pass

        elif occluder[y] < source[y]:
            # cardinal_x == 0 might be true
            # TODO
            pass

        else:
            assert False


def part_01(input_data):
    coordinate_strings = input_data.strip().splitlines()
    coordinates = [tuple(int(i.strip()) for i in coord.split(',')) for coord in coordinate_strings]
    grid = just_generate_the_fucking_thing(coordinates)

