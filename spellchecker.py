import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.parole = md.MultiDictionary()
        pass

    def handleSentence(self, txtIn, language):
        lista = []
        text = replaceChars(txtIn)
        start_time = time.time()
        lista_finale = []
        risultato = self.parole.searchWord(text, language)
        for i in risultato:
            if i._corretta == False:
                lista_finale.append(i)
        end_time = time.time()
        intervallo_tempo_contains = end_time-start_time
        lista.append((lista_finale, intervallo_tempo_contains))

        self.parole = md.MultiDictionary()
        start_time = time.time()
        lista_finale = []
        risultato = self.parole.searchWordLinear(text, language)
        for i in risultato:
            if i._corretta == False:
                lista_finale.append(i)
        end_time = time.time()
        intervallo_tempo_lineare = end_time-start_time
        lista.append((lista_finale, intervallo_tempo_lineare))

        self.parole = md.MultiDictionary()
        start_time = time.time()
        lista_finale = []
        risultato = self.parole.searchWordDichotomic(text, language)
        for i in risultato:
            if i._corretta == False:
                lista_finale.append(i)
        end_time = time.time()
        intervallo_tempo_lineare = end_time - start_time
        lista.append((lista_finale, intervallo_tempo_lineare))


        return lista
        pass

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.?!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
    pass