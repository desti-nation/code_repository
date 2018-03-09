#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import shutil
import os

folder_name = 'Log'
shutil.rmtree(folder_name)
os.mkdir(folder_name)