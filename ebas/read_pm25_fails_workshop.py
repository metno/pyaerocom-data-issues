#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:37:11 2019

@author: jonasg
"""

import pyaerocom as pya
import matplotlib.pyplot as plt
plt.close('all')

r = pya.io.ReadGridded('EMEP_rv4_2599_Rep2013emistrend')


emep_data = r.read_var('od550aer', start=2010)


print(emep_data)

emep_data.quickplot_map(0)

r = pya.io.ReadUngridded()
obs = r.read('AeronetSunV3Lev2.daily', ['od550aer', 'ang4487aer'])
print(obs)

coldata = pya.colocation.colocate_gridded_ungridded(emep_data,
                                                    obs,
                                                    var_name='od550aer',
                                                    harmonise_units=False)                               

coldata.plot_scatter()
