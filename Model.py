import random

class Igra:
    def __init__(self, igralec1, igralec2):
        self.igralci = [igralec1, igralec2]
        self.igralec1 = igralec1
        self.igralec2 = igralec2
        self.igrane_domine = Igrane_domine()
        #novi class nerazdeljene_domine
        self.nerazdeljene_domine = [ Domino(6,6), Domino(6,5), Domino(6,4), Domino(6,3), Domino(6,2), Domino (6,1), Domino(6,0),
                        Domino(5,5), Domino(5,4), Domino(5,3), Domino(5,2), Domino(5,1), Domino(5,0),
                        Domino(4,4), Domino(4,3), Domino(4,2), Domino(4,1), Domino(4,0),
                        Domino(3,3), Domino(3,2), Domino(3,1), Domino(3,0),
                        Domino(2,2), Domino(2,1), Domino(2,0),
                        Domino(1,1), Domino(1,0),
                        Domino(0,0)]

    def razdeli(self):
        for igralec in self.igralci:
            for _ in range(7):
                nakljucna_domina = random.choice(self.nerazdeljene_domine)
                igralec.dodaj_domino(nakljucna_domina)
                self.nerazdeljene_domine.remove(nakljucna_domina)
    
    def zacni_igro(self):
        for n in range(6,-1,-1):
            for igralec in self.igralci:
                if Domino(n,n).domino in igralec.domine:
                    self.igralec_na_potezi = igralec
                    igralec.poteza(Domino(n,n))
                    self.igrane_domine.dodaj_prvo(Domino(n,n))
                    self.naslednji_na_potezi()
                    return
        self.igralec_na_potezi = self.igralec1          

    def naslednji_na_potezi(self):
        if self.igralec_na_potezi == self.igralec1:
            self.igralec_na_potezi = self.igralec2
        elif self.igralec_na_potezi == self.igralec2:
            self.igralec_na_potezi = self.igralec1


    def poteza(self):
        self.igralec_na_potezi.poteza()

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
        self.igrane.insert(0,domino.domino)
        self.leva_stran = domino.leve_pike

    def dodaj_na_desni(self,domino):
        self.igrane.append(domino.domino)
        self.desna_stran = domino.desne_pike

    def dodaj_prvo(self,domino):
        self.igrane.append(domino.domino)
        self.leva_stran = domino.leve_pike
        self.desna_stran = domino.desne_pike

    


    
class Igralec:
    def __init__(self):
        self.domine = []

    def dodaj_domino(self,domino):
        Domine = self.domine
        Domine.append(domino.domino)
        self.domine = Domine

    def razpolozljive_domine(self):
        return self.domine

    def poteza(self,domino):
        self.domine.remove(domino.domino)

class Domino:
    def __init__(self,leve_pike, desne_pike):
        self.leve_pike = leve_pike
        self.desne_pike = desne_pike
        self.domino = (leve_pike,desne_pike)
    
    def __repr__(self):
        return '({}, {})'.format(self.leve_pike, self.desne_pike)
    
    
    def obrni(self):
        self.domino = self.domino.reverse()
        self.leve_pike = self.domino(0)
        self.desne_pike = self.domino(1)


