import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.parole = md.MultiDictionary()
        pass

    def handleSentence(self, txtIn, language):
        lista_finale = []
        text = replaceChars(txtIn)
        self.parole = self.parole.searchWord(text, language)
        for i in self.parole:
            if i._corretta == False:
                lista_finale.append(i)
        return lista_finale
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
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
    pass