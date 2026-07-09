import numpy as np
import matplotlib.pyplot as plt

# Numero di passi
num_steps = 1000

# Genera i passi del moto browniano
displacements = np.random.randn(num_steps)
brownian_motion = np.cumsum(displacements)

# Crea il plot
plt.figure(figsize=(10, 6))
plt.plot(brownian_motion, color='blue')

# Imposta la dimensione dei font degli assi
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

# Salva il grafico in formato PDF
plt.savefig('brownian_motion_1d.pdf')

plt.show()

import yfinance as yf
import matplotlib.pyplot as plt

# Scarica i dati intraday di oggi per l'S&P 500 (^GSPC)
sp500 = yf.Ticker("^GSPC")
# Intervallo di 1 minuto per la giornata odierna
hist = sp500.history(period="1d", interval="1m")

# Estrai il prezzo di chiusura per ogni minuto
spot_price = hist['Close']

# Crea il plot
plt.figure(figsize=(10, 6))
# Rimuoviamo l'asse x (le date) per l'estetica e plottiamo solo i valori
plt.plot(spot_price.values, color='red')


# Imposta la dimensione dei font degli assi
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

# Salva il grafico in formato PDF
# bbox_inches='tight' aiuta a non tagliare le etichette
plt.savefig('spot_price_sp500.pdf', bbox_inches='tight')

plt.show()


