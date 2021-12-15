from os import name
import pandas as pd

titanic = pd.read_csv("titanic.csv")

titanic['Sobrevivente'] = titanic['Survived']

titanic['Sobrevivente'] = titanic['Sobrevivente'].replace([0,1],['Não','Sim'])

titanic.drop('SibSp', axis = 1 , inplace = True)
titanic.drop('Parch', axis = 1 , inplace = True)
titanic.drop('Ticket', axis = 1 , inplace = True)
titanic.drop('Survived', axis = 1 , inplace = True)

titanic.rename(columns={'PassengerId': 'ID_Passageiro'
                        ,'Pclass': 'Classe' 
                        ,'Name': 'Nome'
                        ,'Sex': 'Sexo'
                        ,'Age': 'Idade'
                        ,'Fare': 'Tarifa'
                        ,'Cabin': 'Cabine'
                        ,'Embarked': 'Embarque'
                        }, inplace = True)

titanic['Sexo'] = titanic['Sexo'].replace(['male','female'],['masculino', 'FEMININO'])

NomesAlf = titanic.sort_values('Nome')
print("Ordem alfabetina nome:")
print (NomesAlf.head(5))
