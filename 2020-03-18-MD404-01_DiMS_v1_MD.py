# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:19:03 2020

@author: md546
"""

import pandas as pd
#for importing data
import numpy as np
import matplotlib.pyplot as plt
import os

exp={} #dictionary


directory = r'C:\Users\md546\Documents\2020-03-18_MD04-01_exported-spectra'
for filename in os.listdir(directory):

    if filename.endswith('.xy'):
        
        exp[filename]={}
        exp[filename]['sample_number'] = int(filename[-19:-17])
        
        if 'mouse' in filename:
            exp[filename]['sample_type'] = 'mouse'
            if exp[filename]['sample_number'] < 9:
                exp[filename]['sample_group'] = 'Control'
            
            if exp[filename]['sample_number'] >= 9 and exp[filename]['sample_number'] < 17:
                exp[filename]['sample_group'] = 'Vancomycin'

            if exp[filename]['sample_number'] >= 17 and exp[filename]['sample_number'] < 25:
                exp[filename]['sample_group'] = 'Neomycin'            

            if exp[filename]['sample_number'] >= 25 and exp[filename]['sample_number'] <= 32:
                exp[filename]['sample_group'] = 'AVNM'            
            
            
        elif 'high-qc' in filename:
            exp[filename]['sample_type'] = 'high-qc'
        
        elif 'low-qc' in filename:
            exp[filename]['sample_type'] = 'low-qc'
        

        filepath = os.path.join(directory,filename)


        data = pd.read_csv(filepath,sep = " ", header = None)
        data = np.array(data)

        mask = data[:,1]!= 0
    #asking a question. Does each element of the data not equal zero. Output would be True, True, False ... where false = zero. Indexed to show we are looking at column 1 only
        data = data[mask,:]        
    #index with boolean mask (array) removes all falses (zeroes)

        mask = data[:,1] >= 70 #change depending on lower acceptable limit for counts
        data = data[mask,:]


        lipids = pd.read_csv(r'C:\Users\md546\Documents\2020-03-18_MD04-01_exported-spectra\target-lipid-masses.csv', header = 0)


        masses = np.array(lipids['Mass'])
        lipid_names = lipids.Lipid

        intensity = []
        lipid = []
    
        for i_d in range(data.shape[0]):
        #in range 0 (by default range starts at 0) to 46146 (data.shape = (46146, 2) so data.shape[0] = 46146) in column 0 (assumes column is 0 as I haven't specified)   
        #print(i_d)
        #print(data[i_d,0])
        
            for i_m in range(masses.shape[0]):
                if data[i_d,0] >= masses[i_m]-0.005 and data[i_d,0] <= masses[i_m]+0.005:
               # print(data[i_d,1])
    
                    intensity.append(data[i_d,1])
                    lipid.append(lipid_names[i_m])
                    #print(lipid_names[i_m], masses[i_m], data[i_d,1])
                    #print(i_m)
                    
                
         
    
#        plt.bar(lipid, intensity)
#        plt.ylabel('Intensity')
#        plt.title(filename)
#        plt.show()