import random

class Serija_Iger:
    def __init__(self, igralec1, igralec2, tocke_za_zmago = 100):
        self.igralec1 = igralec1
        self.igralec2 = igralec2
        self.igralci = [igralec1, igralec2]
        self.aktivna_igra = None
        self.koncane_igre = []
        self.tocke_za_zmago = tocke_za_zmago
    
    def nova_igra(self):
        self.aktivna_igra = Igra(self.igralec1, self.igralec2)

    def je_konec(self):
        for igralec in self.igralci:
            if igralec.skupne_tocke >= self.tocke_za_zmago:
                return True
        return False

    def vrni_zmagovalca(self):
        for igralec in self.igralci:
            if igralec.skupne_tocke >= self.tocke_za_zmago:
                self.zmagovalec = igralec
                return igralec
        
class Igra:
    def __init__(self, igralec1, igralec2):
        self.igralci = [igralec1, igralec2]
        self.igralec1 = igralec1
        self.igralec2 = igralec2
        self.igralec_na_potezi = None
        for igralec in self.igralci:
            igralec.nova_igra()
        self.igrane_domine = Igrane_domine([])
        self.nerazdeljene_domine = [Domino(n,i) for n in range(6,-1,-1) for i in range(n,-1,-1)]
        self.poteze = []
        self.koncana = False

    ########################################################################################################
    def zacetna_poteza(self):
        for n in range(6,-1,-1):
            for igralec in self.igralci:
                for domino in igralec.domine:
                    if domino == Domino(n,n):
                        return Poteza(Domino(n,n), "S", igralec)
        for i in range(6,-1,-1):
            for n in range(i - 1,-1,-1):
                for igralec in self.igralci:
                    for domino in igralec.domine:
                        if domino == Domino(i,n):
                            return Poteza(Domino(i,n),"S",igralec)

    def razdeli(self):
        for igralec in self.igralci:
            for _ in range(7):
                igralec.dodaj_domino(self.nakljucna_iz_nerazdeljenih())

    def nakljucna_iz_nerazdeljenih(self):
        nakljucna_domina = random.choice(self.nerazdeljene_domine)
        self.nerazdeljene_domine.remove(nakljucna_domina)
        return nakljucna_domina

    def določi_igralca_na_potezi(self,igralec):
        self.igralec_na_potezi = igralec

    def naslednji_na_potezi(self):
        self.igralec_na_potezi = self.igralec_na_potezi.nasprotnik(self)

    def poteza(self,poteza):
        poteza.igralec.poteza(self.igrane_domine,poteza)
        self.poteze.append(poteza)
        self.naslednji_na_potezi()

    def nakljucna_poteza(self):
        poteza = self.igralec_na_potezi.nakljucna_poteza(self.igrane_domine)
        self.poteze.append(poteza)
        self.naslednji_na_potezi()
        return poteza

    def dodaj_domino(self):
        self.igralec_na_potezi.dodaj_domino(self.nakljucna_iz_nerazdeljenih())

    ###########################################################################################################
    
    def število_potez(self,stran = ""):
        if stran == "":
            return len(self.poteze)
        elif stran == "L" or stran == "D":
            stevilo_potez = 0
            for poteza in self.poteze:
                if poteza.stran == stran:
                    stevilo_potez += 1
            return stevilo_potez
        else:
            return 0

    def zaporedna_poteza(self,zaporedna_poteza):
        število = 0
        if zaporedna_poteza.stran == "S":
            return število
        else:
            for poteza in self.poteze:
                if poteza != zaporedna_poteza:
                    if poteza.stran == zaporedna_poteza.stran:
                        število += 1
                elif poteza == zaporedna_poteza:
                    break
            return število + 1

    def zadnja_poteza(self,stran = ""):
        if stran == "":
            return self.poteze[-1]
        elif stran == "L" or stran == "D":
            stranske_poteze = []
            for poteza in self.poteze:
                if poteza.stran == stran:
                    stranske_poteze.append(poteza)
            return stranske_poteze[-1]
            
    ###########################################################################################################

    def je_konec_igre(self):
        if len(self.igralec1.domine) == 0 or len(self.igralec2.domine) == 0:
            return True
        elif len(self.nerazdeljene_domine) == 0:
            moznepoteze1 = self.igralec1.mozne_poteze(self.igrane_domine)
            moznepoteze2 = self.igralec2.mozne_poteze(self.igrane_domine)
            if len(moznepoteze1) == 0 and len(moznepoteze2) == 0:
                return True
        return False

    def je_kapikua(self):
        if len(self.igralec1.domine) == 0 or len(self.igralec2.domine) == 0:
            igrane_brez_zadnje = self.igrane_domine.brez_zadnje_poteze(self)
            domino = {"L": self.zadnja_poteza().domino.leve_pike, "D": self.poteze[-1].domino.desne_pike}
            igrane = {"L": igrane_brez_zadnje.leva_stran, "D": igrane_brez_zadnje.desna_stran}
            if igrane["L"] == igrane["D"]:
                return igrane["L"] == domino["L"] and igrane["D"] == domino["D"]
            elif domino["L"] == igrane["L"] and domino["D"] == igrane["D"]:
                return True
            elif domino["L"] == igrane["D"] and domino["D"] == igrane["L"]:
                return True
        return False

    def vrni_zmagovalca(self):
        for igralec in self.igralci:
            if len(igralec.domine) == 0:
                return igralec
        if self.igralec1.število_pik() > self.igralec2.število_pik():
            return self.igralec2
        elif self.igralec1.število_pik() < self.igralec2.število_pik():
            return self.igralec1
        elif self.igralec1.število_pik() == self.igralec2.število_pik():
            return self.zadnja_poteza().igralec

    def vrni_koncne_tocke(self):
        sestevek = 0
        for igralec in self.igralci:
            sestevek += igralec.število_pik()
        return sestevek

    def konec_igre(self, serija):
        serija.koncane_igre.append(self)
        serija.aktivna_igra = None
        self.koncana = True
        self.zmagovalec = self.vrni_zmagovalca()
        self.koncne_tocke = self.vrni_koncne_tocke()
        for igralec in self.igralci:
            igralec.konec_igre()
        if self.je_kapikua():
            self.koncne_tocke += 25
            self.kapikua = True
        else:
            self.kapikua = False

    ##############################################################################################################       
    
    def določi_design(self):
        self.design = Igra_design()

class Igrane_domine:
    def __init__(self,igrane = []):
        self.igrane = igrane
        if len(self.igrane) == 0:
            self.leva_stran = None
            self.desna_stran = None
        else:
            self.leva_stran = self.igrane[0][0]
            self.desna_stran = self.igrane[-1][1]

    def __repr__(self):
        return self.igrane

    def __str__(self):
        polje = ''
        for domino in self.igrane:
            polje += '[{}|{}]'.format(domino[0],domino[1])
        return polje
    
    ##########################################################################################################
    def druga_stran(self,stran):
        if stran == "L":
            return "D"
        elif stran == "D":
            return "L"

    def stran(self,stran):
        if stran == "L":
            return self.leva_stran
        elif stran == "D":
            return self.desna_stran

    def določi_stran(self):
            self.leva_stran = self.igrane[0][0]
            self.desna_stran = self.igrane[-1][1]

    def dodaj_prvo(self,domino):
        self.igrane.append(domino.domino)
        self.leva_stran = domino.leve_pike
        self.desna_stran = domino.desne_pike

    def dodaj_k_igranim(self,stran,domino_array):
        if stran == "L":
            self.igrane.insert(0,domino_array)
        elif stran == "D":
            self.igrane.append(domino_array)

    def dodaj_na_stran(self,domino,stran):
        if domino.stranske_pike(stran) == self.stran(stran):
            self.dodaj_k_igranim(stran,domino.obrnjeno_domino)
            self.določi_stran()     
        elif domino.stranske_pike(self.druga_stran(stran)) == self.stran(stran):
            self.dodaj_k_igranim(stran,domino.domino)
            self.določi_stran()  

    def se_lahko_doda_na_stran(self,domino,stran):
        return domino.stranske_pike(stran) == self.stran(stran) or domino.stranske_pike(self.druga_stran(stran)) == self.stran(stran)

    def se_lahko_doda_na_obeh(self,domino):
        return self.se_lahko_doda_na_stran(domino,"L") and self.se_lahko_doda_na_stran(domino,"D")
    
    def je_prava_domina(self,domina):
        if domina.leve_pike == self.leva_stran:
            return True
        elif domina.leve_pike == self.desna_stran:
            return True
        elif domina.desne_pike == self.leva_stran:
            return True
        elif domina.desne_pike == self.desna_stran:
            return True
        return False

    def je_prava_poteza(self,poteza):
        return self.se_lahko_doda_na_stran(poteza.domino,poteza.stran)

    def je_treba_obrnit(self,stran,domino):
        return domino.stranske_pike(stran) == self.stran(stran)
    
    def je_obrnjeno(self,domino):
        for domina in self.igrane:
            if domino.domino == domina:
                return False
            elif domino.obrnjeno_domino == domina:
                return True

    def brez_zadnje_poteze(self,igra):
        if igra.zadnja_poteza().stran == "L":
            igrane_domine = []
            for n in range(1,len(self.igrane)):
                igrane_domine.append(self.igrane[n])
            return Igrane_domine(igrane_domine)
        elif igra.zadnja_poteza().stran == "D":
            igrane_domine = []
            for n in range(len(self.igrane)-1):
                igrane_domine.append(self.igrane[n])
            return Igrane_domine(igrane_domine)
    
class Igralec:
    def __init__(self,ime = "Računalnik"):
        self.domine = []
        self.ime = ime
        self.skupne_tocke = 0
        self.poteze = []
        self.domine_koncanih_iger = []

    def __repr__(self):
        return self.ime

    def __str__(self):
        return self.ime

    ###########################################################################################################

    def nova_igra(self):
        self.domine = []
        self.poteze = []

    def število_pik(self):
        število_pik = 0
        for domino in self.domine:
            število_pik += domino.pike
        return število_pik

    def število_domin(self):
        return len(self.domine)

    def nasprotnik(self,igra):
        if self == igra.igralec1:
            return igra.igralec2
        elif self == igra.igralec2:
            return igra.igralec1

    def naključno_domino(self):
        return random.choice(self.domine)
        
    def zadnje_domino(self):
        return self.domine[self.število_domin() -1] 

    def dodaj_domino(self,domino):
        self.domine.append(domino)

    def poteza(self,igrane_domine,poteza):
        if poteza.stran == "S":
            igrane_domine.dodaj_prvo(poteza.domino)
        else:
            igrane_domine.dodaj_na_stran(poteza.domino,poteza.stran)
        self.poteze.append(poteza)
        self.odstrani_domino(poteza.domino)

    def nakljucna_poteza(self,igrane_domine):
        mozne_poteze = self.mozne_poteze(igrane_domine)
        nakljucna_poteza = random.choice(mozne_poteze)
        igrane_domine.dodaj_na_stran(nakljucna_poteza.domino,nakljucna_poteza.stran)
        self.odstrani_domino(nakljucna_poteza.domino)
        return nakljucna_poteza

    def odstrani_domino(self,domino):
        for domina in self.domine:
            if domina == domino:
                self.domine.remove(domina)

    def razpolozljive_domine(self):
        razpolozljive_domine = []
        for domino in self.domine:
            razpolozljive_domine.append(domino)
        return razpolozljive_domine

    def mozne_poteze(self,igrane_domine):
        mozne_poteze = []
        for domino in self.domine:
            for stran in ["L","D"]:
                if igrane_domine.se_lahko_doda_na_stran(domino,stran):
                    mozne_poteze.append(Poteza(domino,stran,self))
        return mozne_poteze

    def število_moznih_potez(self,igrane_domine):
        return len(self.mozne_poteze(igrane_domine))

    def tocke_po_zmagi(self,stevilo_tock):
        self.skupne_tocke += int(stevilo_tock)
    
    def konec_igre(self):
        self.domine_koncanih_iger.append(self.domine)

class Poteza:
    def __init__(self,domino,stran,igralec):
        self.domino = domino
        self.stran = stran
        self.igralec = igralec

    ###################################################################################################

    def določi_design(self,igra):
        self.design = Poteza_design(igra,self)


class Domino:
    def __init__(self,leve_pike, desne_pike):
        self.leve_pike = leve_pike
        self.desne_pike = desne_pike
        self.domino = (leve_pike,desne_pike)
        self.obrnjeno_domino = (desne_pike, leve_pike)
        self.pike = leve_pike + desne_pike

    def __eq__(self,other):
        return self.domino == other.domino

    def __repr__(self):
        return '({},{})'.format(self.leve_pike, self.desne_pike)
    
    def ___str___(self):
        return '({},{})'.format(self.leve_pike, self.desne_pike)

    ########################################################################################################

    def stranske_pike(self,stran):
        if stran == "L":
            return self.leve_pike
        elif stran == "D":
            return self.desne_pike

    def je_dvojna(self):
        if self.leve_pike == self.desne_pike:
            return True
        else:
            return False

    def slika(self):
        return str(self) + '.jpg'

class Igra_design:
    def __init__(self,width = 9, height = 20):
        self.width = width
        self.height = height
        self.določi_postavitev()
        self.določi_rotacijo()
        self.določi_začetne_pozicije()
        self.določi_left()
        self.določi_top()

    def določi_postavitev(self):
        self.leva_postavitev =  ["h" for _ in range(5)] + ["v" for _ in range(2)] + ["h" for _ in range(9)] + ["v"] + ["h" for _ in range(8)]
        self.desna_postavitev = ["h" for _ in range(5)] + ["v" for _ in range(2)] + ["h" for _ in range(10)] + ["v" for _ in range(6)] 

    def določi_rotacijo(self):
        self.leva_rotacija = [False for _ in range(5)] + [True for _ in range(11)] + [False for _ in range(8)]
        self.desna_rotacija = [False for _ in range(5)] + [True for _ in range(12)] + [False for _ in range(6)]

    def določi_začetne_pozicije(self):
        self.zacetni_left = 52 - self.width / 2
        self.desni_left = self.zacetni_left + self.width * 4 + self.width
        self.levi_left = self.zacetni_left - self.width * 4
        self.zacetni_top = 50 - self.height / 2
        self.zgornji_top = self.zacetni_top - self.height - self.height / 2
        self.spodnji_top = self.zacetni_top + self.height * 2

    def določi_left(self):
        self.left_levo = [self.zacetni_left] + [self.zacetni_left - self.width * n for n in range(1,5)] + [self.levi_left for _ in range(2)] + [self.levi_left + self.width / 2 + n * self.width for n in range(9)] + [self.desni_left] + [self.desni_left - n * self.width for n in range(1,9)]
        self.left_desno = [self.zacetni_left] + [self.zacetni_left + self.width * n for n in range(1,5)] + [self.desni_left for _ in range(2)] + [self.desni_left - self.width * n for n in range(1,11)] + [self.levi_left - self.width for _ in range(5)]

    def določi_top(self):
        self.top_levo = [self.zacetni_top for _ in range(5)] + [self.zacetni_top + self.height / 2 + n * self.height for n in range(2)] + [self.spodnji_top for _ in range(9)] + [self.spodnji_top - self.height for _ in range(7)]
        self.top_desno = [self.zacetni_top for _ in range(5)] + [self.zacetni_top - self.height / 2 - n * self.height for n in range(2)] + [self.zgornji_top for _ in range(10)] + [self.zgornji_top + self.height / 2 + n * self.height for n in range(6)] 

class Poteza_design:
    def __init__(self,igra,poteza):
        zaporedna_poteza = igra.zaporedna_poteza(poteza)
        self.rotate = 0
        if poteza.stran == "S" or poteza.stran == "L":
            self.postavitev = igra.design.leva_postavitev[zaporedna_poteza]
            if igra.design.leva_rotacija[zaporedna_poteza] and not igra.igrane_domine.je_obrnjeno(poteza.domino):
                self.rotate = 180
            elif not igra.design.leva_rotacija[zaporedna_poteza] and igra.igrane_domine.je_obrnjeno(poteza.domino):
                self.rotate = 180
        elif poteza.stran == "D":
            self.postavitev = igra.design.desna_postavitev[zaporedna_poteza]
            if igra.design.desna_rotacija[zaporedna_poteza] and not igra.igrane_domine.je_obrnjeno(poteza.domino):
                self.rotate = 180
            elif not igra.design.desna_rotacija[zaporedna_poteza] and igra.igrane_domine.je_obrnjeno(poteza.domino):
                self.rotate = 180
        self.dimenzije(igra.design.width,igra.design.height)
        if self.postavitev == "h":
            self.slika = "({},{}).jpg".format(poteza.domino.leve_pike,poteza.domino.desne_pike)
        elif self.postavitev == "v":
            self.slika = "v-({},{}).jpg".format(poteza.domino.leve_pike,poteza.domino.desne_pike)
        
        if poteza.stran == "S":
            self.left = igra.design.left_levo[zaporedna_poteza]
            self.top = igra.design.top_levo[zaporedna_poteza]
        elif poteza.stran == "L":
            self.left = igra.design.left_levo[zaporedna_poteza]
            self.top = igra.design.top_levo[zaporedna_poteza]
        elif poteza.stran == "D":
            self.left = igra.design.left_desno[zaporedna_poteza]
            self.top = igra.design.top_desno[zaporedna_poteza]

    def dimenzije(self,width,height):
        if self.postavitev == "h":
            self.width = width
            self.height = height / 2
        elif self.postavitev == "v":
            self.width = width / 2
            self.height = height
    #1-preloma -> prejsnjo + width 
    #prelom+1 - preloma -> prejsnjo
    #prelom - prelom -> prejsnjo - width
    #prelom + 1-prelom -> prejsnjo