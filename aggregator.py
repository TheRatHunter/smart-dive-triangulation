import csv, sys

from triangulation import Triangulation


class Aggregator(object):
    @staticmethod
    def find_minimum_gap_index(value, list):
        """
        Return the index of the closest value from 'value' in list (used to find closest timestamp)
        :param value: The value to look for
        :param list: The list to be searched
        :return: Index of the min gap
        """
        min_val = sys.float_info.max
        min_index = -1
        for val in list:
            if abs(value - val) < min_val:
                min_val = value - val
                min_index = list.index(val)

        return min_index

    @staticmethod
    def aggregate(b1_path, b2_path, b3_path, p_path):
        """
        Parses CSV files and combines them into a tab with all relevant data
        :param b1_path: Beacon 1 file
        :param b2_path: Beacon 2 file
        :param b3_path: Beacon 3 file
        :param p_path: Diver file
        :return: Tab with format | timestamp | T° | Pression | coordonnée plongeur | profondeur (liée à la pression) |
        """
        b1_timestamps = []
        b1_lats = []
        b1_longs = []
        b2_timestamps = []
        b2_lats = []
        b2_longs = []
        b3_timestamps = []
        b3_lats = []
        b3_longs = []
        p_timestamps = []
        p_temperatures = []
        p_pressures = []
        p_dists_with_b1 = []
        p_dists_with_b2 = []
        p_dists_with_b3 = []

        # Parse b1.csv
        with open(b1_path, 'r') as b1_data:
            row_reader = csv.reader(b1_data, delimiter=',', quotechar='|')
            for row in row_reader:
                line = []
                for data in row:
                    line.append(data)
                b1_timestamps.append(int(line[0]))
                b1_lats.append(float(line[1]))
                b1_longs.append(float(line[2]))

        # Parse b2.csv
        with open(b2_path, 'r') as b2_data:
            row_reader = csv.reader(b2_data, delimiter=',', quotechar='|')
            for row in row_reader:
                line = []
                for data in row:
                    line.append(data)
                b2_timestamps.append(int(line[0]))
                b2_lats.append(float(line[1]))
                b2_longs.append(float(line[2]))

        # Parse b3.csv
        with open(b3_path, 'r') as b3_data:
            row_reader = csv.reader(b3_data, delimiter=',', quotechar='|')
            for row in row_reader:
                line = []
                for data in row:
                    line.append(data)
                b3_timestamps.append(int(line[0]))
                b3_lats.append(float(line[1]))
                b3_longs.append(float(line[2]))

        # Parse p.csv
        with open(p_path, 'r') as p_data:
            row_reader = csv.reader(p_data, delimiter=',', quotechar='|')
            for row in row_reader:
                line = []
                for data in row:
                    line.append(data)
                p_timestamps.append(int(line[0]))
                p_temperatures.append(float(line[1]))
                p_pressures.append(float(line[2]))
                p_dists_with_b1.append(float(line[3]))
                p_dists_with_b2.append(float(line[4]))
                p_dists_with_b3.append(float(line[5]))

        # Build final tab
        # | timestamp | T° | Pression | coordonnée plongeur | profondeur (liée à la pression) |
        rich_tab = []
        for i in range(len(p_timestamps)):
            b1_index = Aggregator.find_minimum_gap_index(p_timestamps[i], b1_timestamps)
            b2_index = Aggregator.find_minimum_gap_index(p_timestamps[i], b2_timestamps)
            b3_index = Aggregator.find_minimum_gap_index(p_timestamps[i], b3_timestamps)
            point_depth = Triangulation.get_depth_from_pressure(pressure=p_pressures[i])
            diver_gps = Triangulation.triangulate(
                                 b1_lat=b1_lats[b1_index],
                                 b1_long=b1_longs[b1_index],
                                 b2_lat=b2_lats[b2_index],
                                 b2_long=b2_longs[b2_index],
                                 b3_lat=b3_lats[b3_index],
                                 b3_long=b3_longs[b3_index],
                                 horizontal_dist1=Triangulation.get_horizontal_dist_from_diag_and_depth(
                                     diagonal_dist=p_dists_with_b1[i],
                                     depth=point_depth),
                                 horizontal_dist2=Triangulation.get_horizontal_dist_from_diag_and_depth(
                                     diagonal_dist=p_dists_with_b2[i],
                                     depth=point_depth),
                                 horizontal_dist3=Triangulation.get_horizontal_dist_from_diag_and_depth(
                                     diagonal_dist=p_dists_with_b3[i],
                                     depth=point_depth))
            rich_tab.append([p_timestamps[i],
                             p_temperatures[i],
                             p_pressures[i],
                             diver_gps[0],
                             diver_gps[1],
                             point_depth])

        print('Final tab :')
        for row in rich_tab:
            print(row)

        return rich_tab


if __name__ == '__main__':
    Aggregator().aggregate('./b1.csv', './b2.csv', './b3.csv', './p.csv')
