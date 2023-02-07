# Realizza uno script che acquisisca il tempo attuale (GMT) e lo converta in un tempo in ore, minuti e 
# secondi, più i giorni trascorsi dal "tempo zero".
# Nei sistemi UNIX, questo "tempo zero" è il 1 gennaio 1970.

import time

def tempo_attuale():
    tempo_in_secondi = time.time()
    tempo_in_minuti = tempo_in_secondi / 60
    tempo_in_ore = tempo_in_minuti / 60
    tempo_in_giorni = int(tempo_in_ore / 24)
    ore_rimanenti = int(tempo_in_ore % 24)
    minuti_rimanenti = int(tempo_in_minuti % 60)
    secondi_rimanenti = int(tempo_in_secondi % 60)
    print("Il tempo attuale è", ore_rimanenti, "ore", minuti_rimanenti, "minuti e", secondi_rimanenti, "secondi" )
    print("Sono trascorsi", tempo_in_giorni, "giorni dal tempo zero")

tempo_attuale()