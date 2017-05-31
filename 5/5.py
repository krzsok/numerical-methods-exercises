
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Problem V

import numpy as np
import time


n = 790
Matricescount = 10 

G = [np.matrix(np.sqrt(1/n) * np.random.randn(n, n)) for i in range(Matricescount)] 

time1 = time.time()
SV = [np.linalg.svd(g, compute_uv = False) for g in G]
time2 = time.time()

print(time2-time1)

K = [sv[0] / sv[n-1] for sv in SV]
print("mean logarithm:")
print(np.mean(np.log(K)))
print(n)