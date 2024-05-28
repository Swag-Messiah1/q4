"""
Quarter 4 Project Code

"""

'''
use append to add to a list - we need to sort list tho
'''

import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl open load_workbook

path = r"C:\Users\samue\Downloads\---.xlsx"
#r"C:\Users\samue\Downloads\Q4 FInal Spreadsheet Data - For Project.xlsx"
#r"C:\Users\samue\OneDrive\Documents\Q4 Project Data Sheet.xlsx" <-- Path for excel sheet on OneDrive :
#   Claims permission denied.

data = pd.read_excel(path)
data2 = {
    "CLUB":['Juventus', 'Inter', 'AC Milan', 'AS Roma', 'Lazio', 'Napoli', 'Genoa', 'Empoli','Lecce','Bolonga','Frosinone','Fiorentina', 'Atlanta','Hellas Verona','Torino', 'Monza','Sassoulo','Udinese','Salernitana','Cagliari'],
    "PTS":[46,50,43,41,40,32,12,16,21,54,32,21,32,41,44,54,29,70,7,35],
    "GD":[],
    "MP":[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15]
    
    }
dataframe2=pd.DataFrame(data2)
print (dataframe2)

# updating the column value/data 

data['MP'] = data['MP'].replace({12:14}) 
  

# writing into the file 
data.to_csv(r"C:\Users\samue\Downloads\Q4 Project Excel Data Spreadsheet.xlsx", index=False) 

print(data)

#matches_played = data.MP
#goal_difference = data.GD
#total_points = data.PTS

#while True:
    
  #  chart_change = input(": ")


#while True:
    
  #  chart_change = input(": ")

'''
Clubs (Teams) List:
    
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

