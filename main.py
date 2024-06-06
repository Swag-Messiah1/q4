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

file_path = r"C:\Users\samue\Downloads\---.xlsx"
#r"C:\Users\samue\Downloads\Q4 FInal Spreadsheet Data - For Project.xlsx"
#r"C:\Users\samue\OneDrive\Documents\Q4 Project Data Sheet.xlsx" <-- Path for excel sheet on OneDrive :
#   Claims permission denied.

data = pd.read_excel(file_path)
data2 = {
   "CLUB":['Juventus', 'Inter', 'AC Milan', 'AS Roma', 'Lazio', 'Napoli', 'Genoa', 'Empoli','Lecce','Bolonga','Frosinone','Fiorentina', 'Atalanta','Hellas Verona','Torino', 'Monza','Sassoulo','Udinese','Salernitana','Cagliari'],
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
#from termcolor import colored

#print(colored('hello', 'red'), colored('world', 'green'))

dataframe2=pd.DataFrame(data2)
dataframe2.to_excel(file_path)
print (dataframe2)
# updating the column value/data 

dataframe2 = dataframe2.sort_values(by="PTS", ascending=True).reset_index(drop=True)
#print (dataframe2)
#print ("\n")
cols = ["CLUB", "PTS", "GD", "MP"]

# print (cols[0]) -> "CLUB"
'''
print (f" %15s %3s %2s %2s" % ("CLUB", 'PTS', 'GD', 'MP'))
for index, row in dataframe2.iterrows():
    print(f" %15s %3s %2s %2s" % (row['CLUB'], row['PTS'], row["GD"], row["MP"]))
'''
col=cols[1]
print (f"The team you selected is ___ and it has {dataframe2[col][7]} PTS")
#print (f"{dataframe2[col][7]} PTS")

data['MP'] = data['MP'].replace({12:15}) 

dataframe2 [dataframe2.columns[0:3]]
'''
while True:
    ui1 = input("Type the number of the index of the team you want to select...")
#("Type the index number on the far left coloumn to display that teams number of points (PTS)")
    if ui1 == 0:
         print("You selected Salernitana")  
    if ui1 == 1:
         print("You selected Genoa") 
    if ui1 == 2:
         print("You selected Empoli") 
    if ui1 == 3:
        print("You selected Lecce")  
    if ui1 == 4:
        print("You selected Fiorentina") 
    if ui1 == 5:
        print("You selected Sassoulo") 
    if ui1 == 6:
        print("You selected Napoli") 
    if ui1 == 7:
        print("You selected Friosinone") 
    if ui1 == 8:
        print("You selected Atalanta") 
    if ui1 == 9:
        print("You selected Cagliari") 
    if ui1 == 10:
        print("You selected Lazio") 
    if ui1 == 11:
        print("You selected AS Roma") 
    if ui1 == 12:
        print("You selected Hellas Verona") 
    if ui1 == 13:
        print("You selected AC Milan")  
    if ui1 == 14:
        print("You selected Torino")  
    if ui1 == 15:
        print("You selected Juventus")  
    if ui1 == 16:
        print("You selected Inter")  
    if ui1 == 17:
        print("You selected Monza")  
    if ui1 == 18:
        print("You selected Bolonga")  
    if ui1 == 19:
        print("You selected Udinese")  
'''   


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
