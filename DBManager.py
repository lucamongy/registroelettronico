import json
from Studente import Studente

class DBManager:

    @staticmethod
    def write(studentsList):
        with open('studenti.dbs', 'w', encoding='utf-8') as db:
            for s in studentsList:
                json.dump(s.toDict(),db)
                db.write("\n")

    @staticmethod
    def read():
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