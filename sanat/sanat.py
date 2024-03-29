from virheet import SanaError
import random

class Sanat:
    def __init__(self):
        self._sanat = []
        self._kaikkikirjaimet = None
        self._loydetyt = dict()
    def alusta(self, sanatiedosto='words.txt', minlen=3):
        try:
            with open(sanatiedosto, 'r', encoding='utf-8') as tdsto:
                luettu = [ row.strip() for row in tdsto if len(row) > minlen and row[0] != '#']
            self._sanat = luettu
        except IOError as e:
            raise SanaError("Tiedoston '{}' lukeminen epäonnistui: {1}".format(sanatiedosto, str(e)))
    def alusta_sanalla(self, kaikkikirjaimet):
        def filtteriehto(s):
            if len(s) > len(kaikkikirjaimet): return False
            tmp = list(kaikkikirjaimet)
            try:
                for k in s:
                    tmp.remove(k)
                return True
            except ValueError:
                return False
        self._kaikkikirjaimet = kaikkikirjaimet
        if kaikkikirjaimet in self._loydetyt:
            return self._loydetyt[kaikkikirjaimet]
        loydetyt = list(filter(filtteriehto, self._sanat))
        self._loydetyt[kaikkikirjaimet] = loydetyt
        return loydetyt
    def onko_oikea(self, ehdokas):
        if not self._kaikkikirjaimet:
            raise SanaError('Ei ole alustettu sanalla jossa kaikki käytössä olevat kirjaimet')
        return ehdokas in self._loydetyt[self._kaikkikirjaimet]
    def satunnainen_sana(self, minimipituus=6, maxpituus=8):
        loydetyt = list(filter(lambda s: len(s) >= minimipituus and len(s) <= maxpituus, self._sanat))
        valittusana = loydetyt[random.randint(0, len(loydetyt))]
        self.alusta_sanalla(valittusana)
        return valittusana
    def satunnaiset_kirjaimet(self, minimipituus=6, maxpituus=8, **kwargs):
        if ('sana' in kwargs):
            sana = kwargs['sana']
        else:
            sana = self.satunnainen_sana()
        sanalistana = list(sana)
        random.shuffle(sanalistana)
        ansa = "".join(sanalistana)
        return ansa
