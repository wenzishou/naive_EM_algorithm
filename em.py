#-*-coding: utf-8 -*-
import os,sys
import numpy as np
import time
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from conf import *

def E_step(data_formatted, param_info, r_info):
    #do the expection step
    #x_data = data_info[:, 0].reshape(-1)
    #y_data = data_info[:, 1].reshape(-1)
    #data_formatted = np.stack([x_data, y_data], axis=-1)
    if DEBUG:
        class_index = 0
        data_pdf = multivariate_normal(param_info[class_index][0],
                    param_info[class_index][1]).pdf(data_formatted)
        print(4,data_pdf.shape)
        #plt.ion()
        for _i in xrange(0):
            fig = plt.figure(0)
            ax = Axes3D(fig)
            ax.scatter(x_data, y_data, data_pdf, c='r')
            plt.show()
            plt.close(0)
    data_pdf = np.empty(r_info.shape)
    for class_index in xrange(CLASS_NUM):
        _data_pdf = multivariate_normal(param_info[class_index][0], 
                    param_info[class_index][1]).pdf(data_formatted)
        data_pdf[:, class_index] = _data_pdf
        #set show data info empty
        param_info[class_index][2] = []
    #set r_info
    r_info = data_pdf/data_pdf.sum(1).reshape(-1,1)
    argmax_index = np.argmax(data_pdf, axis = 1)
    for _index in xrange(len(argmax_index)):
        param_info[argmax_index[_index]][2].append(data_formatted[_index])

    if DEBUG:
        for _i in xrange(1):
            fig = plt.figure(0)
            cols = ['r', 'g', 'b', 'k']
            for _j in xrange(CLASS_NUM):
                show_data = np.array(param_info[_j][2])
                plt.scatter(show_data[:, 0], show_data[:, 1], c=cols[_j])
            plt.show()
        
    return data_formatted, param_info, r_info


def M_step(data_formatted, param_info, r_info):
    #do the max step
    for class_index in xrange(CLASS_NUM):
        weight_mul = data_formatted * r_info[:, class_index].reshape(-1,1)
        mean = np.sum(weight_mul, 0)/np.sum(r_info[:, class_index])
        param_info[class_index][0] = mean
        
        var = np.zeros([DIM, DIM])
        for _data_index in xrange(data_formatted.shape[0]):
            diff = (data_formatted[_data_index, :] - mean).reshape(-1, 1)
            curr_var = r_info[_data_index, class_index] * np.matmul(diff, diff.T)
            var += curr_var
        var /= np.sum(r_info[:, class_index])
        param_info[class_index][1] = var

        if DEBUG:
            print('mean %d: ' % class_index,  mean)
            print('var  %d: ' % class_index,  var)
    return data_formatted, param_info, r_info
