"""
Quarter 4 Project Code

"""

'''
use append to add to a list - we need to sort list tho
'''
import pandas as pd


path = r"C:\Users\samue\Downloads\Q4 FInal Spreadsheet Data - For Project.xlsx"
#r"C:\Users\samue\OneDrive\Documents\Q4 Project Data Sheet.xlsx" <-- Path for excel sheet on OneDrive :
#   Claims permission denied.

data = pd.read_excel(path)

# updating the column value/data 
data['MP'] = data['MP'].replace({12:13}) 
  
# writing into the file 
data.to_csv(r"C:\Users\samue\Downloads\Q4 FInal Spreadsheet Data - For Project.xlsx", index=False) 

print(data)

matches_played = data.MP
goal_difference = data.GD
total_points = data.PTS

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

