#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@program: makeh5.py

@task: Create dummy datasets
"""

import h5py
import numpy as np

A = np.array([1, 2])
B = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])
c = 42
d = 1.23

with h5py.File('./ex_dataset.h5', 'w') as hf:
    gf1 = hf.create_group('arrays')
    gf1.create_dataset('A', data=A)
    gf1.create_dataset('B', data=B)
    gf2 = hf.create_group('scalars')
    gf2.create_dataset('c', data=c)
    gf2.create_dataset('d', data=d)
