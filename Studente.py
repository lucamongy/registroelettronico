class Studente:

    def __init__(self, nome, cognome, cf='null', anno=0, sezione='null'):
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.anno = anno
        self.sezione = sezione

    def toDict(self):
        d = {
            "nome": self.nome,
            "cognome": self.cognome,
            "cf": self.cf,
            "anno": self.anno,
            "sezione": self.sezione}
        return d

    def __str__(self):
        s = f"- Nome: {self.nome}\n- Cognome: {self.cognome}"
        if self.cf != 'null':
            s += f"\n- Codice fiscale: {self.cf}"
        if self.anno != 0:
            s += f"\n- Anno: {self.anno}"
        if self.sezione != 'null':
            s += f"\n- Sezione: {self.sezione}"
        s += "\n--------------\n"

        return s