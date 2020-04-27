# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 03:41:05 2020

@author: ASUS
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import function as f

####################### Parsing From HTML ####################################################
website1 = ['https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Administrasi_Jakarta_Barat',
           'https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Administrasi_Jakarta_Utara',
           'https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Administrasi_Jakarta_Timur',
           'https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Administrasi_Jakarta_Selatan']

website2 = ['https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Administrasi_Jakarta_Pusat']

jaka_SubDistrict = []


jaka_SubDistrict = f.parseHTML(website1,0,jaka_SubDistrict)
jaka_SubDistrict = f.parseHTML(website2,1,jaka_SubDistrict)

########################## Flatten The List ###################################################

listSubDistrict = f.flattenTheList(jaka_SubDistrict)

########################## Count Number of Cases in Span of 2013-2016 for each Sub-District #################################
features = ['subDistrict','no. of cases','no. of People Affected','no. of People Forced to Relocate','Days of Flood Recovery']
df = pd.DataFrame(0,index= np.arange(len(listSubDistrict)), columns=features)
df['subDistrict'] = listSubDistrict

numList = np.linspace(1,34,num=34).astype(int)

dataFrame = f.floodOccurence(numList,df)
    
print(dataFrame)
