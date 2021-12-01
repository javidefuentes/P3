#Comparacion

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav

 # Abrir los ficheros
pitch_filename = 'get_pitch_de_sb050.txt'
pitch_wavesurfer_filename = 'pitch_del_wavesurfer.f0'
pitch = np.loadtxt(pitch_filename, skiprows=0,)
pitch_wavesurfer = np.loadtxt(pitch_wavesurfer_filename, skiprows=0,)

# Representar las dos señales
plt.plot( pitch, 'skyblue', label="Sin usar filtro de mediana")
plt.plot( pitch_wavesurfer, 'salmon', label="Usando filtro de mediana")
#plt.xlabel("$Tiempo (s)$", fontsize=8)
plt.ylabel("Frecuencia (Hz)", fontsize=8)
plt.title("Resultado de los pitch", fontsize=10)
plt.legend(loc='upper right', shadow=True, fontsize=6)
plt.show(block=True)
plt.savefig('Comparacion_pitch_2.png')