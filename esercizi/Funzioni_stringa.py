vendite = [100, 200, 300, 400, 500]

max = vendite[0]
for p in vendite:
    if p > max:
        max = p
print(f"Il prezzo massimo è: {max}")
    
    
vendite = [100, 200, 300, 400, 500]



variabile = "lorem(ipsum   dolor sit amet, consectetur adipiscing elit.,Sed do eiusmod tempor incididunt ut labore ,et dolore magna aliqua.)"


print(variabile.isalpha()) # False, perché contiene spazi e caratteri speciali

print(variabile.isdigit()) # False, perché contiene lettere e spazi

print(variabile.isalnum()) # True, perché contiene solo lettere e numeri

print(variabile.upper()) # LOREM(IPSUM   DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT. SED DO EIUSMOD TEMPOR INCIDIDUNT UT LABORE ET DOLORE MAGNA ALIQUA.)

print(variabile.islower()) # lorem(ipsum   dolor sit amet, consectetur adipiscing elit. sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.)

print(variabile.lower()) # lorem(ipsum   dolor sit amet, consectetur adipiscing elit. sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.)

print(variabile.title()) # Lorem(Ipsum   Dolor Sit Amet, Consectetur Adipiscing Elit. Sed Do Eiusmod Tempor Incididunt Ut Labore Et Dolore Magna Aliqua.)

print(variabile.startswith("lorem")) # True, perché la stringa inizia con "lorem"

print(variabile.replace("lorem", "LOREM")) # LOREM(ipsum   dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.)

print(variabile.split(",")) # ['lorem(ipsum   dolor sit amet, consectetur adipiscing elit. sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.)']

conteggio = variabile.split(",")
print(len(conteggio)) 

print(variabile.strip()) # Rimuove gli spazi iniziali e finali, ma non ci sono spazi in questo caso, quindi restituisce la stringa originale    

variabile = "Pietro"

nome = "   Mario Rossi   "
x = " A".join(variabile)
print(x)

print(variabile.find("Pi")) # Restituisce l'indice della prima occorrenza di "Pi" nella stringa, che è 0





   
