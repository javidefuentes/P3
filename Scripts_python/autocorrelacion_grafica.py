#! /usr/bin/python3
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import sys
import wave
import soundfile as sf

ini = 48680 #Empezamos a contar los 30ms a partir del segundo 2,434, donde la trama es sonora, 2,434*20000
fin = 49280 #30 ms después en tramas->2,464
pitch_ini = 48780 #En esta muestra miraremos el periodo del pitch->Corresponde al segundo 2,439
pitch_fin = 48860 #En esta muestra acaba el perido del pitch que estamos mirando-->segundo 2,443
t = np.zeros(fin-ini)
sen, fm = sf.read('sb050.wav')
x = sen[ini: fin]
corr = np.correlate(x, x, 'full')
corr = corr[len(x) - 1: ]
for i in range(fin-ini):
    t[i] = ini + i*0.3/(fin-ini)

pitch = np.zeros(fin-ini)
pitch[100:180]=x[100:180]
plt_periodo = plt.subplot(211)
plt_periodo.set_xlabel("Tiempo", fontsize=8)
plt_periodo.set_ylabel("Amplitud", fontsize=8)
plt_periodo.set_title("Señal temporal", fontsize=10)

plt.plot(t, sen[ini:fin],c="skyblue", label='Señal de 30ms')
plt.plot(t,pitch,c="salmon",label='Periodo de pitch')
plt_periodo.legend(loc='upper right', shadow=True, fontsize=8) 
plt.tight_layout()

plt_corr = plt.subplot(212)
plt_corr.set_xlabel("A", fontsize=8)
plt_corr.set_ylabel("Amplitud", fontsize=8)
plt_corr.set_title("Autocorrelación de la señal", fontsize=10)
plt.plot(corr,c="skyblue",label ='Autocorrelación de la señal')
plt_corr.plot(81,2.08,'or',markersize=4,c="salmon", label='Máximo secundario obtenido en 81')
plt_corr.legend(loc='upper right', shadow=True, fontsize=8)

plt.show(block=True)