import spellchecker



while(True):
    sc = spellchecker.SpellChecker()
    sc.printMenu()


    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        lista = sc.handleSentence(txtIn,"italian")
        print("Using Contains:")
        for i in lista:
            print(i._parola)
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        lista = sc.handleSentence(txtIn,"english")
        print("Using Contains:")
        for i in lista:
            print(i._parola)
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        lista = sc.handleSentence(txtIn,"spanish")
        print("Using Contains:")
        for i in lista:
            print(i._parola)
        continue

    if int(txtIn) == 4:
        break


