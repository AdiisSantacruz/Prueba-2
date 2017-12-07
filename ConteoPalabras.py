def creartxt():
    archi=open('respuesta.txt','w')
    archi.close()
def grabartxt():
    archi = open ('respuesta.txt','a')
    archi.write(str(numPala))
    archi.close()

texto = "este texto es una prueba para el conteo de palabras xd"
pala = texto.split()
numPala = 0

while numPala < len(pala):
    numPala += 1

print ("El numero de palabras en el texto es: " + str(numPala))

creartxt()
grabartxt()
