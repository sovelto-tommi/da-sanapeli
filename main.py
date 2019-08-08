from sanat.sanat import Sanat

if __name__ == '__main__':
    print("Mainissa")

    sanat = Sanat()
    sanat.alusta()
    osuneet = sanat.alusta_sanalla("kerala")
    print(osuneet)
    ehdokkaat = ['ale', 'rakel', 'eioo', 'keralaa']
    # ale on, rakel matchaisi mutta ei ole sanalistassa,
    for e in ehdokkaat:
        print("'{0} ehdotus, tulos: {1}".format(e, sanat.onko_oikea(e)))

