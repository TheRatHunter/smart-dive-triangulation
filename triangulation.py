from math import sin, cos, sqrt, atan2, radians


class Triangulation(object):
    @staticmethod
    def distance_between_coordinates_in_m(latitude_1, longitude_1, latitude_2, longitude_2):
        """
        Returns distance between two coordinates in km
        :param latitude_1:
        :param longitude_1:
        :param latitude_2:
        :param longitude_2:
        :return: distance
        """
        # approximate radius of earth in km
        r = 6373.0

        lat1 = radians(latitude_1)
        lon1 = radians(longitude_1)
        lat2 = radians(latitude_2)
        lon2 = radians(longitude_2)

        d_lon = lon2 - lon1
        d_lat = lat2 - lat1

        a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = r * c

        return distance*1000

    @staticmethod
    def get_depth_from_pressure(pressure):
        """
        Get depth from pressure
        :param pressure: pressure in bars
        :return: Depth in m
        """
        return 10 * (pressure - 1)

    @staticmethod
    def get_horizontal_dist_from_diag_and_depth(diagonal_dist, depth):
        """
        Pythagoras theorem to compute horizontal distance
        :param diagonal_dist: Diagonal dist gotten from ultrasound device
        :param depth: depth of the diver
        :return: Horizontal dist
        """
        return sqrt(diagonal_dist * diagonal_dist - depth * depth)

    @staticmethod
    def circle_intersection(circle1, circle2):
        """
        @summary: calculates intersection points of two circles
        Credits to https://gist.github.com/xaedes/974535e71009fa8f090e
        @param circle1: tuple(x,y,radius)
        @param circle2: tuple(x,y,radius)
        @result: (point1, point2, dx, dy) tuple of intersection points (which are (x,y) tuple) and meter delta
        in x and y
        """
        # return self.circle_intersection_sympy(circle1,circle2)
        x1, y1, r1 = circle1
        x2, y2, r2 = circle2
        # http://stackoverflow.com/a/3349134/798588
        dx, dy = x2 - x1, y2 - y1

        # Pass coordinates difference in m difference
        x_on_y_ratio = dx / dy
        distance_in_m = Triangulation.distance_between_coordinates_in_m(x1, y1, x2, y2)
        dy = sqrt((distance_in_m * distance_in_m) / (x_on_y_ratio * x_on_y_ratio + 1))
        dx = x_on_y_ratio * dy

        d = sqrt(dx * dx + dy * dy)
        if d > r1 + r2:
            print('#1 d : ' + str(d) + ' r1 : ' + str(r1) + ' r2 : ' + str(r2))
            return None  # no solutions, the circles are separate
        if d < abs(r1 - r2):
            print('#2 d : ' + str(d) + ' r1 : ' + str(r1) + ' r2 : ' + str(r2))
            return None  # no solutions because one circle is contained within the other
        if d == 0 and r1 == r2:
            print('#3 d : ' + str(d) + ' r1 : ' + str(r1) + ' r2 : ' + str(r2))
            return None  # circles are coincident and there are an infinite number of solutions

        a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
        h = sqrt(r1 * r1 - a * a)
        xm = x1 + a * dx / d
        ym = y1 + a * dy / d
        xs1 = xm + h * dy / d
        xs2 = xm - h * dy / d
        ys1 = ym - h * dx / d
        ys2 = ym + h * dx / d

        return (xs1, ys1), (xs2, ys2), dx, dy

    @staticmethod
    def find_closest_points_amongst_4(p1, p2, p3, p4):
        """
        Find good intersection
        :param p1: (x1, y1) tuple
        :param p2: //
        :param p3: //
        :param p4: //
        :return:
        """
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4
        min_point = min(abs(x1 - x3) + abs(y1 - y3),
                        abs(x1 - x4) + abs(y1 - y4),
                        abs(x2 - x3) + abs(y2 - y3),
                        abs(x2 - x4) + abs(y2 - y4))

        if min_point == abs(x1 - x3) + abs(y1 - y3) or min_point == abs(x1 - x4) + abs(y1 - y4):
            point = p1
        else:
            point = p2

        return point

    @staticmethod
    def triangulate(b1_lat, b1_long, b2_lat, b2_long, b3_lat, b3_long,
                    horizontal_dist1, horizontal_dist2, horizontal_dist3):
        """
        Compute diver's GPS coordinates
        :param b1_lat: Latitude of the beacon 1
        :param b1_long: Longitude of the beacon 1
        :param b2_lat: Latitude of the beacon 2
        :param b2_long: Longitude of the beacon 2
        :param b3_lat: Latitude of the beacon 3
        :param b3_long: Longitude of the beacon 3
        :param horizontal_dist1: Horizontal distance between diver and beacon 1
        :param horizontal_dist2: Horizontal distance between diver and beacon 2
        :param horizontal_dist3: Horizontal distance between diver and beacon 3
        :return: GPS Coordinates of the diver
        """
        inters1 = Triangulation.circle_intersection((b1_lat, b1_long, horizontal_dist1),
                                                    (b2_lat, b2_long, horizontal_dist2))
        inters2 = Triangulation.circle_intersection((b1_lat, b1_long, horizontal_dist1),
                                                    (b3_lat, b3_long, horizontal_dist3))
        good_intersection_meters = Triangulation.find_closest_points_amongst_4(inters1[0], inters1[1], inters2[0],
                                                                               inters2[1])

        # Transform the coordinates back in GPS
        dx_meters_1_2 = inters1[2]
        dy_meters_1_2 = inters1[3]
        dx_coordinates_1_2 = abs(b1_lat - b2_lat)
        dy_coordinates_1_2 = abs(b1_long - b2_long)

        good_intersection_coordinates = [-1.0, -1.0]
        if dx_meters_1_2 == 0:
            dx_meters_1_2 = 1
        if dy_meters_1_2 == 0:
            dy_meters_1_2 = 1
        if dx_meters_1_2 != 0 and dx_meters_1_2 != 0:
            good_intersection_coordinates = \
                [b1_lat + ((good_intersection_meters[0] / dx_meters_1_2) * dx_coordinates_1_2),
                 b1_long + ((good_intersection_meters[1] / dy_meters_1_2) * dy_coordinates_1_2)]

        print('+-------- Diver\'s GPS coordinates computation -------------')
        print('| Beacon 1 : (' + "{0:.2f}".format(b1_lat) + ', ' + "{0:.2f}".format(
            b1_long) + ')')
        print('| Beacon 2 : (' + "{0:.2f}".format(b2_lat) + ', ' + "{0:.2f}".format(
            b2_long) + ')')
        print('| Beacon 3 : (' + "{0:.2f}".format(b3_lat) + ', ' + "{0:.2f}".format(
            b3_long) + ')')
        print('| Diver distances: (' + "{0:.2f}".format(horizontal_dist1) + ", " + "{0:.2f}".format(
            horizontal_dist2) + ', ' + "{0:.2f}".format(horizontal_dist3) + ')')
        print('| Point found in meters delta from b1 : (' + "{0:.2f}".format(good_intersection_meters[0]) + ', ' +
              "{0:.2f}".format(good_intersection_meters[1]) + ')')
        print('| Point found in GPS : (' + "{0:.2f}".format(good_intersection_coordinates[0]) + ', ' +
              "{0:.2f}".format(good_intersection_coordinates[1]) + ')')
        print('+----------------------------------------------------------')

        return [good_intersection_coordinates[0], good_intersection_coordinates[1]]
