class Igra:
    def __init__(self, igralec1, igralec2):
        self.igralec1 = igralec1
        self.igralec2 = igralec2
    
    def zacni(self,igralec):
        self.igralec_na_potezi = igralec
    
    def naslednji_na_potezi(self):
        if self.igralec_na_potezi == self.igralec1:
            self.igralec_na_potezi = self.igralec2
        elif self.igralec_na_potezi == self.igralec2:
            self.igralec_na_potezi = self.igralec1

    def je_konec_igre(self):
        if self.igralec1.stevilo_domin == 0 or self.igralec2.stevilo_domin == 0:
            return True
        elif self.igralec1.stevilo_moznih_potez == 0 and self.igralec2.stevilo_moznih_potez == 0:
            return True
        return False


class Tabla:   
    def ___init___(self,Domino):
        self.igrane_domine = [Domino]
        self.leva_stran = Domino.leve_pike
        self.desna_stran = Domino.desne_pike

    def igraj_na_levi(self,Domino):
        self.igrane_domine = self.igrane_domine.insert(0,Domino)
        self.leva_stran = Domino.leve_pike

    def igraj_na_desni(self,Domino):
        self.igrane_domine = self.igrane_domine.append(Domino)
        self.desna_stran = Domino.desne_pike
    


class Igralec:
    def stevilo_domin(self,Igralceve_domine):
        return len(Igralceve_domine.domine)
    
    def stevilo_motnih_potez(self,Igralceve_domine):
        return len(Igralceve_domine.mozne_poteze)

    def igraj(self,Domino,Stran):
            Tabla.dodaj(Domino,Stran)
            Igralceve_Domine.Domine = igralceve_domine.Domine.Pop(Domino)
            Igra.naslednji_na_potezi()


class Igralceve_Domine:
    def __init__(self,domine):
        self.Domine = domine

    def mozne_poteze(self):
        seznam_moznih_potez = []
        for Domino in self.Domine:
            if Tabla.je_mozna_poteza(Domino,"L"):
                seznam_moznih_potez.append((Domino,"L"))
            if Tabla.je_mozna_poteza(Domino,"R"):
                seznam_moznih_potez.append((Domino,"L"))
        return seznam_moznih_potez


class Domino:
    def __init__(self,leva,desna):
        self.domino = [leva,desna]
        self.leve_pike = leva
        self.desne_pike = desna
    
    def obrni(self):
        self.domino = [self.desna,self.leva]
        leva = self.leve_pike
        self.leve_pike = self.desne_pike
        self.desne_pike = leva


