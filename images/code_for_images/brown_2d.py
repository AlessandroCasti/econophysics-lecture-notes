# brownian_motion_script.py

import numpy as np
import matplotlib.pyplot as plt

# --- Parametri della simulazione ---
num_steps = 5000  # Numero di passi nel percorso
time_step = 1     # Intervallo di tempo per ogni passo (arbitrario)
# La dimensione del passo è legata alla "temperatura" del sistema.
# Usiamo una deviazione standard di sqrt(time_step) come da teoria.
step_size_std = np.sqrt(time_step) 

# --- Simulazione ---
# Genera passi casuali indipendenti in 2D (direzioni x e y)
# da una distribuzione normale con media 0.
steps = np.random.normal(loc=0.0, scale=step_size_std, size=(num_steps, 2))

# Calcola la traiettoria sommando cumulativamente i passi.
# La posizione al tempo t è la somma di tutti i passi fino a t.
path = np.cumsum(steps, axis=0)

# Aggiungi il punto di partenza all'origine (0,0)
start_point = np.zeros((1, 2))
path = np.vstack([start_point, path])

# --- Plotting ---
plt.figure(figsize=(8, 8))
plt.plot(path[:, 0], path[:, 1], lw=0.7, color='blue') # Traccia il percorso

# Evidenzia il punto di inizio e di fine
plt.plot(path[0, 0], path[0, 1], 'go', markersize=8, label='Start')
plt.plot(path[-1, 0], path[-1, 1], 'ro', markersize=8, label='End')

# Formattazione del grafico
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, linestyle='--', alpha=0.6)
plt.axis('equal') # Assicura che le scale sugli assi x e y siano uguali
plt.legend()

# Salva l'immagine in un file che puoi usare in LaTeX
plt.savefig("brownian_motion_2d.png", dpi=300)

# Mostra il grafico
plt.show()
