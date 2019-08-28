import random
class Serija_Iger:
    def __init__(self, igralec1, igralec2, tocke_za_zmago = 100):
        self.igralec1 = igralec1
        self.igralec2 = igralec2
        self.koncane_igre = []
        self.tocke_za_zmago = tocke_za_zmago
        
    def nova_igra(self):
        self.aktivna_igra = Igra(self.igralec1, self.igralec2)

    def vodilni(self):
        if self.igralec1.skupne_tocke >= self.igralec2.skupne_tocke:
            return self.igralec1
        elif self.igralec2.skupne_tocke > self.igralec1.skupne_tocke:
            return self.igralec2
        

class Igra:
    def __init__(self, igralec1, igralec2):
        self.igralci = [igralec1, igralec2]
        self.igralec1 = igralec1
        self.igralec2 = igralec2
        self.igrane_domine = Igrane_domine()
        self.nerazdeljene_domine = [Domino(n,i) for n in range(6,-1,-1) for i in range(n,-1,-1)]
        self.poteze = []

    def koncne_tocke(self):
        sestevek = 0
        for igralec in self.igralci:
            for domino in igralec.domine:
                sestevek += domino.pike
        for domino in self.nerazdeljene_domine:
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
    
    def zacni_igro(self):
        for n in range(6,-1,-1):
            for igralec in self.igralci:
                for domino in igralec.domine:
                    if domino.domino == Domino(n,n).domino:
                        self.igralec_na_potezi = igralec
                        igralec.odstrani_domino(Domino(n,n))
                        self.igrane_domine.dodaj_prvo(Domino(n,n))
                        self.naslednji_na_potezi()
                        return
        self.igralec_na_potezi = self.igralec1          

    def naslednji_na_potezi(self):
        self.igralec_na_potezi = self.igralec_na_potezi.nasprotnik(self)
       

    def nakljucna_poteza(self):
        mozne_poteze = self.igralec_na_potezi.mozne_poteze(self.igrane_domine)
        while len(mozne_poteze) == 0:
            self.dodaj_domino()
            mozne_poteze = self.igralec_na_potezi.mozne_poteze(self.igrane_domine)
        self.igralec_na_potezi.nakljucna_poteza(self.igrane_domine)
        self.naslednji_na_potezi()

    def poteza(self,poteza):
        self.igralec_na_potezi.poteza(self.igrane_domine,poteza)
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
        tabla = ' '
        if len(self.igrane) != 0:
            for domino in self.igrane:
                tabla = tabla + domino + " " 
            return tabla

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
        if domino.leve_pike == self.leva_stran or domino.desne_pike == self.leva_stran:
            return True
        else: return False
    
    def se_lahko_doda_na_desni(self,domino):
        if domino.leve_pike == self.desna_stran or domino.desne_pike == self.desna_stran:
            return True
        else: return False

    def je_prava_poteza(self,poteza):
        if poteza[1] == "L":
            if self.se_lahko_doda_na_levi(poteza[0]):
                return True
        elif poteza[1] == "D":
            if self.se_lahko_doda_na_desni(poteza[0]):
                return True
        return False



    
class Igralec:
    def __init__(self,ime = "Računalnik"):
        self.domine = []
        self.ime = ime
        self.skupne_tocke = 0

    def __repr__(self):
        return self.ime

    def __str__(self):
        return self.ime

    def nasprotnik(self,igra):
        if self == igra.igralec1:
            return igra.igralec2
        elif self == igra.igralec2:
            return igra.igralec1
        
    def dodaj_domino(self,domino):
        self.domine.append(domino)

    def razpolozljive_domine(self):
        razpolozljive_domine = []
        for domino in self.domine:
            razpolozljive_domine.append(domino.domino)
        return razpolozljive_domine

    def tocke_po_zmagi(self,tocke):
        self.skupne_tocke += tocke

    #def poteza(self,igrane_domine,poteza):

    def poteza(self,igrane_domine,poteza):
        if poteza[1] == "L":
            igrane_domine.dodaj_na_levi(poteza[0])
            self.odstrani_domino(poteza[0])
        elif poteza[1] == "D":
            igrane_domine.dodaj_na_desni(poteza[0])
            self.odstrani_domino(poteza[0])

    def nakljucna_poteza(self,igrane_domine):
        mozne_poteze = self.mozne_poteze(igrane_domine)
        nakljucna_poteza = random.choice(mozne_poteze)
        if nakljucna_poteza[1] == "L":
            igrane_domine.dodaj_na_levi(nakljucna_poteza[0])
            self.odstrani_domino(nakljucna_poteza[0])
        elif nakljucna_poteza[1] == "D":
            igrane_domine.dodaj_na_desni(nakljucna_poteza[0])
            self.odstrani_domino(nakljucna_poteza[0])

    def odstrani_domino(self,domino):
        for domina in self.domine:
            if domina.domino == domino.domino or domina.domino == domino.obrnjeno_domino:
                self.domine.remove(domina)
                return

    def mozne_poteze(self,igrane_domine):
        mozne_poteze = []
        for domino in self.domine:
            if domino.leve_pike == igrane_domine.leva_stran or domino.desne_pike == igrane_domine.leva_stran:
                mozne_poteze.append([domino,"L"])

            if domino.leve_pike == igrane_domine.desna_stran or domino.desne_pike == igrane_domine.desna_stran:
                mozne_poteze.append([domino,"D"])
        return mozne_poteze


class Domino:
    def __init__(self,leve_pike, desne_pike):
        self.leve_pike = leve_pike
        self.desne_pike = desne_pike
        self.domino = (leve_pike,desne_pike)
        self.obrnjeno_domino = (desne_pike, leve_pike)
        self.pike = leve_pike + desne_pike
    
    def __repr__(self):
        return '({}, {})'.format(self.leve_pike, self.desne_pike)
    
    def ___str___(self):
        return '({}, {})'.format(self.leve_pike, self.desne_pike)
