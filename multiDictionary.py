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
            if lista.__contains__(parola.lower()):
                parola = rw.RichWord(parola)
                parola._corretta = True
            else:
                parola = rw.RichWord(parola)
                parola._corretta = False
            lista2.append(parola)
        return lista2
        pass

    def searchWordLinear(self, words, language):
        lista = self.printDic(language)
        lista2 = []
        parole = words.split(" ")
        for parola in parole:
            corretta = False
            for i in lista:
                if parola.lower() == i.lower():
                    parola = rw.RichWord(parola)
                    parola._corretta = True
                    lista2.append(parola)
                    corretta = True
                    break
            if corretta == False:
                parola = rw.RichWord(parola)
                lista2.append(parola)
        return lista2
        pass

    def searchWordDichotomic(self, words, language):
        lista = self.printDic(language)
        lista2 = []
        parole = words.split(" ")
        for parola in parole:
            corretta = False
            if parola == lista[round(len(lista)/2)]:
                parola = rw.RichWord(parola)
                parola.corretta = True
            elif parola<lista[round(len(lista)/2)]:
                for i in range(round(len(lista)/2), 0, -1):
                    if parola == lista[i]:
                        parola = rw.RichWord(parola)
                        parola._corretta = True
                        lista2.append(parola)
                        corretta = True
                        break
                if corretta == False:
                    parola = rw.RichWord(parola)
                    lista2.append(parola)
            else:
                for i in range(round(len(lista)/2), len(lista)):
                    if parola == lista[i]:
                        parola = rw.RichWord(parola)
                        parola._corretta = True
                        lista2.append(parola)
                        corretta = True
                        break
                if corretta == False:
                    parola = rw.RichWord(parola)
                    lista2.append(parola)

        return lista2
        pass


