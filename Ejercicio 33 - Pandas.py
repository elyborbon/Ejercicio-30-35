import pandas as pd 
Lista = [10,20,30,40,50]

Lista_T = pd.Series(Lista)
print (Lista_T)

print (Lista_T.to_json())