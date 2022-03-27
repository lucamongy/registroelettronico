import json
from Studente import Studente
from Professore import Professore


class DBManager:

    @staticmethod
    def writeall(studentsList,professorsList,subjectsList):
        DBManager.swrite(studentsList)
        DBManager.pwrite(professorsList)
        DBManager.sbwrite(subjectsList)

    @staticmethod
    def sbwrite(subjectsList):
        with open('materie.dbs', 'w', encoding='utf-8') as db:
            for sb in subjectsList:
                json.dump(sb.todict(),db)
                db.write("\n")

    @staticmethod
    def pwrite(professorsList):
        with open('professori.dbs', 'w', encoding='utf-8') as db:
            for p in professorsList:
                json.dump(p.todict(),db)
                db.write("\n")

    @staticmethod
    def swrite(studentsList):
        with open('studenti.dbs', 'w', encoding='utf-8') as db:
            for s in studentsList:
                json.dump(s.todict(),db)
                db.write("\n")

    def pread(self):
        professorsList = []
        dictList = []
        with open('professori.dbs', 'r', encoding='utf-8') as db:
            for p in db.readlines():
                dictList.append(json.loads(p))
        for p in dictList:
            nome = p["nome"]
            cognome = p["cognome"]
            codice = p["codice"]
            materia = p["materia"]
            professorsList.append(Professore(nome,cognome,codice,materia))


    @staticmethod
    def sread():
        studentsList = []
        dictList = []
        with open('studenti.dbs', 'r', encoding='utf-8') as db:
            for s in db.readlines():
                dictList.append(json.loads(s))
        for s in dictList:
            nome = s["nome"]
            cognome = s["cognome"]
            cf = s["cf"]
            anno = int(s["anno"])
            sezione = s["sezione"]
            studentsList.append(Studente(nome,cognome,cf,anno,sezione))

        return studentsList