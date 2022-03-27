from Studente import Studente
from DBManager import DBManager
from Professore import Professore
from Materia import Materia

studentsList = []
subjectsList = []
professorsList = []

menu = "\n\n\n--- Menu' ---\n1- Modalità inserimento\n2- Modalità Lista\n3- Inserisci nuovo studente\n-------------"
insmenu = "\n\n\n--- Menu' ---\n1- Inserisci nuova materia\n2- Inserisci nuovo professore\n3- Inserisci nuovo studente\n-------------"
listmenu = "\n\n\n--- Menu' ---\n1- Mostra lista studenti\n2- Mostra lista materie\n3- Mostra lista professori\n-------------"
cmd = ''
print(menu)

while cmd != 'q':
    cmd = input("Inserire operazione (q per uscire, m per menu'):\t").lower()
    if cmd == '1':
        print(insmenu)
        cmd = input("Inserire operazione (q per uscire, m per menu'):\t").lower()
        if cmd == '1':
            subjectsList.append(Materia.inserimento())
        elif cmd == '2':
            professorsList.append(Professore.inserimento())
        elif cmd == '3':
            studentsList.append(Studente.inserimento())
        elif cmd == 'q':
            cmd = ''
    elif cmd == '2':
        print(listmenu)
        cmd = input("Inserire operazione (q per uscire, m per menu'):\t").lower()
        if cmd == '1':
            for s in studentsList:
                print(s)
        elif cmd == '2':
            for s in subjectsList:
                print(s)
        elif cmd == '3':
            for p in professorsList:
                print(p)
        elif cmd == 'q':
            cmd = ''
    elif cmd == 'm':
        print(menu)





subjectsList.append(Materia("Matematica","MT255","Matematica"))

professorsList.append(Professore("John","Smith","1232","MT255"))

studentsList.append(Studente("Luca","Mongiardo"))
studentsList.append(Studente("Johnny","Sins"))

DBManager.writeall(studentsList,professorsList,subjectsList)




"""
s = Studente("Luca","Mongiardo") #prova studente
print(f"prima prova:\n{s}\n\n") #prova override str
print(s.getVoti())
s.addVoto("storia",10)
print(s.getVoti())
s.setMateria("storia",5)
print(s.getVoti())
s.addVoto("storia",10)
print(s.getVoti())
"""




''''
#lista studenti
studenti = []
studenti.append(Studente("John","Smith","SMTJHN65D04F257P"))
studenti.append(Studente("Luca","Mongiardo","MNGLCU01P23D122C",5,'I'))


#database
DBManager.write(studenti) #scrivo
sl = DBManager.read()  #leggo e salvo in studenti

#stampo gli studenti per confrontarli
for i in range(0,len(studenti)):
    print(f"lista1:\n{studenti[i]}")
    print(f"lista2:\n{sl[i]}")
'''

