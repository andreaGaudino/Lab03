class Dictionary:
    def __init__(self):
        self._dict = []
        pass

    def loadDictionary(self,path):
        with open(path, "r") as liguaggio:
            righe = liguaggio.readlines()
            for i in righe:
                self._dict.append(i.strip("\n").lower())
        return self._dict
        pass

    def printAll(self):
        for i in self._dict:
            print(i)
        pass


    @property
    def dict(self):
        return self._dict