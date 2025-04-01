import pandas as pd 

Lista = [4,5,6,7,8,9,10]

Lista_T = pd.Series(Lista) 
print (Lista_T)

Objeto_Data = Lista_T.to_frame()
print (Objeto_Data)
print (type(Objeto_Data))