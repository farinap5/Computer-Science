#!/usr/bin/python3
import numpy as np

anosFile = "./anos.txt"
alturaFile = "./altura.txt"
minA = 1998
maxA = 2005

anos = np.array(np.loadtxt(anosFile),dtype=int)
janelaAno = ((anos>=minA) & (anos<=maxA))

idx = np.where(janelaAno)
alturas = np.array(np.loadtxt(alturaFile), dtype=float)

avg = np.average(alturas[idx])
print("Média das alturas: {altura:.4}".format(altura=avg))
