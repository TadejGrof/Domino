import random
class Serija_Iger:
    def __init__(self, igralec1, igralec2, tocke_za_zmago = 100):
        self.igralec1 = igralec1
        self.igralec2 = igralec2
        self.igralci = [igralec1, igralec2]
        self.aktivna_igra = None
        self.koncane_igre = []
        self.tocke_za_zmago = tocke_za_zmago
    
    def vrni_zmagovalca(self):
        for igralec in self.igralci:
            if igralec.skupne_tocke >= self.tocke_za_zmago:
                self.zmagovalec = igralec
                return igralec

    def je_konec(self):
        for igralec in self.igralci:
            if igralec.skupne_tocke >= self.tocke_za_zmago:
                return True
        return False

    def nova_igra(self):
        self.aktivna_igra = Igra(self.igralec1, self.igralec2)

    def vodilni(self):
        if self.igralec1.skupne_tocke >= self.igralec2.skupne_tocke:
            return self.igralec1
        elif self.igralec2.skupne_tocke > self.igralec1.skupne_tocke:
            return self.igralec2
        else: return None
        
class Igra:
    def __init__(self, igralec1, igralec2):
        self.igralci = [igralec1, igralec2]
        self.igralec1 = igralec1
        self.igralec2 = igralec2
        self.igralec_na_potezi = None
        for igralec in self.igralci:
            igralec.domine = []
            igralec.poteze = []
        self.igrane_domine = Igrane_domine()
        self.nerazdeljene_domine = [Domino(n,i) for n in range(6,-1,-1) for i in range(n,-1,-1)]
        self.poteze = []
        self.koncana = False

    def doloci_design(self):
        self.design = Igra_design()

    def konec_igre(self, serija):
        serija.koncane_igre.append(self)
        self.koncana = True
        self.zmagovalec = self.vrni_zmagovalca()
        self.koncne_tocke = self.vrni_koncne_tocke()
        if self.je_kapikua():
            self.koncne_tocke += 25
            self.kapikua = True
        else:
            self.kapikua = False

    
    def je_kapikua(self):
        self.igrane_domine.brez_zadnje_poteze(self)
        domino = {"L": self.zadnja_poteza().domino.leve_pike, "D": self.poteze[-1].domino.desne_pike}
        igrane = {"L": self.igrane_domine.leva_brez_zadnje, "D": self.igrane_domine.desna_brez_zadnje}
        if igrane["L"] == igrane["D"]:
            return False
        elif domino["L"] == igrane["L"] and domino["D"] == igrane["D"]:
            return True
        elif domino["L"] == igrane["D"] and domino["D"] == igrane["L"]:
            return True
        else:
            return False

    def vrni_zmagovalca(self):
        for igralec in self.igralci:
            if len(igralec.domine) == 0:
                return igralec
        if self.igralec1.stevilo_pik() > self.igralec2.stevilo_pik():
            return self.igralec2
        elif self.igralec1.stevilo_pik() < self.igralec2.stevilo_pik():
            return self.igralec1
        elif self.igralec1.stevilo_pik() == self.igralec2.stevilo_pik():
            return self.zadnja_poteza().igralec

    def stevilo_potez(self,stran = ""):
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

    def zaporedna_poteza(self,moja_poteza):
        stevilo = 0
        if moja_poteza.stran == "S":
            return stevilo
        else:
            for poteza in self.poteze:
                if poteza != moja_poteza:
                    if poteza.stran == moja_poteza.stran:
                        stevilo += 1
                elif poteza == moja_poteza:
                    break
            return stevilo + 1

    def zadnja_poteza(self,stran = ""):
        if stran == "":
            return self.poteze[-1]
        elif stran == "L" or stran == "D":
            stranske_poteze = []
            for poteza in self.poteze:
                if poteza.stran == stran:
                    stranske_poteze.append(poteza)
            return stranske_poteze[-1]

    def index_poteze(self,moja_poteza):
        index = 0
        for poteza in self.poteze:
            if poteza != moja_poteza:
                index += 1
            elif poteza == moja_poteza:
                break
        return index
            
    def vrni_koncne_tocke(self):
        sestevek = 0
        for igralec in self.igralci:
            for domino in igralec.domine:
                sestevek += domino.pike
        return sestevek

    def je_konec_igre(self):
        if len(self.igralec1.domine) == 0 or len(self.igralec2.domine) == 0:
            return True
        elif len(self.nerazdeljene_domine) == 0:
            moznepoteze1 = self.igralec1.mozne_poteze(self.igrane_domine)
            moznepoteze2 = self.igralec2.mozne_poteze(self.igrane_domine)
            if len(moznepoteze1) == 0 and len(moznepoteze2) == 0:
                return True
        return False

    def nakljucna_iz_nerazdeljenih(self):
        nakljucna_domina = random.choice(self.nerazdeljene_domine)
        self.nerazdeljene_domine.remove(nakljucna_domina)
        return nakljucna_domina

    def razdeli(self):
        for igralec in self.igralci:
            for _ in range(7):
                igralec.dodaj_domino(self.nakljucna_iz_nerazdeljenih())
    
    def doloci_igralca_na_potezi(self,igralec):
        self.igralec_na_potezi = igralec

    def zacetna_poteza(self):
        for n in range(6,-1,-1):
            for igralec in self.igralci:
                for domino in igralec.domine:
                    if domino.domino == Domino(n,n).domino:
                        return Poteza(Domino(n,n), "S", igralec)
        return None
        
                  
    def naslednji_na_potezi(self):
        self.igralec_na_potezi = self.igralec_na_potezi.nasprotnik(self)
       

    def nakljucna_poteza(self):
        poteza = self.igralec_na_potezi.nakljucna_poteza(self.igrane_domine)
        self.poteze.append(poteza)
        self.naslednji_na_potezi()
        return poteza

    def poteza(self,poteza):
        poteza.igralec.poteza(self.igrane_domine,poteza)
        self.poteze.append(poteza)
        self.naslednji_na_potezi()

    def dodaj_domino(self):
        self.igralec_na_potezi.dodaj_domino(self.nakljucna_iz_nerazdeljenih())
    
    def dodaj_do_poteze(self):
        while len(self.igralec_na_potezi.mozne_poteze(self.igrane_domine)) == 0:
            self.dodaj_domino()
            
class Igrane_domine:
    def __init__(self):
        self.igrane = []

    def __repr__(self):
        return self.igrane

    def __str__(self):
        polje = ''
        for domino in self.igrane:
            polje += '[{}|{}]'.format(domino[0],domino[1])
        return polje
    
    def stran(self,stran):
        if stran == "L":
            return self.leva_stran
        elif stran == "D":
            return self.desna_stran

    def brez_zadnje_poteze(self,igra):
        if igra.zadnja_poteza().stran == "L":
            self.leva_brez_zadnje = self.igrane[1][0]
            self.desna_brez_zadnje = self.desna_stran
        elif igra.zadnja_poteza().stran == "D":
            self.leva_brez_zadnje = self.leva_stran
            self.desna_brez_zadnje = self.igrane[-2][1]

    def dodaj_na_levi(self,domino):
        if domino.desne_pike == self.leva_stran:
            self.igrane.insert(0,domino.domino)
            self.leva_stran = domino.leve_pike
        elif domino.leve_pike == self.leva_stran:
            self.igrane.insert(0,domino.obrnjeno_domino)
            self.leva_stran = domino.desne_pike

    def dodaj_na_desni(self,domino):
        if domino.leve_pike == self.desna_stran:
            self.igrane.append(domino.domino)
            self.desna_stran = domino.desne_pike
        elif domino.desne_pike == self.desna_stran:
            self.igrane.append(domino.obrnjeno_domino)
            self.desna_stran = domino.leve_pike

    def dodaj_prvo(self,domino):
        self.igrane.append(domino.domino)
        self.leva_stran = domino.leve_pike
        self.desna_stran = domino.desne_pike

    def se_lahko_doda_na_levi(self,domino):
        if domino.leve_pik() == self.leva_stran or domino.desne_pike == self.leva_stran:
            return True
        else: return False
    
    def se_lahko_doda_na_desni(self,domino):
        if domino.leve_pik() == self.desna_stran or domino.desne_pike == self.desna_stran:
            return True
        else: return False
    
    def se_lahko_doda_na_obeh(self,domino):
        if self.se_lahko_doda_na_levi(domino) and self.se_lahko_doda_na_desni(domino):
            return True
        else:
            return False

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
        if poteza.stran == "L":
            if self.se_lahko_doda_na_levi(poteza.domino):
                return True
        elif poteza.stran == "D":
            if self.se_lahko_doda_na_desni(poteza.domino):
                return True
        return False

    def je_treba_obrnit(self,stran,domino):
        if stran == "L":
            if domino.leve_pike == self.leva_stran:
                return True
        elif stran == "D":
            if domino.desne_pike == self.desna_stran:
                return True
        return False
        
class Igralec:
    def __init__(self,ime = "Racunalnik"):
        self.domine = []
        self.ime = ime
        self.skupne_tocke = 0
        self.poteze = []

    def __repr__(self):
        return self.ime

    def __str__(self):
        return self.ime

    def stevilo_pik(self):
        stevilo_pik = 0
        for domino in self.domine:
            stevilo_pik += domino.leve_pike + domino.desne_pike
            return stevilo_pik



    def skrite_domine(self):
        skrite_domine = ''
        for _ in self.domine:
            skrite_domine += ' [ | ]'
        return skrite_domine


    def nasprotnik(self,igra):
        if self == igra.igralec1:
            return igra.igralec2
        elif self == igra.igralec2:
            return igra.igralec1

    def stevilo_domin(self):
        return len(self.domine)

    def zadnje_domino(self):
        return self.domine[self.stevilo_domin() -1] 

    def dodaj_domino(self,domino):
        self.domine.append(domino)

    def razpolozljive_domine(self):
        razpolozljive_domine = []
        for domino in self.domine:
            razpolozljive_domine.append(domino.domino)
        return razpolozljive_domine

    def tocke_po_zmagi(self,stevilo_tock):
        self.skupne_tocke += int(stevilo_tock)

    def poteza(self,igrane_domine,poteza):
        if poteza.stran == "L":
            igrane_domine.dodaj_na_levi(poteza.domino)
        elif poteza.stran == "D":
            igrane_domine.dodaj_na_desni(poteza.domino)
        elif poteza.stran == "S":
            igrane_domine.dodaj_prvo(poteza.domino)
        self.poteze.append(poteza)
        self.odstrani_domino(poteza.domino)

    def nakljucna_poteza(self,igrane_domine):
        mozne_poteze = self.mozne_poteze(igrane_domine)
        nakljucna_poteza = random.choice(mozne_poteze)
        if nakljucna_poteza.stran == "L":
            igrane_domine.dodaj_na_levi(nakljucna_poteza.domino)
        elif nakljucna_poteza.stran == "D":
            igrane_domine.dodaj_na_desni(nakljucna_poteza.domino)
        self.odstrani_domino(nakljucna_poteza.domino)
        return nakljucna_poteza

    def odstrani_domino(self,domino):
        for domina in self.domine:
            if domina.domino == domino.domino or domina.domino == domino.obrnjeno_domino:
                self.domine.remove(domina)
                return

    def mozne_poteze(self,igrane_domine):
        mozne_poteze = []
        for domino in self.domine:
            if domino.leve_pike == igrane_domine.leva_stran:
                mozne_poteze.append(Poteza(domino,"L",self,True))
            elif domino.desne_pike == igrane_domine.leva_stran:
                mozne_poteze.append(Poteza(domino,"L",self,False))
            if domino.leve_pike == igrane_domine.desna_stran:
                mozne_poteze.append(Poteza(domino,"D",self,False))
            elif domino.desne_pike == igrane_domine.desna_stran:
                mozne_poteze.append(Poteza(domino,"D",self,True))
        return mozne_poteze

    def stevilo_moznih_potez(self,igrane_domine):
        return len(self.mozne_poteze(igrane_domine))

class Poteza:
    def __init__(self,domino,stran,igralec,obrnjeno = False):
        self.domino = domino
        self.stran = stran
        self.igralec = igralec
        self.obrnjeno = obrnjeno

    def doloci_design(self,igra):
        self.design = Poteza_design(igra,self)


class Domino:
    def __init__(self,leve_pike, desne_pike):
        self.leve_pike = leve_pike
        self.desne_pike = desne_pike
        self.domino = (leve_pike,desne_pike)
        self.obrnjeno_domino = (desne_pike, leve_pike)
        self.pike = leve_pike + desne_pike
    
    def leve_pik(self):
        return self.domino[0]
    
    def desne_pik(self):
        return self.domino[1]

    def je_dvojna(self):
        if self.leve_pike == self.desne_pike:
            return True
        else:
            return False

    def __repr__(self):
        return '({},{})'.format(self.leve_pike, self.desne_pike)
    
    def ___str___(self):
        return '({},{})'.format(self.leve_pike, self.desne_pike)

    def slika(self):
        return str(self) + '.jpg'

class Igra_design:
    def __init__(self,width = 9, height = 20):
        self.width = width
        self.height = height
        self.postavitev = ["h" for _ in range(5)] + ["v" for _ in range(2)] + ["h" for _ in range(10)] + ["v"]
        self.rotate = [False for _ in range(5)] + [True for _ in range(11)]
        self.zacetni_left = 50 - self.width / 2
        self.desni_left = self.zacetni_left + self.width * 4 + self.width
        self.levi_left = self.zacetni_left - self.width * 4
        self.zacetni_top = 50 - self.height / 2
        self.zgornji_top = self.zacetni_top - self.height - self.height / 2
        self.spodnji_top = self.zacetni_top + self.height * 2
        self.left_levo = [self.zacetni_left] + [self.zacetni_left - self.width * n for n in range(1,5)] + [self.levi_left for _ in range(2)] + [self.levi_left + self.width / 2 + n * self.width for n in range(9)]
        self.left_desno = [self.zacetni_left] + [self.zacetni_left + self.width * n for n in range(1,5)] + [self.desni_left for _ in range(2)] + [self.desni_left - self.width * n for n in range(1,10)]    
        self.top_levo = [self.zacetni_top for _ in range(5)] + [self.zacetni_top + self.height / 2 + n * self.height for n in range(2)] + [self.spodnji_top for _ in range(10)]
        self.top_desno = [self.zacetni_top for _ in range(5)] + [self.zacetni_top - self.height / 2 - n * self.height for n in range(2)] + [self.zgornji_top for _ in range(10)]


class Poteza_design:
    def __init__(self,igra,poteza):
        zaporedna_poteza = igra.zaporedna_poteza(poteza)
        self.postavitev = igra.design.postavitev[zaporedna_poteza]
        self.dimenzije(igra.design.width,igra.design.height)
        if self.postavitev == "h":
            self.slika = "({},{}).jpg".format(poteza.domino.leve_pike,poteza.domino.desne_pike)
        elif self.postavitev == "v":
            self.slika = "v-({},{}).jpg".format(poteza.domino.leve_pike,poteza.domino.desne_pike)
        if igra.design.rotate[zaporedna_poteza]:
            if poteza.obrnjeno:
                self.rotate = 0
            else:
                self.rotate = 180
        else:
            if poteza.obrnjeno:
                self.rotate = 180
            else:
                self.rotate = 0
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