import spellchecker



while(True):
    sc = spellchecker.SpellChecker()
    sc.printMenu()


    txtIn = input("-")
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        lista = sc.handleSentence(txtIn,"italian")
        print(f"Using Contains:\nTempo impiegato {lista[0][1]} secondi")
        for i in lista[0][0]:
            print(i)
        print()
        print(f"Using Linear:\nTempo impiegato {lista[1][1]} secondi")
        for i in lista[1][0]:
            print(i)
        print()
        print(f"Using Dichotomic:\nTempo impiegato {lista[2][1]} secondi")
        for i in lista[2][0]:
            print(i)
        print()

        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        lista = sc.handleSentence(txtIn, "italian")
        print(f"Using Contains:\nTempo impiegato {lista[0][1]} secondi")
        for i in lista[0][0]:
            print(i)
        print()
        print(f"Using Linear:\nTempo impiegato {lista[1][1]} secondi")
        for i in lista[1][0]:
            print(i)
        print()
        print(f"Using Dichotomic:\nTempo impiegato {lista[2][1]} secondi")
        for i in lista[2][0]:
            print(i)
        print()
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        lista= sc.handleSentence(txtIn, "italian")
        print(f"Using Contains:\nTempo impiegato {lista[0][1]} secondi")
        for i in lista[0][0]:
            print(i)
        print()
        print(f"Using Linear:\nTempo impiegato {lista[1][1]} secondi")
        for i in lista[1][0]:
            print(i)
        print()
        print(f"Using Dichotomic:\nTempo impiegato {lista[2][1]} secondi")
        for i in lista[2][0]:
            print(i)
        print()
        continue

    if int(txtIn) == 4:
        break


