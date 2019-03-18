#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:37:11 2019

@author: jonasg
"""

import pyaerocom as pya

r = pya.io.ReadEbas()
#d = r.read('sconcso4', station_names=['B*'])

emep_r = pya.io.ReadGridded('EMEP_rv4_2599_Rep2013emistrend')#.read_var('sconcso4')

print(emep_r)
# =============================================================================
# coldata = pya.colocation.colocate_gridded_ungridded(emep_data,
#                                                     d,
#                                                     'sconcso4',
#                                                     harmonise_units=False)                               
# =============================================================================
