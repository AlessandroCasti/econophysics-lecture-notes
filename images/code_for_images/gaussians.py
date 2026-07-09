import numpy as np
import matplotlib.pyplot as plt
import scienceplots

# Imposta lo stile del grafico
plt.style.use(['science', 'grid'])

# Dati per il grafico
x = np.linspace(-5, 5, 500)
# Aggiunto un tempo molto piccolo (0.05) per la gaussiana stretta
times = [0.05, 0.2, 1.0, 4.0] 
# Etichette aggiornate per 4 curve
labels = [r'$t_1 > 0$', r'$t_2 > t_1$', r'$t_3 > t_2$', r'$t_4 > t_3$']
# Aggiunto il nero per la prima curva e scalato gli altri blu
colors = ['#000000', '#0d47a1', '#1976d2', '#64b5f6'] 

# Creazione della figura
fig, ax = plt.subplots(figsize=(6, 4))

# Disegna le quattro curve gaussiane
for i, t in enumerate(times):
    # Funzione Gaussiana p(x,t) con D=1/2
    y = 1 / np.sqrt(2 * np.pi * t) * np.exp(-x**2 / (2 * t))
    ax.plot(x, y, label=labels[i], color=colors[i])

# --- BLOCCO PER LA FRECCIA RIMOSSO ---

# Imposta gli assi centrati
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Etichette degli assi
ax.set_xlabel('$x$', loc='right')
ax.set_ylabel('$p(x,t)$', loc='top', rotation=0)

# Imposta i limiti e rimuove i tick numerici
ax.set_xlim(-5, 5)
ax.set_ylim(0, 2)
ax.set_xticks([])
ax.set_yticks([])

# Aggiunge la legenda
ax.legend()

# Salva il grafico in formato PDF vettoriale
plt.savefig('gaussian_evolution.pdf')

print("Grafico 'gaussian_evolution.pdf' aggiornato con successo.")
