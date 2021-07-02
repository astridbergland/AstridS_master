#!/usr/bin/env python
# coding: utf-8

# # <center>How to use the GFPy functions
# ![Logo.png](attachment:Logo.png)
# ### <center><font color='green'>This notebook contains small examples how to use the various functions of the GFPy-Package
#     
# #### <font color='red'>Note: Before using these functions, be sure to install the GFPy package from pip:
# `pip install GFPy`
# #### <font color='red'>To update, type:
# `pip install -U GFPy`

# ### <center><font color='blue'> GFPy.Ocean

# #### Read in CTD data from raw files

# In[1]:


import GFPy.Ocean as Oc
import matplotlib.pyplot as plt
import numpy as np

# Document Data location (absolute or relative to current location)
data_loc = 'C:/Users/astri/Downloads/ODENnew/'

# Read all station files in specified folder, and save result in a .npy file
CTD_all = Oc.read_CTD(data_loc,'Data',outpath='./')

# Read specific stations in the folder
#stations = range(500,505)
#CTD_part = Oc.read_CTD(data_loc,'test_cruise',stations=stations) 
#print(CTD_part.keys())


# #### Plot a CTD section

# In[ ]:


#define stations included in the CTD section
stations = range(401,410)

# plot the section, given the variable CTD_all from above
Oc.plot_CTD_section(CTD_all,stations,
                 cruise_name='test_cruise',section_name='TEST')

axx = plt.gcf().axes
axx[0].set_ylim([200,0])

# %%
## plot the section, given the path to the .npy file given above
#Oc.plot_CTD_section('./test_cruise_CTD.npy',stations,
#                 cruise_name='test_cruise',section_name='A')
# save the current figure
#plt.savefig('./test_image.pdf')

# plot a section of a single variable of your choice (for example Oxygen)
Oc.plot_CTD_single_section(CTD_all,stations,parameter='OX',
                           clabel='Oxygen [mg/l]',cmap='cmo.oxy')


# #### Plot a CTD profile

# In[ ]:


# define the station for which to plot a profile
station = 402

# plot a single profile
Oc.plot_CTD_station(CTD_all, station)
plt.savefig('./test_profile.pdf')

# plot several single profiles in one plot with subplots
plt.figure()
plt.subplot(121)
Oc.plot_CTD_station(CTD_all, station,add = True)
plt.title('Station 402')
plt.subplot(122)
Oc.plot_CTD_station(CTD_all, station+1,add = True)
plt.title('Station 403')
# if you want to manipulate the figure afterwards, you have to get the
# axes using plt.gcf().axes. There are 4 axes in this example, 2 for each
# subplot, because we have two x-axes in each subplot. To, i.e. change the
# temperaure range and xlabel in the first sublplot, do:
axx = plt.gcf().axes
axx[0].set_xlim(0,15)
axx[0].set_xlabel('Liberal temperature [˚C]');


# #### Plot a map of CTD stations

# In[ ]:


# define the stations to plot on the map
stations = range(401,410)
 
plt.figure()
Oc.plot_CTD_map(CTD_all,stations)
plt.savefig('./test_map.pdf')
plt.figure()
# Plot all stations in a map
#Oc.plot_CTD_map(CTD_all)  


# #### Plot a TS diagram with CTD data

# In[ ]:


plt.figure()
Oc.plot_CTD_ts(CTD_all,[401,402],pref=0)

# you can also create an empty TS-Diagram, and plot your data in it:
plt.figure()
Oc.create_empty_ts((-2,35),(0,40),0)

# Calculate freshwater content
print(Oc.calc_freshwater_content(CTD_all[401]['S'],CTD_all[401]['z']))


# #### Read a mini CTD file, and plot some quick plots

# In[ ]:


file = 'Example_data/Ocean_data/mini_CTD/F2031323_4.TOB'
mCTD = Oc.read_mini_CTD(file)
print(mCTD.keys())

# if you want, you can also convert to DataFrame
import pandas
df_mCTD = pandas.DataFrame(mCTD)
display(df_mCTD)

# plot a quick profile,just for a quick look, make the nice plot yourself :)
Oc.plot_CTD_station({0:mCTD},0)


# #### Read ADCP data

# In[ ]:


import GFPy.Ocean as Oc
import matplotlib.pyplot as plt
from matplotlib.dates import num2date
import numpy as np

ADCP_file = 'Example_data/Ocean_data/ADCP/os150nb.nc'
ADCP = Oc.read_ADCP(ADCP_file)
print(ADCP.keys())
time = num2date(ADCP['time'])

plt.figure(figsize=(13,6))
plt.contourf(time,ADCP['depth'][0,:],ADCP['u'].transpose(),levels=np.linspace(-0.4,0.4,100))
plt.gca().invert_yaxis()
plt.colorbar()


# #### Read a mooring .mat file

# In[ ]:


mooring_file = 'Example_data/Ocean_data/Mooring/MF_sill.mat'

mooring = Oc.read_mooring_from_mat(mooring_file)
print(mooring.keys())
print(mooring['instrumentation'])
RDCP = mooring['ins'][1]
print(RDCP.keys())
RDCP_u = np.asarray(RDCP['u']) # will fix so that you don't have to convert to array...
RDCP_time = Oc.mat2py_time(np.asarray(RDCP['time']))
print(RDCP['hab']) # height above instrument!!!

plt.figure(figsize=(20,3))
plt.plot(RDCP_time,RDCP_u[:,5])


# #### Read and plot GPS drifter data

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import cartopy.crs as ccrs
import matplotlib.ticker as mticker
from datetime import datetime, timedelta

# =============================================================================
# global settings -
# =============================================================================
# define the time of deployment and recovery
t_deploy =   '2020-03-03 18:10:00'
t_recovery = '2020-03-03 19:00:00'
# Define an averaging interval
avg_interval = '2min'
# set the offset (half the average time interval)
offset = '60s'

# Define the file location
path = 'Example_data/Ocean_data/Drifters/Unitracker-1 2020-03-02 00_00_00-2020-03-06 00_00_00.csv'

# =============================================================================
# Read the Drifter data
# =============================================================================
# Read the drifter data
drifter_dat = Oc.read_drifter(path)

# Estimate the instantaneous speed and heading from latitude and longitude
speed, heading = Oc.cal_dist_dir_on_sphere(drifter_dat.lat,drifter_dat.lng)
# Estimate the time average of speed and heading
speed_avg, heading_avg = Oc.cal_dist_dir_on_sphere(drifter_dat.lat.resample(avg_interval, loffset = offset).mean(),
                                                  drifter_dat.lng.resample(avg_interval, loffset = offset).mean())

# Set heading to nan, in case speed is 0 m/s
heading[speed<=0]         = np.nan
heading_avg[speed_avg<=0] = np.nan

# =============================================================================
# Plot the Drifter data
# =============================================================================

# Plot the Latitude and Longitude
fig,ax = plt.subplots(figsize = [8,5], nrows=2, sharex=True)
ax[0].plot(drifter_dat.lat[t_deploy:t_recovery], label = 'instantaneous')
ax[0].plot(drifter_dat.lat.resample(avg_interval,loffset=offset).mean()[t_deploy:t_recovery],
           label=avg_interval+' average')
ax[0].legend()
ax[0].set_ylabel('Latitude ($^{\circ}N$)')
ax[1].plot(drifter_dat.lng[t_deploy:t_recovery], label = 'instantaneous')
ax[1].plot(drifter_dat.lng.resample(avg_interval,loffset = offset).mean()[t_deploy:t_recovery])
ax[1].set_ylabel('Longitude ($^{\circ}E$)')
ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax[1].set_xlabel('time (HH:MM)')


fig,ax = plt.subplots(figsize = [8,5], nrows=2, sharex=True)
ax[0].plot(drifter_dat.speed[t_deploy:t_recovery], label = 'drifter measured speed')
ax[0].plot(speed[t_deploy:t_recovery], label = 'instantaneous retrieved speed')
ax[0].plot(speed_avg[t_deploy:t_recovery], label = 'averaged retrieved speed')
ax[0].set_ylabel('Speed (m/s)')
ax[0].legend()
ax[1].plot(drifter_dat.angle[t_deploy:t_recovery],'o',markersize=2, label = 'drifter measured heading')

ax[1].plot(heading[t_deploy:t_recovery],'o',markersize=2, label = 'instantaneous retrieved heading')
ax[1].plot(heading_avg[t_deploy:t_recovery],'o',markersize=5, label = 'averaged retrieved heading')
ax[1].set_ylabel('Heading ($^{\circ}$)')
ax[1].set_xlim([t_deploy,t_recovery])
ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax[1].set_xlabel('time (HH:MM)')

# =============================================================================
# Plot the map - may need to adjust the extent or projection
# =============================================================================
extent    = [5,5.4,60.7,60.9]
disp_proj = ccrs.Mercator()
data_proj = ccrs.PlateCarree()
fig = plt.figure(figsize=(9,13))
ax = plt.axes(projection=disp_proj)
ax.plot(drifter_dat.lng[t_deploy:t_recovery],
        drifter_dat.lat[t_deploy:t_recovery],
        transform=data_proj)
ax.coastlines('10m')
ax.set_extent(extent)
gl = ax.gridlines(draw_labels=True)


gl.xlabel_style = {'size': 16, 'color': 'k'}
gl.ylabel_style = {'size': 16, 'color': 'k'}
plt.xlabel('Longitude [°E]')
ax.set_ylabel('Latitude [°N]')


# ### <center><font color='blue'> GFPy.Met_data

# #### Read an AWS file 

# In[ ]:


from GFPy.Met_data import *
import glob

# Document Data location (absolute or relative to current location)
data_loc = 'Example_data/Met_data/AWS/'

# -----------------
# Read ascii format
#------------------ 
data_format ='*.dat'

# Get all files of sought format
filenames = sorted(glob.glob(data_loc+data_format))

# Read the first ascii file
AWS_dat = read_dat_AWS(filenames[0])

plot_AWS(filenames[0])
# ------------------
# read netcdf format
# ------------------

data_format ='*.nc'

# Get all files of sought format
filenames = sorted(glob.glob(data_loc+data_format))

# Read the first netcdf file
AWS_nc = read_netcdf_AWS(filenames[0])


# ---------------------------
# read ascii or netcdf format
# ---------------------------

AWS, variables = read_single_AWS(filenames[0])


# #### Read the dataset recorded by the ship log of Kristine Bonnevie

# In[ ]:


# Document Data location (absolute or relative to current location)
data_loc = 'Example_data/Met_data/Ship_log/'

# define the data format
data_format ='*.csv'

# Get all files of sought format
filenames = sorted(glob.glob(data_loc+data_format))

# read the file
ship_log = read_ship_log(filenames)


# In[ ]:




