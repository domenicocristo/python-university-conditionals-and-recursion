# L'ultimo teorema di Fermat afferma che non esistono numeri interi positivi a, b e c tali che 
# a^n + b^n = c^n per qualsiasi valore di n maggiore di 2.

# 1. Scrivete una funzione di nome verifica_fermat che richieda quattro parametri a, b, c e n
# e controlli se il teorema regge. Se n è maggiore di 2 e fosse a^n + b^n = c^n
# il programma dovrebbe visualizzare: "Santi Numi, Fermat si è sbagliato!", altrimenti: "No, questo non è vero."

# 2. Scrivete una funzione che chieda all'utente di inserire valori di a, b, c e n, li converta in interi
# e usi verifica_fermat per controllare se violano il teorema di Fermat.

def verifica_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Santi Numi, Fermat si è sbagliato!")
    else:
        print("No, questo non è vero.")

def chiedi_valori_e_verifica_fermat():
    a = int(input("Inserisci il valore di a: "))
    b = int(input("Inserisci il valore di b: "))
    c = int(input("Inserisci il valore di c: "))
    n = int(input("Inserisci il valore di n: "))
    verifica_fermat(a, b, c, n)
    
chiedi_valori_e_verifica_fermat()