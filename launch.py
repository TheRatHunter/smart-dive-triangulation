import csv

from aggregator import Aggregator


class Launch(object):
    @staticmethod
    def go(b1, b2, b3, p, output):
        """
        Launches the triangulation for the given input file and writes result in new CSV
        :return:
        """
        tab = Aggregator().aggregate(b1, b2, b3, p)

        with open(output, 'w') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in tab:
                csv_writer.writerow(row)

        return 0


if __name__ == '__main__':
    Launch.go('./b1.csv', './b2.csv', './b3.csv', './p.csv', 'output.csv')
