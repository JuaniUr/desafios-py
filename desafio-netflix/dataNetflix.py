import csv
from collections import Counter

archivo = open ('netflix_titles.csv', encoding="utf-8")

lector = csv.reader (archivo, delimiter= ',')
#print (lector)

archivo_pelis_2021 = open('peliculas_agregadas_2021.csv','w', encoding= "utf-8")

encabezado = next(lector)
#print(encabezado)

writer = csv.writer (archivo_pelis_2021)

writer.writerow(encabezado)
contador = Counter()

# Peliculas_2021 = filter (lambda x: '2021' in x(6), lector)

pelis_2021 = []

for linea in lector:
    pais = linea[5]
    contador[pais] += 1
    if ('2021' in linea[6]):
        writer.writerow(linea)
dic5 = dict (contador.most_common(5))
print (dic5)
archivo_pelis_2021.close()
archivo.close()                    