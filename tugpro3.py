# -*- coding: utf-8 -*-
"""Tugpro3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CxrN_nfnxU_8rmAActNfn9B9lRCqFaN_

Kelompok:
  - Mohammad Akbar Fauzy Ali (1301194133)
  - Ario Bagus Bramantyo (1301190372)
  - Kevin Daniel Hamonangan Ompusunggu (1301180276)

---


LIBRARY


---
"""

import math
import pandas
import numpy as np

"""

---


TRAINING DATA


---

"""

xls_train = pandas.read_excel('https://github.com/AkbarFauzy/test.xls/blob/main/mobil.xls?raw=true')
xls_train.head()

"""

---


TEST DATA


---

"""

xls_test = pandas.read_excel('https://github.com/AkbarFauzy/test.xls/blob/main/test.xls?raw=true')
xls_test.head()

"""

---


KNN CLASS


---

"""

class KNN:
  def __init__(self, _data_test, _data_train, k = 3):
    self.k = k
    self.data_test = _data_test
    self.neighbors = pandas.DataFrame(self.NearestNeighbor(self.data_test, _data_train),
                                      columns=['Nama Mobil',
                                               'Ukuran',
                                               'Kenyamanan',
                                               'Irit',
                                               'Kecepatan',
                                               'Harga (Ratus Juta)',
                                               'Euclidean',
                                               'Manhattan',
                                               'Minkowski',
                                               'Supremum'])

  def Euclidean(self, data1, data2):
    sum = 0
    for i in range(len(data1)):
      sum += (data1[i] - data2[i+1])**2
    return math.sqrt(sum)

  def Manhattan(self, data1, data2):
    sum = 0
    for i in range(len(data1)):
      sum += abs(data1[i] - data2[i+1])
    return sum

  def Minkowski(self, data1, data2, h = 1.5):
    sum = 0
    for i in range(len(data1)):
      sum += abs((data1[i] - data2[i+1]))**h
    return sum**1./h

  def Supremum(self, data1, data2):
    sum = []
    for i in range(len(data1)):
      sum.append(abs(data1[i] - data2[i+1]))
    return max(sum)

  def NearestNeighbor(self, _data_test, _data_train):
    Neighbor = [] 
    for i in range(len(_data_train)): 
      Neighbor.append(np.append(_data_train[i], 
                      np.append(self.Euclidean(_data_test, _data_train[i]), 
                      np.append(self.Manhattan(_data_test, _data_train[i]), 
                      np.append(self.Minkowski(_data_test, _data_train[i]), 
                                self.Supremum(_data_test, _data_train[i]))))))
    return Neighbor

"""

---


MAIN PROGRAM


---


"""

output = KNN(xls_test.values.flatten(), xls_train.values)

euclidean = output.neighbors.sort_values(by='Euclidean')[:output.k]
manhattan = output.neighbors.sort_values(by='Manhattan')[:output.k]
minkowski = output.neighbors.sort_values(by='Minkowski')[:output.k]
supremum = output.neighbors.sort_values(by='Supremum')[:output.k]

euclidean['Nama Mobil'].to_excel('rekomendasi_euclidean.xls', index = False, header= False)
manhattan['Nama Mobil'].to_excel('rekomendasi_manhattan.xls', index = False, header= False)
minkowski['Nama Mobil'].to_excel('rekomendasi_minkowski.xls', index = False, header= False)
supremum['Nama Mobil'].to_excel('rekomendasi_supremum.xls', index = False, header= False)

# Hanya untuk Visualisasi data
# display(euclidean)
# display(manhattan)
# display(minkowski)
# display(supremum)