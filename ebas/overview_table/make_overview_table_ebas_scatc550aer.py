#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 13:20:18 2019

@author: jonasg
"""

import numpy as np
import pyaerocom as pya
import pandas as pd
from collections import OrderedDict as od

def init_stat_result():
    d = od(totnum                   = 0,
           nans                     = 0,
           raw                      = 0,
           lev2                     = 0,
           lev3                     = 0,
           high_rh                  = 0,
           no_rhcol                 = 0,
           invalid                  = 0,
           invalid_notnan           = 0,
           nir                      = 0,
           nir_dry                  = 0,
           files                    = 0,
           files_nodata             = 0)
    return d

def run():
    #constraints = dict(LOG_READ_STATS=True, MERGE_META=False)
    constraints = dict()
    #constraints['station_names'] = ['Ale*', 'Upper*Buff*', 'Harwell', 'Melpi*']
    
    #constraints['station_names'] = ['Upper*Buff*', 'Melp*']
    
    RNG = [-10, 1000]
    
    r = pya.io.ReadEbas()
    r.opts.LOG_READ_STATS = True
    files = r.get_file_list(vars_to_retrieve=['scatc550aer'],
                            **constraints)
    
    VARS = ['scatc550aer', 'scatcrh', 'scatc550dryaer']
    
    results = {}
    for i, file in enumerate(files):
        if i%20 == 0:
            print('At file {} ({})'.format(i+1, len(files)))
        
        data = r.read_file(file, vars_to_retrieve=VARS)
        
        r.opts.REMOVE_INVALID_FLAGS = True
        data_noflag = r.read_file(file, vars_to_retrieve=VARS)
        r.opts.REMOVE_INVALID_FLAGS = False
        
        stat = data.station_name
        
        if not stat in results:
            results[stat] = init_stat_result()
        
        res = results[stat]
        
        if 'scatc550aer' in data:
            res['files'] += 1
            vals = data['scatc550aer']
            
            nir = np.logical_or(vals < RNG[0], vals > RNG[1])
            
            res['nir'] += nir.sum()
            
            totnum = len(vals)
            res['totnum'] += totnum
            
            nans = np.isnan(vals)
            nannum = nans.sum()
            
            res['nans'] += nannum
            res['raw'] += totnum - nannum
            
            # write flag column eval info
            res['invalid'] += data_noflag.var_info['scatc550aer']['num_flag_invalid']
            res['invalid_notnan'] += data_noflag.var_info['scatc550aer']['num_notnan_flag_invalid']
            
            if data['datalevel'] == '2':
                res['lev2'] += np.sum(~np.isnan(data_noflag['scatc550aer']))
            if not 'scatcrh' in data:
                res['no_rhcol'] += totnum
            else: # dry is available as well as RH
                dry = data_noflag['scatc550dryaer']
                res['high_rh'] += np.isnan(dry).sum() - np.isnan(vals).sum()
                
                nir_dry = np.logical_or(dry < RNG[0], dry > RNG[1])
                
                res['nir_dry'] += nir_dry.sum()
                
                dry[nir_dry] = np.nan
                
                notnan = ~np.isnan(dry)
                
                res['lev3'] += notnan.sum()
            
        
        
    print(results)
            
    header = ['station']
    header.extend(list(init_stat_result()))
    
    table = []
    
    for stat, values in results.items():
        _vals = [stat]
        _vals.extend(list(values.values()))
        table.append(_vals)
    
    df = pd.DataFrame(table, columns=header)
    df.to_csv('ebas_summary_table_scatc550aer.csv')

if __name__ == '__main__':
    run()
    
    
    



