from sanat.sanat import Sanat

def run():
    print("Tervetuloa pelaamaan!\n")
    sanat = Sanat()
    sanat.alusta()
    # virhekäsittely puuttuu!!!
    montako = int(input("Montako sanaa pitää löytää / kierros? "))

    while True:
        while True:
            kirjaimet = sanat.satunnaiset_kirjaimet()
            if len(sanat.alusta_sanalla(kirjaimet)) > montako:
                break
        pelaa_kierros(sanat, kirjaimet, montako)
        vastaus = input("\nUusi kierros? [K/e]")
        if vastaus.lower() == 'e':
            break
        print("Kiva juttu, jatketaan")

def pelaa_kierros(sanat, kirjaimet, montako=5):
    print("Koita löytää {0} sanaa seuraavista kirjaimista:".format(montako))
    print("\t",  "".join(kirjaimet.split()))
    oikeita = 0
    ehdotetut = []
    while True:
        ehdokas = input("> ")
        if ehdokas in ehdotetut:
            print("Olet jo ehdottanut sanaa '{0}', ei käy".format(ehdokas))
            continue
        ehdotetut.append(ehdokas)
        if sanat.onko_oikea(ehdokas):
            oikeita += 1
            print("Oikein, löydettyjä sanoja {0}/{1}".format(oikeita, montako))
            if oikeita >= montako:
                break
        else:
            print("Ei osunut, löydettyjä sanoja {0}/{1}".format(oikeita, montako))

if __name__ == '__main__':
    run()
