#-*-coding: utf-8 -*-
CLASS_NUM = 4
DIM = 2
data_conf = [
                [
                    [0, 20],    #mean
                    [[3, 1], [1, 8]], #var
                    100
                ], 
                [
                    [0, 0],    #mean
                    [[8, -1], [-1, 3]], #var
                    100
                ], 
                [
                    [20, 20],
                    [[3, -2], [-2, 5]],
                    100
                ],
                [
                    [20, 0],
                    [[9, 7], [7, 6]],
                    100
                ],
            ]
DEBUG = True

assert CLASS_NUM == len(data_conf)
