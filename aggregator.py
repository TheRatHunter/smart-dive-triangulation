import csv


class Aggregator(object):
    @staticmethod
    def aggregate(b1_path, b2_path, b3_path, p_path):
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
                b1_timestamps.append(line[0])
                b1_lats.append(line[1])
                b1_longs.append(line[2])

        # Parse b2.csv
        with open(b2_path, 'r') as b2_data:
            row_reader = csv.reader(b2_data, delimiter=',', quotechar='|')
            for row in row_reader:
                line = []
                for data in row:
                    line.append(data)
                b2_timestamps.append(line[0])
                b2_lats.append(line[1])
                b2_longs.append(line[2])

        # Parse b3.csv
        with open(b3_path, 'r') as b3_data:
            row_reader = csv.reader(b3_data, delimiter=',', quotechar='|')
            for row in row_reader:
                line = []
                for data in row:
                    line.append(data)
                b3_timestamps.append(line[0])
                b3_lats.append(line[1])
                b3_longs.append(line[2])

        # Parse p.csv
        with open(p_path, 'r') as p_data:
            row_reader = csv.reader(p_data, delimiter=',', quotechar='|')
            for row in row_reader:
                line = []
                for data in row:
                    line.append(data)
                p_timestamps.append(line[0])
                p_temperatures.append(line[1])
                p_pressures.append(line[2])
                p_dists_with_b1.append(line[3])
                p_dists_with_b2.append(line[4])
                p_dists_with_b3.append(line[5])

        # Log results
        print('CSV reading outputs :')
        print(b1_timestamps)
        print(b1_lats)
        print(b1_longs)
        print(b2_timestamps)
        print(b2_lats)
        print(b2_longs)
        print(b3_timestamps)
        print(b3_lats)
        print(b3_longs)
        print(p_timestamps)
        print(p_temperatures)
        print(p_pressures)
        print(p_dists_with_b1)
        print(p_dists_with_b2)
        print(p_dists_with_b3)

        # Build final tab


if __name__ == '__main__':
    Aggregator().aggregate('./b1.csv', './b2.csv', './b3.csv', './p.csv')
