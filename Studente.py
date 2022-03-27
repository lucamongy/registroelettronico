class Studente:

    def __init__(self, nome, cognome, cf='null', anno=0, sezione='null'):
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.anno = anno
        self.sezione = sezione
        self.voti = {}

    def addVoto(self,materia,voto):
        if materia in self.voti:
            self.voti[materia].append(voto)
            return 0
        return 1

    def setMateria(self,materia,voto=0):
        if voto == 0:
            self.voti[materia] = []
        else:
            self.voti[materia] = [voto]

    def loadVoti(self,voti):
        self.voti = voti

    def getVoti(self):
        return self.voti

    def todict(self):
        d = {
            "nome": self.nome,
            "cognome": self.cognome,
            "cf": self.cf,
            "anno": self.anno,
            "sezione": self.sezione}
        return d

    @staticmethod
    def inserimento():
        nome = input("Inserire nome: ")
        cognome = input("Inserire cognome: ")
        cf = input("Inserire codice fiscale (facoltativo): ")
        anno = int(input("Inserire anno (facoltativo): "))
        if anno == "":
            anno = 0
        sezione = input("Inserire sezione (facoltativo): ")
        return Studente(nome,cognome,cf,anno,sezione)

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