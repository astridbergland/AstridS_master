
# Reading in data from Oden 05

from netCDF4 import Dataset
from cartopy import crs
import matplotlib.pyplot as plt
import numpy as np
import cartopy.feature as cfeatures

# 1 
import os
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('C:/Users/astri/Downloads/ODENnew/Data') if isfile(join('C:/Users/astri/Downloads/ODENnew/Data', f))]
                                

path='C:/Users/astri/Downloads/ODENnew/Data'
#open('77DN200508_00001_00002_ctd.nc')

os.chdir(path)
data = Dataset(onlyfiles[0])

# data.variables.keys() - shows all the variables in the file 

#print['temperature']


temp1 = data['temperature'][:]

posT1 = np.extract(temp1 > 0, temp1)

meanT = np.mean(posT1)

plt.plot(temp1, -np.arange(len(temp1)))




