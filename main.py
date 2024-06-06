
"""
Quarter 4 Project Code (MORE PRECISE)

"""

import pandas as pd

#Path 
file_path = r"C:\Users\samue\Downloads\---.xlsx"
data = pd.read_excel(file_path)

#Greeting!
print("\nWelcome to the the Serie A Standings Chart Directory! \nType 20 as the team index anytime to stop the directory \n")

#Chart Data
data_2 = {
   "CLUB":['Juventus', 'Inter', 'AC Milan', 'AS Roma', 'Lazio', 'Napoli', 'Genoa', 'Empoli','Lecce','Bolonga','Frosinone','Fiorentina', 'Atalanta','Hellas Verona','Torino', 'Monza','Sassoulo','Udinese','Salernitana','Cagliari'],
    "PTS":[46,50,43,41,40,32,12,16,21,54,32,21,32,41,44,54,29,70,7,35],
    "GD":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "MP":[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15]    
    }

dataframe2=pd.DataFrame(data_2)
dataframe2.to_excel(file_path)
dataframe2 [dataframe2.columns[0:3]]

# updating/changing the column values/data 
dataframe2.at[2, 'MP'] =7
dataframe2.at[2, 'PTS'] =7 #<-- DONT MESS WITH THIS RIGHT NOW

data['MP'] = data['MP'].replace({12:15})

#Sorting the Data
dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
print(dataframe2)

##
cols = ["CLUB", "PTS", "GD", "MP"]
col=cols[1]

#User_Input
while True:
    ui = int(input("Type the number of the index of the team you want to select..."))
    if ui == 0:
        club = "Udinese"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 1:
        club = "Bolonga"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 2:
        club = "Monza"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 3:
        club = "Inter"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 4:
        club = "Juventus"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 5:
        club = "Torino"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 6:
        club = "AS Roma"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 7:
        club = "Hellas Verona"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 8:
        club = "Lazio"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 9:
        club = "Cagliari"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 10:
        club = "Atalanta"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 11:
        club = "Napoli"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 12:
        club = "Friosinone"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 13:
        club = "Sassoulo"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 14:
        club = "Lecce"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 15:
        club = "Fiorentina"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 16:
        club = "Empoli"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 17:
        club = "Genoa"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 18:
        club = "AC Milan"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 19:
        club = "Salernitana"
        print (f"\nThe team you selected is {club} and they have {dataframe2[col][ui]} PTS \n")
        dataframe2 = dataframe2.sort_values(by="PTS", ascending=False).reset_index(drop=True)
        print(dataframe2)
    if ui == 20:
        print ("You have stopped the Serie A Standings Chart Directory!")
        break
  

   


'''
#Formatting:
    
print (f" %15s %3s %2s %2s" % ("CLUB", 'PTS', 'GD', 'MP'))
for index, row in dataframe2.iterrows():
    print(f" %15s %3s %2s %2s" % (row['CLUB'], row['PTS'], row["GD"], row["MP"]))
    
from termcolor import colored
print(colored('hello', 'red'), colored('world', 'green'))

'''
