# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:36:49 2020

@author: ASUS
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#
#
#features = ['month','no. of subdistrict affected','no. of People Affected','no. of People Forced to Relocate','Days of Flood Recovery']
#year = [2013,2014,2015,2016,2017,2018]
#noOfMonth = np.linspace(1,12,num=12)
#data =[]
#
#for i in range(len(year)):
#    
#    df= pd.DataFrame(0,index= np.arange(len(noOfMonth)), columns=features)
#
#    dataFlood = pd.read_csv('Data-Rekap-Banjir-'+str(year[i])+'.csv')
#
#    df = dataFlood[['bulan','kecamatan','jiwa_terdampak','jumlah_jiwa_pengungsi_tertinggi','lama_genangan']].fillna(0)
#    df.columns=features
#    df['year'] =year[i]
#    
#    data.append(df)
#
#dataFlood_2013 = data[0].apply(pd.to_numeric)
#dataFlood_2014 = data[1].apply(pd.to_numeric)
#dataFlood_2015 = data[2].apply(pd.to_numeric)
#dataFlood_2016 = data[3].apply(pd.to_numeric)
#dataFlood_2017 = data[4].apply(pd.to_numeric)
#
#
#print(dataFlood_2013['month'])
#
#
#
#plt.figure(figsize=(12, 8))
#
#plt.plot(dataFlood_2013['month'], dataFlood_2013['no. of subdistrict affected'], marker='o', markerfacecolor='blue', markersize=12, color='blue', linewidth=3, label='2013')
#plt.plot(dataFlood_2014['month'], dataFlood_2014['no. of subdistrict affected'], marker='o', markerfacecolor='red', markersize=12, color='red', linewidth=3, label='2014')
#plt.plot(dataFlood_2015['month'], dataFlood_2015['no. of subdistrict affected'], marker='o', markerfacecolor='green', markersize=12, color='green', linewidth=3, label='2015')
#plt.plot(dataFlood_2016['month'], dataFlood_2016['no. of subdistrict affected'], marker='o', markerfacecolor='orange', markersize=12, color='orange', linewidth=3, label='2016')
#plt.plot(dataFlood_2017['month'], dataFlood_2017['no. of subdistrict affected'], marker='o', markerfacecolor='magenta', markersize=12, color='magenta', linewidth=3, label= '2017')
#
#plt.show()
##
#################################################################################
###
#dataRainfallRate = pd.read_csv('curah-hujan.csv')
#dataRainfallRate = dataRainfallRate.iloc[1:13]
#
#d = {'Januari':1, 'Februari':2, 'Maret':3, 'April':4, 'Mei':5, 'Juni':6,\
#      'Juli':7,'Agustus':8,'September':9,'Oktober':10, 'November':11, 'Desember':12}
#
#dataRainfallRate = dataRainfallRate[['Bulan','2013','2014','2015','2016','2017']]
#dataRainfallRate.Bulan = dataRainfallRate.Bulan.map(d)
#
#dataRainfallRate = dataRainfallRate.apply(pd.to_numeric)
#
#print(dataRainfallRate['2013'])
#
#plt.figure(figsize=(12, 8))
#plt.plot(dataRainfallRate['Bulan'], dataRainfallRate['2013'], marker='o', markerfacecolor='blue', markersize=12, color='blue', linewidth=3)
#plt.plot(dataRainfallRate['Bulan'], dataRainfallRate['2014'], marker='o', markerfacecolor='red', markersize=12, color='red', linewidth=3)
#plt.plot(dataRainfallRate['Bulan'], dataRainfallRate['2015'], marker='o', markerfacecolor='green', markersize=12, color='green', linewidth=3)
#plt.plot(dataRainfallRate['Bulan'], dataRainfallRate['2016'], marker='o', markerfacecolor='orange', markersize=12, color='orange', linewidth=3)
#plt.plot(dataRainfallRate['Bulan'], dataRainfallRate['2017'], marker='o', markerfacecolor='magenta', markersize=12, color='magenta', linewidth=3)
#plt.show()
#
################################################################################
#from sklearn import preprocessing
#
#plt.figure(figsize=(12, 8))
#plt.plot(dataRainfallRate['2013'], dataFlood_2013['no. of subdistrict affected'],'rx')
#plt.plot(dataRainfallRate['2014'], dataFlood_2014['no. of subdistrict affected'],'rx')
#plt.plot(dataRainfallRate['2015'], dataFlood_2015['no. of subdistrict affected'],'rx')
#plt.plot(dataRainfallRate['2016'][0:-1], dataFlood_2016['no. of subdistrict affected'],'rx')
#plt.plot(dataRainfallRate['2017'], dataFlood_2017['no. of subdistrict affected'],'rx')
#plt.xlim(0,800)
#plt.ylim(0,30)
#plt.show()
#
################################################################################
#plt.figure(figsize=(12, 8))
#plt.plot(dataRainfallRate['2013'], dataFlood_2013['no. of People Affected'],'rx')
#plt.plot(dataRainfallRate['2014'], dataFlood_2014['no. of People Affected'],'rx')
#plt.plot(dataRainfallRate['2015'], dataFlood_2015['no. of People Affected'],'rx')
#plt.plot(dataRainfallRate['2016'][0:-1], dataFlood_2016['no. of People Affected'],'rx')
#plt.plot(dataRainfallRate['2017'], dataFlood_2017['no. of People Affected'],'rx')
##plt.xlim(0,700)
#plt.ylim(-30000,250000)
#plt.show()
#
################################################################################
#
#pdListX = [dataRainfallRate['2013'], dataRainfallRate['2014'], dataRainfallRate['2015'], \
#          dataRainfallRate['2016'][0:-1], dataRainfallRate['2017']]
#
#pdListY_district =[dataFlood_2013['no. of subdistrict affected'],dataFlood_2014['no. of subdistrict affected'],\
#                   dataFlood_2015['no. of subdistrict affected'], dataFlood_2016['no. of subdistrict affected'],\
#                   dataFlood_2017['no. of subdistrict affected']]
#pdListY_population = [dataFlood_2013['no. of People Affected'],dataFlood_2014['no. of People Affected'],\
#                      dataFlood_2015['no. of People Affected'],dataFlood_2016['no. of People Affected'],\
#                      dataFlood_2017['no. of People Affected']]
#
#X = pd.concat(pdListX,ignore_index=True).values
#Y_district = pd.concat(pdListY_district,ignore_index=True).values
#Y_population = pd.concat(pdListY_population,ignore_index=True).values
#
##
#Y_district_array=Y_district.reshape(len(Y_district),1)
#Y_population_array=Y_population.reshape(len(Y_population),1)
#X_array = X.reshape(len(X),1)
#
#X_population = np.delete(X_array, np.argmax(Y_population_array))
#X_population = X_population.reshape(len(X_population),1)
#Y_population_array = np.delete(Y_population_array, np.argmax(Y_population_array))
#Y_population_array = Y_population_array.reshape(len(Y_population_array),1)
#print(np.shape(Y_population_array))
#
####################################### Linear Regression Model ###################################################
#from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LinearRegression
#
#lm = LinearRegression()
#xTrain, xTest, yTrain, yTest = train_test_split(X_array,Y_district_array, test_size = 0.3, random_state=40)
#
#lm.fit(xTrain,yTrain)
#
#lmArray = np.asanyarray([lm.intercept_,lm.coef_])
#print(lmArray)
##
#flip = np.flip(lmArray.transpose()).reshape((2,))
#normEqPolyFit = np.poly1d(flip)
#plt.figure(figsize=(12, 8))
#plt.plot(X,Y_district,'rx',X,normEqPolyFit(X),'-b',linewidth=3)
#plt.show()
#
####################################### Polynomial Regression Model ###################
#
#from sklearn.preprocessing import PolynomialFeatures
#
#Rsqu_test = []
#xTrain, xTest, yTrain_pop, yTest_pop = train_test_split(X_population,Y_population_array, test_size = 0.3, random_state=40)
#
#order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#for n in order:
#    pr = PolynomialFeatures(degree=n)
#    
#    xTrain_pr = pr.fit_transform(xTrain)
#    xTest_pr = pr.fit_transform(xTest)      
#    lm.fit(xTrain_pr, yTrain_pop)
#    
#    Rsqu_test.append(lm.score(xTest_pr, yTest_pop))
#
#plt.figure(figsize=(12, 8))
#plt.plot(order, Rsqu_test, linewidth=3)
#plt.xlabel('order')
#plt.ylabel('R^2')
#plt.title('R^2 Using Test Data')
#plt.ylim(0.30,1)
#plt.show()
##
#########################################################################################
#inds = X_population.ravel().argsort()   
#X_p = X_population.ravel()[inds].reshape(-1,1)
#Y_p = Y_population_array[inds]
#pr_2 = PolynomialFeatures(degree=2)
#
#xTrain_pr = pr_2.fit_transform(X_p)
#   
#lm.fit(xTrain_pr, Y_p)
#plt.figure(figsize=(12, 8))
#plt.plot(X_p,Y_p,'rx')
#plt.plot(X_p, lm.predict(xTrain_pr),'-b',linewidth=3)
###

data2018 = pd.read_csv('bps-file.csv')

print(data2018)
dataDKI = data2018[data2018.Kabupaten.isin(['DKI Jakarta'])]
dataDKI = dataDKI.dropna(axis='columns')
print(dataDKI)
