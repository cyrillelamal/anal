"""
Лабораторная работа 4
"""
from varseries import ContinuousVS, DiscreteVS


def task1():
    values = [
        103.4, 115.2, 127, 131, 114, 114.1, 119.6, 125.5, 116.9, 118.1, 123.5,
        113.5, 112.3, 123, 125, 129.9, 99.2, 111, 122, 134, 107.1, 117, 117.5,
        118.5, 124, 127.8, 108, 119.5, 123, 126.1, 100.1, 120.2, 122.2, 124.8,
        109, 113, 122.5, 135.8, 97, 121.1, 123.8, 123.2, 105.9, 122.6, 123.9,
        129.5, 107, 123.5, 128.5, 117.5, 121.5, 127.5, 113.2, 120.6, 126.5,
        116, 122.9, 138, 115, 123.1, 140, 94.1, 110, 112.9, 132, 102, 109.5,
        118.3, 135, 112.5, 115.5, 120, 126, 130, 105.5, 108.2, 119.2, 131.4,
        106.5, 112, 120.8, 121.9, 134.2, 115.7, 118.9, 124.5, 111.5, 121, 133,
        116.5, 119, 129, 106.1, 119.8, 133.6, 114.5, 118, 128
    ]
    v = ContinuousVS(values)
    v.draw_cumulate()\
        .draw_empiric_dist_func()\
        .draw_hist()


def task2():
    values = {
        1: 2, 2: 3, 3: 6, 4: 8, 5: 22, 6: 9
    }
    v = DiscreteVS(values)
    v.draw_polygon()\
        .draw_cumulate()\
        .draw_empiric_dist_func()


def task3():
    values = [
            1.14285583, 0.21398374, 1.25641624, 0.67329946, 1.21496283, 0.99101069,
            1.39925669, 0.61109646, 0.85890088, 0.78632108, 0.9738463, 1.3846759,
            0.49488379, 1.0979642, 1.02453946, 1.06382694, 0.78161594, 1.20567321,
            1.38270281, 0.88719158, 0.75776634, 1.16915277, 1.23004829, 0.71265086,
            1.02887585, 0.82302015, 1.24597822, 1.45686546, 0.91103144, 0.77406981,
            1.09453619, 0.79865011, 0.88126134, 1.10711803, 1.00136848, 0.92217984,
            1.24560914, 0.78720264, 0.954333, 0.99578226, 0.81526016, 0.77680747,
            1.23527671, 1.73649997, 1.25015887, 0.71522997, 0.76771727, 1.0515177,
            0.53930926, 1.32623785, 0.59025817, 0.84943463, 1.0391314, 0.87918459,
            0.60738125, 1.18346139, 0.83580503, 0.95130778, 1.40929416, 0.60987357,
            1.39038211, 1.06430415, 0.6048676, 1.36443751, 0.98420392, 1.31749231,
            1.10304182, 0.25832193, 0.31529515, 0.43993342, 0.90625883, 1.49160615,
            0.66502074, 0.3382135, 0.5468639, 0.66566206, 1.22896107, 1.32777678,
            1.21582933, 1.00298477, 0.8827651, 1.07884146, 1.45221163, 0.63185447,
            0.9416058, 1.07515286, 0.97412237, 1.51354811, 1.12753343, 0.72361969,
            0.50409524, 0.68639066, 0.82355366, 0.69646316, 0.65239474, 0.72192621,
            1.05932474, 1.25494818, 1.87487639, 0.74979352
    ]
    v = ContinuousVS(values)
    v.draw_cumulate()\
        .draw_empiric_dist_func()\
        .draw_hist()


def task4():
    values = [
        4, 4, 3, 3, 2, 5, 2, 3, 3, 4,
        3, 4, 4, 2, 5, 2, 3, 3, 4, 4,
        3, 3, 4, 4, 2, 5, 5, 2, 3, 3
    ]
    v = ContinuousVS(values)
    v.draw_cumulate()\
        .draw_empiric_dist_func()\
        .draw_hist()


def task5():
    values = [
        18, 10, 17, 13, 15, 15, 14, 17, 20, 19,
        15, 15, 14, 13, 16, 16, 12, 11, 13, 14,
        19, 20, 15, 16, 15, 16, 14, 16, 13, 12
    ]
    v = ContinuousVS(values)
    v.draw_cumulate()\
        .draw_empiric_dist_func()\
        .draw_hist()
