#(STILL WORKING ON LEARNING THE FORMAT (CSV)
"""
Quarter 4 Project Code

"""
"""

'''
use append to add to a list - we need to sort list tho
'''

'''
import pandas as pd
#import matplotlib.pyplot as plt <-- possile way to import excel sheet into code.
#    df = pd.read_csv("C:\\Users\\_____\\Downloads\\_____.csv")

d = {'Team': [1, 2, 3, 4, 7], 'PTS': [14, 10, 9, 6, 5], 'GD': [7, 8, 12, 1, 11]}

df = pd.DataFrame(data=d)

print(df)

'''
import pandas as pd

chart = {'|-----Team------|': ['Juventus', 'Inter', 'AC Milan', 'AS Roma', 'Lazio', 'Napoli', 'Genoa', 'Empoli','Lecce','Bolonga','Frosinone','Fiorentina', 'Atlanta','Hellas Verona','Torino', 'Monza','Sassoulo','Udinese','Salernitana','Cagliari', ], '|PTS|': [14, 10, 9, 6, 5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 7, 8, 9, 20], '|GD|': [7, 8, 12, 1, 11, 1, 3, 4, 5, 6, 6, 7, 23, 5, 2, 4, 5, 23, 4, 2]}

standings_chart = pd.DataFrame(data=chart)

print(standings_chart)

row_count = standings_chart.shape[0]

print('\n' + "Number of teams:")
print(row_count)

'''
    
    Juventus,
    Inter,
    AC_Milan,
    Roma,
    Napoli,
    Bolonga,
    Torino,
    Fiorentina,
    Lecce,
    Frosinone,
    Cagliari,
    Salernitana,
    Sassoulo,
    Udinese,
    Lazio,
    Monza,
    Hellas_Verona,
    Atalanta,
    Genoa,
    Empoli,   
'''    


