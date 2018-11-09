# -*- coding: utf-8 -*-
import numpy as np
import cv2

from triangulation import Triangulation


class Draw(object):
    @staticmethod
    def draw_intersection_calculation(la1, lo1, r1, la2, lo2, r2, la3, lo3, r3, px, py):
        # return self.circle_intersection_sympy(circle1,circle2)
        x1, y1 = int((la1 - 40) * 100), int(lo1 * 100)
        x2, y2 = int((la2 - 40) * 100), int(lo2 * 100)
        x3, y3 = int((la3 - 40) * 100), int(lo3 * 100)
        px, py = int((px - 40) * 100), int(py * 100)

        # Create a black image
        img = np.zeros((600, 600, 3), np.uint8)

        # Bricolage temporaire pour faire coincider les distances en km avec les coordonées GPS (conflit plan/spérique)
        r1 = int(r1 / 1000)
        r2 = int(r2 / 800)
        r3 = int(r3 / 800)-10

        print('x b1 : ' + str(x1))
        print('y b1 : ' + str(y1))
        print('H_dist b1 : ' + str(r1))
        print('x b2 : ' + str(x2))
        print('y b2 : ' + str(y2))
        print('H_dist b2 : ' + str(r2))
        print('x b3 : ' + str(x3))
        print('y b3 : ' + str(y3))
        print('H_dist b3 : ' + str(r3))
        print('x diver : ' + str(px))
        print('y diver : ' + str(py))

        # Circles : (0,0,r1), (dx2, dy2, r2), (dx3, dy3, r3)
        cv2.circle(img, (x1, y1), 1, (255, 0, 0), 2)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.circle(img, (x2, y2), 1, (255, 0, 0), 2)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.circle(img, (x3, y3), 1, (255, 0, 0), 2)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.circle(img, (x1, y1), r1, (255, 0, 0), 2)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.circle(img, (x2, y2), r2, (255, 0, 0), 2)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.circle(img, (x3, y3), r3, (255, 0, 0), 2)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.circle(img, (px, py), 1, (0, 0, 255), 2)

        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        exit(0)

    @staticmethod
    def draw_example():
        Draw.draw_intersection_calculation(
            42.495994, 3.442279,
            Triangulation.distance_between_coordinates_in_m(42.495994, 3.442279, 43.10572, 3.949412),
            43.181071, 5.21284, Triangulation.distance_between_coordinates_in_m(43.181071, 5.21284, 43.10572, 3.949412),
            43.355465, 3.828563,
            Triangulation.distance_between_coordinates_in_m(43.355465, 3.828563, 43.10572, 3.949412),
            43.10572, 3.949412)


if __name__ == '__main__':
    Draw.draw_example()
