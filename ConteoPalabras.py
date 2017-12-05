texto = "este texto es una prueba para el conteo de palabras xd"
pala = texto.split()
numPala = 0

while numPala < len(pala):
    numPala += 1

print ("El numero de palabras en el texto es: " + str(numPala))