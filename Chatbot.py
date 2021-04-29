


def Abfrage():
    a = input("Wie ist dein Name? ")



    print("Hallo {}".format(a))

    b = input("{} wie Alt bist du?".format(a))
    c = int(b)
    if c < 5:
        print("Du Huan geh mal zur Schule")
    elif c > 100:
        print("{} Wir sind keine (Jugendfreie Seite), du kannst uns vertrauen (zwinker)".format(a))
    elif c > 5 and c < 100:
        d = input("Noice da hat dein Immunsystem gute Arbeit geleistet. Wie geht´s dir? ")
        if d == "gut":
            print("schön schön")
        else:
            print("Schade. Warum geht es dir Heute nur {}?".format(d))












def Strat():
    Abfrage()
    Strat()
Strat()





















































