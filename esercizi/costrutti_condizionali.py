# n = int(input("Inserisci un numero: "))
# somma = 0
# for i in range(1, n+1):
#     somma += i
# print("La somma dei primi", n, "numeri è:", somma)


# n = int(input("Inserisci il numero di cui stampare la tabellina: "))

# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)
#     print(f"{n} x {i} = {n * i}")
#     print("%d x %d = %d" % (n, i, n * i))


# n = int(input("Inserisci un numero: "))

# for i in range(2, n+1):
#     if i % 2 == 0:
#         print(i)
 


# n= int(input("inserisci il numero:"))

# fatt=1

# for n in range(1,n+1):
#     fatt*=n
# print(f"Il fattoriale di {n} è: {fatt}")    

  
# n= int(input("inserisci il numero:"))
# x = n
# fatt=1

# for n in range(n,1,-1):
#     fatt*=n
# print(f"Il fattoriale di {x} è: {fatt}")       


# n = int(input("inserisci il numero:"))

# for i in range(1, n+1):
#     if i % 3 == 0:
#         print(i, end=" ")


# n = int(input("inserisci il numero:"))

# for i in range(1, n+1):
#     quad = i ** 2
#     print(f"Il quadrato di {i} è: {quad}")


#Calcola e stampa con input la somma dei primi n numeri dispari (es. n=5 → 1+3+5+7+9=25)
# somma=0
# num=1
# n=int(input("Inserisci il numero finale:"))
# for i in range (1,n+1):
#     somma= somma + num
#     num= num+2
# print(f"La somma numeri dispari fino a {n} è: {somma}")

#ALTERNATIVA AL CODICE PRECEDENTE

# n = int(input("Inserisci n: "))

# somma = 0
# contatore = 0

# for numero in range(1, n * 2 + 1):
#     if numero % 2 != 0:   # verifica se è dispari
#         somma += numero
#         contatore += 1
    
#     if contatore == n:    # fermati dopo n dispari
#         break

# print("La somma dei primi", n, "numeri dispari è:", somma)


#Dato in input base=2 ed esponente=5, calcola 2 elevato a 5.

# base = int(input("Inserisci la base: "))
# esponente = int(input("Inserisci l'esponente: "))
# risultato = 1
# for i in range(esponente):
#     risultato *= base
# print(f"{base} elevato a {esponente} = {risultato}")


#Scrivi un programma che stampa in input tutti i multipli di 5 da 5 a 100.

# n = int(input("Inserisci un numero: "))
# for i in range(5, n+1, 5):
#     print(i)
    

#Scrivi un programma che stampa in input i numeri dispari da 1 a 19.

# n = int(input("Inserisci un numero: "))

# for i in range(1, n+1, 2):
#     print(i, end=" ")


#Scrivi un programma che stampa in input la tabellina del 9 al contrario (da 10×9 a 1×9).

# n = int(input("Inserisci un numero: "))

# for i in range(10, 0, -1):
#     print(f"{i} x {n} = {i * n}")


#Scrivi un programma utilizzando input che calcola la somma dei numeri pari da 2 a 50.

# n = int(input("Inserisci un numero: "))

# somma = 0
# for i in range(2, n+1, 2):
#     somma += i
# print(f"La somma dei numeri pari da 2 a {n} é: {somma}")


#Scrivi un programma utilizzando input che stampa il cubo di ogni numero da 1 a 10 (es: 1³=1, 2³=8, ecc.).

# n = int(input("Inserisci un numero: "))

# for i in range(n):
#     cubo = (i+1) ** 3
#     print(f"Il cubo di {i+1} è: {cubo}")


#Scrivi un programma utilizzando input che calcola la media dei numeri da 1 a 20.

# n = int(input("Inserisci un numero: "))

# somma = 0
# for i in range(1, n+1):
#     somma += i
# media = somma / n
# print(f"La media dei numeri da 1 a {n} é: {media}")

# i =20
# while i >= 10:
#     print(i)
#     i -= 1
# else:
#     print("Il ciclo è terminato")

