import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.lista_parole = d.Dictionary()
        pass

    def printDic(self, language):
        lista=[]
        if language=="italian":
            lista=self.lista_parole.loadDictionary("resources/Italian.txt")
        elif language=="english":
            lista=self.lista_parole.loadDictionary("resources/English.txt")
        elif language=="spanish":
            lista=self.lista_parole.loadDictionary("resources/Spanish.txt")
        self.lista_parole = lista
        return self.lista_parole

        pass

    def searchWord(self, words, language):
        lista = self.printDic(language)
        lista2 = []
        parole = words.split(" ")
        for parola in parole:
            if parola.lower() in lista:
                parola = rw.RichWord(parola)
                parola._corretta = True
            else:
                parola = rw.RichWord(parola)
                parola._corretta = False
            lista2.append(parola)
        return lista2
        pass


