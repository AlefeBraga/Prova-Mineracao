from os import name
import pandas as pd

titanic = pd.read_csv("titanic.csv")

titanic['Sobrevivente'] = titanic['Survived']

titanic['Sobrevivente'] = titanic['Sobrevivente'].replace([0,1],['Não','Sim'])

titanic.drop('SibSp', axis = 1 , inplace = True)
titanic.drop('Parch', axis = 1 , inplace = True)
titanic.drop('Ticket', axis = 1 , inplace = True)
titanic.drop('Survived', axis = 1 , inplace = True)

NomesAlf = titanic.sort_values('Name')
print("Ordem alfabetina nome:")
print (NomesAlf.head(5))

