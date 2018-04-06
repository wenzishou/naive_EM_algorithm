#-*-coding: utf-8 -*-
import os,sys
import matplotlib.pyplot as plt
import numpy as np
from conf import *
from init import *
from em import *
#CLASS_NUM = 2
#data_conf = [
#                [
#                    [0, 0],
#                    [[1, 0], [0, 5]],
#                    900
#                ], 
#                [
#                    [8, 8],
#                    [[3, -2], [-2, 5]],
#                    900
#                ]
#            ]
#DEBUG = True

def get_train_data():
    x = []
    y = []
    for i in xrange(CLASS_NUM):
        _x, _y = np.random.multivariate_normal(data_conf[i][0], 
                                                data_conf[i][1],
                                                data_conf[i][2]).T
        x += _x.tolist()
        y += _y.tolist()
    return x, y

def plot_dots(x, y):
    plt.plot(x,y,'x')
    plt.axis('equal')
    plt.show()


x, y = get_train_data()
data_info, r_info = init_data(x,y)
param_info = init_parameter()
for _i in xrange(8):
    data_info, param_info, r_info = E_step(data_info, param_info, r_info)
    data_info, param_info, r_info = M_step(data_info, param_info, r_info)

#print(x)
#plot_dots(x,y)
