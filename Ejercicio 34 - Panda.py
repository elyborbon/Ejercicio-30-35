import pandas as pd
capitales = ["Moscu", "Berlin", "Bogota", "Lima", "Paris"]
paises = ["Rusia", "Alemania", "Colombia", "Peru", "Francia"]

#Ejercicio 2
serie = pd.Series(capitales, index=paises)
print (serie)

#Ejercicio 1
diccionario = serie.to_dict()
print (diccionario)

print (type(diccionario))