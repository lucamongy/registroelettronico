import json

from Materia import Materia
from Studente import Studente
from Professore import Professore


class DBManager:

    @staticmethod
    def writeall(studentsList,professorsList,subjectsList):
        DBManager.swrite(studentsList)
        DBManager.pwrite(professorsList)
        DBManager.sbwrite(subjectsList)

    @staticmethod
    def readall():
        results = {}
        results["subjects"] = DBManager.sbread()
        results["professors"] = DBManager.pread()
        results["students"] = DBManager.sread()

        return results



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

    @staticmethod
    def sbread():
        subjectList = []
        dictList = []
        try:
            with open('materie.dbs', 'r+', encoding='utf-8') as db:
                for sb in db.readlines():
                    dictList.append(json.loads(sb))
        except(FileNotFoundError):
            print("File studenti inesistente.")
            return subjectList
        for p in dictList:
            nome = p["nome"]
            codice = p["codice"]
            descrizione = p["descrizione"]
            subjectList.append(Materia(nome,codice,descrizione))

        return subjectList

    @staticmethod
    def pread():
        professorsList = []
        dictList = []
        try:
            with open('professori.dbs', 'r+', encoding='utf-8') as db:
                for p in db.readlines():
                    dictList.append(json.loads(p))
        except(FileNotFoundError):
            print("File professori inesistente.")
            return professorsList
        for p in dictList:
            nome = p["nome"]
            cognome = p["cognome"]
            codice = p["codice"]
            materia = p["materia"]
            professorsList.append(Professore(nome,cognome,codice,materia))
        return professorsList

    @staticmethod
    def sread():
        studentsList = []
        dictList = []
        try:
            with open('studenti.dbs', 'r', encoding='utf-8') as db:
                for s in db.readlines():
                    dictList.append(json.loads(s))
        except(FileNotFoundError):
            print("File studenti inesistente.")
            return studentsList
        for s in dictList:
            nome = s["nome"]
            cognome = s["cognome"]
            cf = s["cf"]
            anno = int(s["anno"])
            sezione = s["sezione"]
            studentsList.append(Studente(nome,cognome,cf,anno,sezione))

        return studentsList