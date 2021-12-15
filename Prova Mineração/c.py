from os import name
import pandas as pd

titanic = pd.read_csv("titanic.csv")

titanic['Sobrevivente'] = titanic['Survived']

titanic['Sobrevivente'] = titanic['Sobrevivente'].replace([0,1],['Não','Sim'])

NomesAlf = titanic.sort_values('Name')
print("Ordem alfabetina nome:")
print (NomesAlf.head(5))

