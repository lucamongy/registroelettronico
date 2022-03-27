class Materia:

    def __init__(self, nome, codice,descrizione=""):
        self.nome = nome
        self.codice = codice
        self.descrizione = descrizione

    def todict(self):
        d = {
            "nome": self.nome,
            "codice": self.codice,
            "descrizione": self.descrizione}
        return d

    @staticmethod
    def inserimento():
        nome = input("Inserire nome: ")
        codice = input("Inserire codice: ")
        descrizione = input("Inserire descrizione (facoltativo): ")
        return Materia(nome,codice,descrizione)

    def __str__(self):
        s = f"----------\n- Codice Materia: {self.codice}\n- Nome: {self.nome}"
        if self.descrizione != "":
            s+= f"\n- Descrizione: {self.descrizione}"
        s += "\n----------"
        return s