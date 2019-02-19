#!\Anaconda3\envs\py35 python

# -*- coding: utf-8 -*-
#!@Time   : 2019/2/14 11:08
#!@Author : python
#!@File   : .py

'''
不同模型批处理后的dice对比
'''

import csv
import os
import sys

path_of_csv = r'F:\Workspace\PycharmProjects\compare'

csv_0 = os.path.join(path_of_csv, 'scr.csv')
csv_1 = os.path.join(path_of_csv, 'dst0.csv')
csv_2 = os.path.join(path_of_csv, 'dst1.csv')
csv_3 = os.path.join(path_of_csv, 'dst2.csv')

write_csv_path = os.path.join(path_of_csv, 'compare.csv')

out = open(write_csv_path,'a', newline='')
csv_write = csv.writer(out,dialect='excel')

# 以024为标准来储存
num_line = 0
csv_1_file = csv.reader(open(csv_1))
for each_line_1 in csv_1_file:
    if 0 == num_line:
        each_line_1.extend(['dice1', 'hd1', 'rvd1', 'dice2', 'hd2', 'rvd2', 'dice3', 'hd3', 'rvd3'])
        csv_write.writerow(each_line_1)
    else:
        each_line_2_has = 0
        csv_2_file = csv.reader(open(csv_2))
        for each_line in csv_2_file:
            if (each_line[2] == each_line_1[2]) and (each_line[6] == each_line_1[6]):
                each_line_1.extend(each_line[-3:])
                each_line_2_has = 1
                break
        if 0 == each_line_2_has:
            each_line_1.extend(['', '', ''])

        each_line_0_has = 0
        csv_0_file = csv.reader(open(csv_0))
        for each_line in csv_0_file:
            if (each_line[2] == each_line_1[2]) and (each_line[6] == each_line_1[6]):
                each_line_1.extend(each_line[-3:])
                each_line_0_has = 1
                break
        if 0 == each_line_0_has:
            each_line_1.extend(['', '', ''])

        each_line_3_has = 0
        csv_3_file = csv.reader(open(csv_3))
        for each_line in csv_3_file:
            if (each_line[2] == each_line_1[2]) and (each_line[6] == each_line_1[6]):
                each_line_1.extend(each_line[-3:])
                each_line_3_has = 1
                break
        if 0 == each_line_3_has:
            each_line_1.extend(['', '', ''])

        csv_write.writerow(each_line_1)

    num_line += 1

out.close()
print ('write over')




