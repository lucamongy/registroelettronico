class Professore:

    def __init__(self,nome,cognome,codice,materia):
        self.nome = nome
        self.cognome = cognome
        self.codice = codice
        self.materia = materia

    def todict(self):
        d = {
            "nome": self.nome,
            "cognome": self.cognome,
            "codice": self.codice,
            "materia": self.materia
        }
        return d

    @staticmethod
    def inserimento():
        nome = input("Inserire nome: ")
        cognome = input("Inserire cognome: ")
        codice = input("Inserire codice: ")
        materia = input("Inserire materia: ")
        return Professore(nome,cognome,codice,materia)

    def __str__(self):
        s = f"----------\n- Codice: {self.codice}\n- Nome: {self.nome}\n- Cognome: {self.cognome}\n- Materia: {self.materia}\n----------\n"
        return s