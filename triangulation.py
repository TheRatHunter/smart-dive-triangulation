from math import sqrt


class Triangulation(object):
    @staticmethod
    def get_depth_from_pressure(pressure):
        """
        Get depth from pressure
        :param pressure: pressure in bars
        :return: Depth in m
        """
        return 10*(pressure-1)

    @staticmethod
    def get_horizontal_dist_from_diag_and_depth(diagonal_dist, depth):
        """
        Pythagoras theorem to compute horizontal distance
        :param diagonal_dist: Diagonal dist gotten from ultrasound device
        :param depth: depth of the diver
        :return: Horizontal dist
        """
        return sqrt(diagonal_dist*diagonal_dist - depth*depth)

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
        return [0.0, 0.0]

    @staticmethod
    def run():
        print('Hello, world!')


if __name__ == '__main__':
    Triangulation().run()
