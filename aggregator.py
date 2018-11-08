class Aggregator(object):
    @staticmethod
    def aggregate(b1_path, b2_path, b3_path, p_path):
        print(b1_path)


if __name__ == '__main__':
    Aggregator().aggregate('./b1.csv', './b2.csv', './b3.csv', './p.csv')
