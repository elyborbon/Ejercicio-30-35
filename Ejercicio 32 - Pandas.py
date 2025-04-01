import pandas as pd 
lista = [5,3,5,7,7,7,3,1,2,3,4,5]

lista_1 = pd.Series(lista )
print (lista_1)
print (lista_1.value_counts())
