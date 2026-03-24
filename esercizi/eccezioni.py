#Gestisci l'eccezione ValueError convertendo una stringa in un intero
# try:
#     numero = int("abc")
# except ValueError:
#     print("Si è verificato un errore: la stringa non può essere convertita in un intero.")  
    
# try:
#     numero = int("abc")
# except Exception as e:
#     print(f"Si è verificato un errore: {e}  {type(e)}")
#     print(e.__class__)



#Gestisci l'eccezione AttributeError definendo il valore di una stringa None

# stringa = None

# try:
#     lunghezza = len(stringa)  # Usa len() per la lunghezza
#     print(f"Lunghezza: {lunghezza}")
# except Exception as e:             # Cattura TypeError, non AttributeError
#     print(f"Errore: l'oggetto non ha una lunghezza definita (es. è None). {e}")
    
    
    
#Gestisci l'eccezione TypeError creando operazioni tra tipi diversi

# try:
#     risultato = 2 + "2"  # Somma un intero con una stringa
#     print(f"Risultato: {risultato}")
# except TypeError as e:
#     print(f"Si sono verificati errori di tipo: {e}")


#Gestisci le eccezioni ZeroDividError e AttributeError nello stesso blocco utilizzando try except

# stringa = None
# try:
    
#     lunghezza = len(stringa)
#     print(f"Lunghezza: {lunghezza}")    # Usa len() per la lunghezza
#     divisione = 10 / 0  # Questo causerà ZeroDivisionError
# except Exception as e:
#     print(f"Si sono verificati errori di tipo: {e}")
# except ZeroDivisionError as e:
#     print(f"Si è verificato un errore di divisione per zero: {e}")


#Gestisci le eccezioni ValueError e TypeError nello stesso blocco utilizzando try except

# try:
#     numero = int("abc")  # Questo causerà ValueError
#     risultato = 2 + "2"  # Questo causerà TypeError
# except ValueError as e: 
#     print(f"Si sono verificati errori di tipo: {e}")
# except TypeError as e:
#     print(f"Si sono verificati errori di tipo: {e}")



#Valida una stringa non vuota utilizzando try except

# stringa = ""
# try:
#     if not stringa:  # Controlla se la stringa è vuota
#         raise ValueError("La stringa non può essere vuota.")
#     print(f"Stringa valida: {stringa}")
# except ValueError as e:
#     print(f"Errore: {e}")


#Valida un eta' specificando che non può' essere minore di 0 e maggiore di 100 usando try except

# eta = -5
# try:
#     if eta < 0 or eta > 100:
#         raise ValueError("L'età deve essere compresa tra 0 e 100.")
#     print(f"Età valida: {eta}")
# except ValueError as e:
#     print(f"Errore: {e}")


#Gestisci 2 tipologie di eccezioni diverse utilizzando un blocco try annidato

# try:
#     numero = int(input("Inserisci un numero: "))
#     if numero < 0:
#         raise ValueError("Il numero deve essere maggiore o uguale a zero.")
#     try:
#         if numero > 100:
#             raise ValueError("Il numero deve essere minore o uguale a 100.")   
#     except ValueError as e:
#         print(f"Errore: {e}")
# except ValueError as e:
#     print(f"Errore: {e}")  
# else:
#     print(f"Valore corretto inserito: {numero}")
    
# try:   
#     numero = 10
#     divisore = 0

#     print(numero / divisore)
# except:
#     print("Si è verificato un errore di divisione per zero.")


while True:
    try:
        numero1 = int(input("Inserisci il primo numero: "))
        numero2 = int(input("Inserisci il secondo numero: "))
        
        numero = numero1 / numero2
        #print("Il risultato della divisione dei due numeri inseriti é:",numero)
        #break
    except ZeroDivisionError:  
        print("Si è verificato un errore: il divisore non può essere zero.")
    
    except ValueError:
        print("Devi inserire un numero")
        
    else:
         print("Il risultato della divisione dei due numeri inseriti é:",numero)
         
    finally:
        print("operazione terminata")
        break