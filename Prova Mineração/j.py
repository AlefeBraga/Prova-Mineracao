import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('titanic.csv')
titanic.to_excel('titanic.xlsx')