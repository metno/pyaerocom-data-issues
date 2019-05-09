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

READ_ONLY_CORRECTED = True

CORR_FILE = 'aerocom3_OsloCTM3v1.01-met2010_AP3-CTRL_ec550aer_ModelLevel_2010_monthly_CALENDAR_CORR_LEV_CORR.nc'
if READ_ONLY_CORRECTED:
    d = pya.GriddedData(CORR_FILE, var_name='ec550aer')
    print(d)
else:

    for file in glob.glob('*CALENDAR_CORR.nc'):
        os.remove(file)
    
    CALENDAR_OK = False
    files = glob.glob('aerocom*monthly.nc')
    print(files)
    
    def check_lev_okay(file):
        
        d = pya.GriddedData(file,var_name='ec550aer')
        if 'lev' in d.dimcoord_names:
            return (True, file)
        
        ds_lev_wrong = xarr.open_dataset(file)
        
        lev = np.arange(len(ds_lev_wrong.lev.data))
        ds_lev_wrong.lev.data = lev
        file_corr = file.split('.nc')[0] + '_LEV_CORR.nc'
        ds_lev_wrong.to_netcdf(file_corr)
        return (False, file_corr)
    
    for file in files:
        try:
            ds = xarr.open_dataset(file)
            CALENDAR_OK = True
        except ValueError as e:
            if 'month' in repr(e):
                ds_wrong = xarr.open_dataset(file, decode_times=False)
                ds_wrong.time.attrs['calendar'] = 'standard'
                ds_wrong.to_netcdf(file.split('.nc')[0] + '_CALENDAR_CORR.nc')
        
    if CALENDAR_OK:
        file = glob.glob('aerocom*monthly.nc')[0]
    else:
        file = glob.glob('aerocom*monthly_CALENDAR_CORR.nc')[0]
        
    (LEV_OK, file) = check_lev_okay(file)
        
    d = pya.GriddedData(file, var_name='ec550aer')
    print(d)
