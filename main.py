# -*- coding: utf-8 -*-
"""
Quarter 4 Project Code

"""

'''
use append to add to a list - we need to sort list tho
'''

import pandas as pd
#from openpyxl.utils.dataframe import dataframe_to_rows
#from openpyxl open load_workbook

path = r"C:\Users\samue\Downloads\---.xlsx"
#r"C:\Users\samue\Downloads\Q4 FInal Spreadsheet Data - For Project.xlsx"
#r"C:\Users\samue\OneDrive\Documents\Q4 Project Data Sheet.xlsx" <-- Path for excel sheet on OneDrive :
#   Claims permission denied.

data = pd.read_excel(path)
data2 = {
   "CLUB":['Juventus', 'Inter', 'AC Milan', 'AS Roma', 'Lazio', 'Napoli', 'Genoa', 'Empoli','Lecce','Bolonga','Frosinone','Fiorentina', 'Atlanta','Hellas Verona','Torino', 'Monza','Sassoulo','Udinese','Salernitana','Cagliari'],
    "PTS":[46,50,43,41,40,32,12,16,21,54,32,21,32,41,44,54,29,70,7,35],
    "GD":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "MP":[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15]    
    }
'''
print (len(data2['CLUB']))
print (len(data2['PTS']))
print (len(data2['GD']))
print (len(data2['MP']))
'''
dataframe2=pd.DataFrame(data2)
#print (dataframe2)
# updating the column value/data 

dataframe2 = dataframe2.sort_values(by="PTS", ascending=True).reset_index(drop=True)
print (dataframe2)
print ("\n")
cols = ["CLUB", "PTS", "GD", "MP"]

# print (cols[0]) -> "CLUB"

col=cols[1]
print ("data ->")
print (dataframe2[col][5])

data['MP'] = data['MP'].replace({12:15}) 
  

# writing into the file 
#data.to_csv(r"C:\Users\samue\Downloads\Q4 Project Excel Data Spreadsheet.xlsx", index=False) 

#print(data)

#matches_played = data.MP
#goal_difference = data.GD
#total_points = data.PTS

#while True:
    
  #  chart_change = input(": ")

'''
chart = {'|-----Team------|': ['Juventus', 'Inter', 'AC Milan', 'AS Roma', 'Lazio', 'Napoli', 'Genoa', 'Empoli','Lecce','Bolonga','Frosinone','Fiorentina', 'Atlanta','Hellas Verona','Torino', 'Monza','Sassoulo','Udinese','Salernitana','Cagliari', ], '|PTS|': [14, 10, 9, 6, 5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 7, 8, 9, 20], '|GD|': [7, 8, 12, 1, 11, 1, 3, 4, 5, 6, 6, 7, 23, 5, 2, 4, 5, 23, 4, 2]}

standings_chart = pd.DataFrame(data=chart)

print (standings_chart)

row_count = standings_chart.shape[0]

print('\n' + "Number of Teams:")
print(row_count)

column_count = standings_chart.shape[1]

print('\n' + "Number of Categories:")
print(column_count)
    
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
