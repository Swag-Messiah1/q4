#(STILL WORKING ON LEARNING THE FORMAT (CSV)
"""
Quarter 4 Project Code

"""

'''
use append to add to a list - we need to sort list tho
'''
import csv

scoresList = open("path", "r")

csvReader = csv.reader(scoresList)
header = csvReader.next()
stadiumIndex = header.index("Stadium")
teamIndex = header.index("Team")
goalsagainstIndex = header.index("GoalsAgainst")
goalsforIndex = header.index("Goalsfor")

'''

serie_a_teams = {
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
    }

def Juventus():

    
def Inter():

    
def AC_Milan():

    
def Roma():

    
def Napoli():

    
def Atalanta():

    
def Lazio():

    
def Bolonga():

    
def Fiorentina():

    
def Genoa():

    
def Monza():

    
def Torino():

    
def Udinese():

    
def Lecce():  
    
    
def Hellas_Verona():

    
def Empoli():
    
    
def Frosinone():
    
    
def Cagliari():
    
    
def Sassoulo():
    
    
def Salernitana():
    
    
'''    
    
def Sassoulo():
    
    
def Salernitana():
