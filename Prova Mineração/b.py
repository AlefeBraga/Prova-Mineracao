from os import name
import pandas as pd

titanic = pd.read_csv("titanic.csv")

NomesAlf = titanic.sort_values('Name')
print("Ordem alfabetina nome:")
print (NomesAlf.head(20))