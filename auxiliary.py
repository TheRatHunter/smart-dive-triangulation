from math import sin, cos, sqrt, atan2, radians


class Coordinates(object):

    @staticmethod
    def distance_between_coordinates_in_km(latitude_1, longitude_1, latitude_2, longitude_2):
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

        return distance

    @staticmethod
    def compute_fake_distances():
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
                Coordinates.distance_between_coordinates_in_km(lats_b1[i], longs_b1[i], lats_p[i], longs_p[i]))
            horizontal_distances_with_b2.append(
                Coordinates.distance_between_coordinates_in_km(lats_b2[i], longs_b2[i], lats_p[i], longs_p[i]))
            horizontal_distances_with_b3.append(
                Coordinates.distance_between_coordinates_in_km(lats_b3[i], longs_b3[i], lats_p[i], longs_p[i]))

        for i in range(len(horizontal_distances_with_b1)):
            print(str(i) + ' ' + str(horizontal_distances_with_b1[i]) + ' ' + str(horizontal_distances_with_b2[i])
                  + ' ' + str(horizontal_distances_with_b3[i]))

        # TODO : passer à la distance diagonale avec la profondeur


if __name__ == '__main__':
    d = Coordinates().distance_between_coordinates_in_km(12, 3, 15, 9)
    print('Result : ' + str(d) + ' km.')
    Coordinates().compute_fake_distances()
