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
                        ,'Pclass': 'classe' 
                        ,'Name': 'Nome'
                        ,'Sex': 'Sexo'
                        ,'Age': 'Idade'
                        ,'Fare': 'Tarifa'
                        ,'Cabin': 'Cabine'
                        ,'Embarked': 'Embarque'
                        }, inplace = True)

titanic['Sexo'] = titanic['Sexo'].replace(['male','female'],['masculino', 'FEMININO'])


survivied = titanic.loc[titanic['Sobrevivente']=='Não']

Sobreviventes_per_Class = survivied.groupby(["Sobrevivente","Sexo"]).count()


print(Sobreviventes_per_Class['Nome'])

