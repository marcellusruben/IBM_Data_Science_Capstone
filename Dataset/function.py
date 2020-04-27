# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 05:36:30 2020

@author: ASUS
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

def parseHTML(website, content, myList):
    
    for i in range (len(website)):
        
        wikiPage = website[i]
        request = requests.get(wikiPage)
        soup = BeautifulSoup(request.content,'lxml')

        table = soup.find_all('table')[content]
        df = pd.read_html(str(table))

        dataFrame = df[0]
        
        myList.append(dataFrame['Kecamatan'].iloc[:-1].values.tolist())
    
    return myList

def flattenTheList(myList):
    
    flatList = []
    for sublist in myList:
        for item in sublist:
            flatList.append(item)
            
    return list(set(flatList))

def floodOccurence(numList, dataFrame):
    
    for i in range (len(numList)):
    
        data = pd.read_csv('Data-Kejadian-Banjir-'+str(numList[i])+'.csv')

        groupData =data.groupby('kecamatan', sort=False)\
        .agg({'kelurahan': 'size','jumlah_jiwa': 'sum', 'jumlah_pengungsi': 'sum', 'lama_genangan': 'sum'})
        groupData =groupData.reset_index()

        for j in range (len(groupData)): 
            dataFrame.loc[dataFrame['subDistrict']== groupData['kecamatan'][j], 'no. of cases'] += groupData['kelurahan'][j]
            dataFrame.loc[dataFrame['subDistrict']== groupData['kecamatan'][j], 'no. of People Affected'] += groupData['jumlah_jiwa'][j]
            dataFrame.loc[dataFrame['subDistrict']== groupData['kecamatan'][j], 'no. of People Forced to Relocate'] += groupData['jumlah_pengungsi'][j]
            dataFrame.loc[dataFrame['subDistrict']== groupData['kecamatan'][j], 'Days of Flood Recovery'] += groupData['lama_genangan'][j]
            
    return dataFrame