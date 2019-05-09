#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:37:40 2019

@author: jonasg
"""

import glob, os
import numpy as np
import pyaerocom as pya
import xarray as xarr

def check_file_okay(file):
    issues = []
    OK = True
    try:
        ds = xarr.open_dataset(file)
    except ValueError as e:
        OK = False
        if 'month' in repr(e):
            issues.append('Invalid calendar. Error: {}'.format(repr(e)))
            ds = xarr.open_dataset(file, decode_times=False)
            ds.time.attrs['calendar'] = 'standard'
        else:
            raise
    if not ds.lev.standard_name == 'atmosphere_hybrid_sigma_pressure_coordinate':
        OK = False
        issues.append('Invalid standard name for lev coordinate: {}'.format(ds.lev.standard_name))
        ds.lev.attrs['standard_name'] = 'atmosphere_hybrid_sigma_pressure_coordinate'
    
    if ds.lev.data[0] == ds.lev.data[1]:
        OK = False
        issues.append('Level values not strictly monotonic')
        lev_vals = np.arange(len(ds.lev.data))
        ds.lev.data = lev_vals
        
    if not OK:
        file = file.split('.nc')[0] + '_CORR.nc'
        ds.to_netcdf(file)
    return (file, OK, issues)



for file in glob.glob('*CORR.nc'):
    os.remove(file)


file = glob.glob('aerocom3_Oslo*monthly.nc')[0]
print(file)

(file, OK, issues) = check_file_okay(file)
    
d = pya.GriddedData(file, var_name='ec550aer')
print(d)    

if len(issues) > 0:
    print('------------------------------------------')
    print('Detected following issues:')
for issue in issues:
    print(issue)
    