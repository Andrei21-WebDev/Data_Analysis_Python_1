import numpy as np
import pandas as pd
import prices as prices
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
import csv

from functions import *

elevi = pd.read_csv("Date/elevi_inscrisi.csv", index_col=0)
eleviInscrisi = list(elevi)[0:]
#print(eleviInscrisi)
valori = elevi[eleviInscrisi].values

coduriJudete = pd.read_csv("Date/judete.csv", index_col=0)
merge = elevi.merge(right=coduriJudete, left_index=True, right_index=True)
#print(merge)

# 1. PONDEREA ELEVILOR INSCRISI IN PERIOADA 2018 - 2021
eleviJudete = merge[eleviInscrisi + ["CodJudet"]].groupby(by="CodJudet").agg(sum)
ponderiElevi = np.transpose(np.transpose(eleviJudete.values)/np.sum(eleviJudete.values, axis=1))
salvarePonderi = pd.DataFrame(ponderiElevi, eleviJudete.index, eleviJudete.columns)
salvarePonderi.to_csv("Rezolvari/PonderiElevi.csv")

# 2. ENTROPIA
entropiePonderi = salvarePonderi.apply(func=shannon, axis=1)
entropiePonderi.name = "Entropia"
entropiePonderi.to_csv("Rezolvari/Entropie.csv")

# 3. SIMPSON
simpsonPonderi = salvarePonderi.apply(func=simpson, axis=1)
simpsonPonderi.name = "Simpson"
simpsonPonderi.to_csv("Rezolvari/Simpson.csv")

# 4. STANDARDIZARE
stand = standardizareDate(elevi, scal=False)
#print(stand)
salvareDate(stand, elevi.index, eleviInscrisi, "Rezolvari/Standardizare.csv")

# 5. CORELATIA
corelatia = np.corrcoef(valori, rowvar=False)
salvareDate(corelatia, eleviInscrisi, eleviInscrisi, "Rezolvari/Corelatie.csv")

# 6. COVARIANTA
covarianta = np.cov(valori, rowvar=False)
#print("Covarianta: ", covarianta)
salvareDate(covarianta, eleviInscrisi, eleviInscrisi, "Rezolvari/Covarianta.csv")

#INVSIMPSON
invsimpsonPonderi = salvarePonderi.apply(func=invsimpson, axis=1)
invsimpsonPonderi.name = "Invsimpson"
invsimpsonPonderi.to_csv("Rezolvari/Invsimpson.csv")

# 7. BAR CHART - REPREZENTAREA GRAFICA A DISTRIBUTIEI DE ELEVI REPARTIZATI PE JUDETE INTRE 2018 SI 2021
#data = dict()
#with open('Date/bar_chart_elevi.csv', 'r') as f:
    #for line in f.readlines():
        #an, judet, nrElevi = line.split(',')
        #if an not in data:
            #data[an] = []
        #data[an].append((judet, int(nrElevi)))
#positions = [221, 222, 223, 224]
#colors = ['r', 'g', 'b', 'y']
#for i, l in enumerate(data.keys()):
    #plt.subplot(positions[i])
    #data_i = dict(data[l])
    #plt.bar(data_i.keys(), data_i.values(), color=colors[i])
    #plt.xlabel(l)
#plt.show()

# 8. PIE CHART - TOTALUL ELEVILOR INSCRISI INTRE 2018 SI 2021 (EXPRIMAT IN PROCENTE)
ani = []
total_elevi = []

#with open('Date/total_elevi.csv', 'r') as csvfile:
    #linii = csv.reader(csvfile, delimiter=',')
    #for i in linii:
        #ani.append(i[0])
        #total_elevi.append(int(i[1]))
#plt.pie(total_elevi, labels=ani, autopct='%.2f%%')
#plt.title('Numarul total de elevi (%)', fontsize=20)
#plt.show()

# 9. NUMARUL MEDIU DE ELEVI INSCRISI IN PERIOADA 2018-2021
#x = []
#y = []
#with open('Date/medie_elevi.csv', 'r') as csvfile:
    #lines = csv.reader(csvfile, delimiter=',')
    #for row in lines:
        #x.append(row[0])
        #y.append(int(row[1]))
#plt.plot(x, y, color='g', linestyle='dashed', marker='o')
#plt.xticks(rotation=25)
#plt.xlabel('Interval timp')
#plt.ylabel('Medie elevi')
#plt.title('Raport medie elevi', fontsize=20)
#plt.grid()
#plt.show()