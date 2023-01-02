

import numpy as np
import math
import matplotlib.pyplot as plt
import time
import pickle
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel, ConstantKernel
from sklearn.gaussian_process.kernels import Sum, Matern, Product, RBF
from pathlib import Path
data_folder = Path("C:/Users/mahom/Desktop/ISO_NE_Dataset_Final/Nestor")
filename = "iso_ne.pickle"
file_to_open = data_folder / filename
pickle_in=open(file_to_open,'rb')
iso_ne=pickle.load(pickle_in)

for location in range(8):

    # read CSV
    
    data2011=iso_ne[location][0]
    data2012=iso_ne[location][1]
    data2013=iso_ne[location][2]
    data2014=iso_ne[location][3]
    data2015=iso_ne[location][4]
    data2016=iso_ne[location][5]
    data2017=iso_ne[location][6]
    data2018=iso_ne[location][7]
    
    # LOADZONES========
# location 0: ME
# location 1: NH
# location 2: VT
# location 3: CT
# location 4: RI
# location 5: SEMASS
# location 6: WCMASS
# location 7: NEMASSBOST
      