from Studente import Studente
from DBManager import DBManager


s = Studente("Luca","Mongiardo") #prova studente
print(f"prima prova:\n{s}\n\n") #prova override str


#lista studenti
studenti = []
studenti.append(Studente("Simone","Mongiardo"))
studenti.append(Studente("John","Smith","SMTJHN65D04F257P"))
studenti.append(Studente("Luca","Mongiardo","MNGLCU01P23D122C",5,'I'))


#database
DBManager.write(studenti) #scrivo
sl = DBManager.read()  #leggo e salvo in studenti

#stampo gli studenti per confrontarli
for i in range(0,len(studenti)):
    print(f"lista1:\n{studenti[i]}")
    print(f"lista2:\n{sl[i]}")