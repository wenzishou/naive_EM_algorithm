#-*-coding: utf-8 -*-
import os,sys
import numpy as np
import random
from conf import *
def init_parameter():
    param = [] 
    for _c in xrange(CLASS_NUM):
        param.append([])
        #[mean, convar, [data_x, data_y]]
        _p_mean  = []
        for _d in xrange(DIM):
            _p_mean.append(random.randint(0,30)*random.random())
        _p_convar = np.identity(DIM)
        param[_c].append(_p_mean)
        param[_c].append(_p_convar)
        param[_c].append([[], []])
    if DEBUG:
        print(param)
    return param

def init_data(x, y):
    assert len(x)==len(y)
    np_data = np.zeros((len(x), DIM))
    r_info = np.ones((len(x), CLASS_NUM)) * (1.0/CLASS_NUM) 
    for _i in xrange(len(x)):
        np_data[_i, :] = [x[_i], y[_i]]
    if DEBUG:
        print(np_data, r_info)


    #x_data = np_data[:, 0].reshape(-1)
    #y_data = np_data[:, 1].reshape(-1)
    data_formatted = np.stack([x, y], axis=-1)
    return data_formatted, r_info 


