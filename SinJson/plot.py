import random
import numpy as np
import matplotlib.pyplot as plt
from API import *

def trigger_hist_from_tuples(tuples_list):
    # diccionario para contar la frecuencia de cada valor
    freq_dict = {}
    for item in tuples_list:
        if item[0] not in freq_dict:
            freq_dict[item[0]] = 1
        else:
            freq_dict[item[0]] += 1

    # listas para almacenar los nombres y las frecuencias
    names = []
    frequencies = []
    colors = []

    # generar un color aleatorio para cada barra
    for i in range(len(freq_dict)):
        colors.append('#{:06x}'.format(random.randint(0, 256**3-1)))

    # agregar los nombres y las frecuencias a las listas
    for key, value in freq_dict.items():
        names.append(key)
        frequencies.append(value)

    # crear el histograma
    plt.bar(names, frequencies, color=colors)
    plt.xticks(rotation=90)
    plt.ylabel('Frecuencia')
    plt.xlabel('Canciones')
    plt.show()

def trigger_heatmap_from_tuples(tuples_list):
# extraer los primeros valores de cada tupla
    values = [item[0] for item in tuples_list]

    # extraer las frecuencias de cada valor
    frequencies = []
    for value in set(values):
        freq = values.count(value)
        frequencies.append(freq)

    # crear el mapa de calor
    heatmap, xedges, yedges = np.histogram2d(frequencies, frequencies, bins=10)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.clf()
    plt.imshow(heatmap.T, extent=extent, origin='lower')
    plt.xlabel('Frecuencia')
    plt.ylabel('Frecuencia')
    plt.colorbar()
    plt.show()


recently_played = get_recently_played_songs(50)
top_tracks = get_user_top_tracks(20)
trigger_hist_from_tuples(recently_played)