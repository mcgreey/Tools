#!\Anaconda3\envs\py35 python

# -*- coding: utf-8 -*-
#!@Time   : 2019/2/19 14:03
#!@Author : python
#!@File   : .py
import os

scr_path = r'F:\DataTest\30cases_Pinnacle_luzong\30例-陆总Pinnacle'
scr_path_0 = r'F:\DataTest\30cases_Pinnacle_luzong\新的10例'
dst_path = r'F:\DataTest\30cases_Pinnacle_luzong'

for sub_file in os.listdir(scr_path_0):
    sub_path = os.path.join(scr_path_0, sub_file)
    for dirName_final, subDir_final, files_final in os.walk(sub_path):
        if subDir_final == []:
            f = open(os.path.join(dst_path, 'scr0.txt'), 'a')
            f.write(str(sub_file) + ' :  ' + str(len(files_final)))
            f.write('\n')
            f.close()
