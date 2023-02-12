"""
1. Scrivete una funzione di nome triangolo che riceva tre interi come argomenti e che mostri
"Si" o "No", a seconda che si possa o meno formare un triangolo con dei bastoncini delle tre
lunghezze date. 
(Se la somma di due lunghezze è uguale alla terza, si ha un triangolo "degenere".)

2. Scrivete una funzione che chieda all'utente di inserire tre lunghezze, le converta in interi, e le 
passi a triangolo per verificare se si possa o meno formare un triangolo.
"""

def triangolo(a, b, c):
    if a > b + c:
        print("No")
    elif b > a + c:
        print("No")
    elif c > a + b:
        print("No")
    else:
        print("Si")

def chiedi_lunghezze_e_verifica_triangolo():
    a = int(input("Inserisci la prima lunghezza: "))
    b = int(input("Inserisci la seconda lunghezza: "))
    c = int(input("Inserisci la terza lunghezza: "))
    triangolo(a, b, c)

chiedi_lunghezze_e_verifica_triangolo()
