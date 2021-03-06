# -*- coding: utf-8 -*-
from math import sqrt

from triangulation import Triangulation


class Coordinates(object):

    @staticmethod
    def compute_fake_distances():
        """
        Computes the distances for fake coordinates
        :return: List of distances for each beacon
        """
        lats_b1 = [42.475537,
                   42.462165,
                   42.459861,
                   42.487563,
                   42.468548,
                   42.445896,
                   42.495632,
                   42.458961,
                   42.464587,
                   42.431256,
                   42.459864,
                   42.485214,
                   42.484562]
        longs_b1 = [3.476611,
                    3.497214,
                    3.486521,
                    3.465423,
                    3.498541,
                    3.475632,
                    3.475698,
                    3.482541,
                    3.476589,
                    3.463251,
                    3.463254,
                    3.485201,
                    3.458900]

        lats_b2 = [42.459861,
                   42.495632,
                   42.445896,
                   42.462165,
                   42.468548,
                   42.475537,
                   42.487563,
                   42.485214,
                   42.464587,
                   42.484562,
                   42.431256,
                   42.459864,
                   42.458961]
        longs_b2 = [3.576611,
                    3.575632,
                    3.582541,
                    3.565423,
                    3.585201,
                    3.597214,
                    3.575698,
                    3.586521,
                    3.576589,
                    3.598541,
                    3.563254,
                    3.563251,
                    3.558900]

        lats_b3 = [42.587563,
                   42.568548,
                   42.559861,
                   42.559864,
                   42.584562,
                   42.545896,
                   42.595632,
                   42.562165,
                   42.564587,
                   42.531256,
                   42.525537,
                   42.585214,
                   42.558961]
        longs_b3 = [3.576611,
                    3.558900,
                    3.586521,
                    3.575632,
                    3.598541,
                    3.565423,
                    3.575698,
                    3.585201,
                    3.576589,
                    3.563251,
                    3.563254,
                    3.597214,
                    3.575406]

        lats_p = [42.588544,
                  42.565214,
                  42.558523,
                  42.557459,
                  42.588456,
                  42.544587,
                  42.591265,
                  42.563269,
                  42.561204,
                  42.530021,
                  42.523698,
                  42.581254,
                  42.550789]
        longs_p = [3.574569,
                   3.555524,
                   3.587894,
                   3.576532,
                   3.597854,
                   3.561022,
                   3.572266,
                   3.589884,
                   3.577845,
                   3.562653,
                   3.567854,
                   3.596694,
                   3.572235]

        horizontal_distances_with_b1 = []
        horizontal_distances_with_b2 = []
        horizontal_distances_with_b3 = []
        for i in range(len(lats_b1)):
            horizontal_distances_with_b1.append(
                Triangulation.distance_between_coordinates_in_m(lats_b1[i], longs_b1[i], lats_p[i], longs_p[i]))
            horizontal_distances_with_b2.append(
                Triangulation.distance_between_coordinates_in_m(lats_b2[i], longs_b2[i], lats_p[i], longs_p[i]))
            horizontal_distances_with_b3.append(
                Triangulation.distance_between_coordinates_in_m(lats_b3[i], longs_b3[i], lats_p[i], longs_p[i]))

        pressures = [1.2,
                     1.9,
                     2.6,
                     3.8,
                     4.7,
                     5.2,
                     5.6,
                     5.3,
                     4.9,
                     3.8,
                     2.5,
                     1.9,
                     1.1]
        depths = []
        for i in pressures:
            depths.append(10 * (i - 1))

        diagonal_distances_with_b1 = []
        diagonal_distances_with_b2 = []
        diagonal_distances_with_b3 = []
        for i in range(len(depths)):
            diagonal_distances_with_b1.append(
                sqrt((depths[i] * depths[i]) +
                     (horizontal_distances_with_b1[i] * horizontal_distances_with_b1[i])))
            diagonal_distances_with_b2.append(
                sqrt((depths[i] * depths[i]) +
                     (horizontal_distances_with_b2[i] * horizontal_distances_with_b2[i])))
            diagonal_distances_with_b3.append(
                sqrt((depths[i] * depths[i]) +
                     (horizontal_distances_with_b3[i] * horizontal_distances_with_b3[i])))

        print('Diagonal distances : ')
        for i in range(len(horizontal_distances_with_b1)):
            print('Diagonal : ' + str(diagonal_distances_with_b1[i]) + ', horizontal : '
                  + str(horizontal_distances_with_b1[i]) + ', vertical : ' + str(depths[i]))
        print('---')
        for i in range(len(horizontal_distances_with_b2)):
            print('Diagonal : ' + str(diagonal_distances_with_b2[i]) + ', horizontal : '
                  + str(horizontal_distances_with_b2[i]) + ', vertical : ' + str(depths[i]))
        print('---')
        for i in range(len(horizontal_distances_with_b3)):
            print('Diagonal : ' + str(diagonal_distances_with_b3[i]) + ', horizontal : '
                  + str(horizontal_distances_with_b3[i]) + ', vertical : ' + str(depths[i]))

        return [diagonal_distances_with_b1, diagonal_distances_with_b2, diagonal_distances_with_b3]


if __name__ == '__main__':
    d = Triangulation().distance_between_coordinates_in_m(12, 3, 15, 9)
    print('Result : ' + str(d) + ' km.')
    diagonal_d = Coordinates().compute_fake_distances()
