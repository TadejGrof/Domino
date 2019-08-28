from Model import Serija_Iger, Igra, Igralec, Igrane_domine, Domino, Poteza

def preberi():
    return input('> ')

def preberi_stevilo():
    while True:
        izbira = preberi()
        if izbira.isdigit():
            return int(izbira)
        else:
            print('Vpišite številko')

def informacije(serija):
    print('Igralčeve skupne točke: ', serija.igralec1.skupne_tocke)
    print('Računlanikove skupne točke: ', serija.igralec2.skupne_tocke)
    print('Točke potrebne za zmago: ', serija.tocke_za_zmago)

def racunalnikova_poteza(igra):
    igra.nakljucna_poteza()
    poteza = igra.zadnja_poteza()
    igrano_domino = poteza.domino
    stran = poteza.stran

    print('Računalnik je naredil potezo!')
    if stran == "L":
        print('Igral je: ', igrano_domino, ' na levo stran!')
    elif stran == "R":
        print('Igral je: ', igrano_domino, ' na desno stran!')

def prva_poteza(igra):
    igra.zacni_igro()
    if igra.število_potez() == 1:
        igralec_prve_poteze = igra.poteze[0].igralec
        if igralec_prve_poteze == igra.igralec2:
            print('Racunalnik je začel igro z: ', igra.poteze[0].domino)
            print('Na potezi je Igralec!')
        elif igralec_prve_poteze.ime == igra.igralec1.ime:
            print('Igralec je začel igro z: ', igra.poteze[0].domino)
            print('Na potezi je Računalnik!')
            racunalnikova_poteza(igra)
    else: print('Nobeden od igralcev ni imel dvojne domine. Igro začne igralec!')

def aktivni_podatki(igra):
    print('Računlanikove domine: ', igra.igralec2.skrite_domine())
    print('')
    print('Igrane domine: ', igra.igrane_domine)
    print('')
    print('Moje domine: ', igra.igralec1.domine)

def moznosti_meni(igra):
    mozne_poteze = igra.igralec1.mozne_poteze(igra.igrane_domine)
    for i in range(len(mozne_poteze)):
        if mozne_poteze[i].stran == "L":
            print(i, ') ', mozne_poteze[i].domino, 'na levo stran.')
        elif mozne_poteze[i].stran == "D":
            print(i, ') ', mozne_poteze[i].domino, 'na desno stran.')
    izbira_poteze(igra,mozne_poteze)

def izbira_poteze(igra,mozne_poteze):
    while True:
        izbira = preberi_stevilo()
        if izbira >= 0 and izbira < len(mozne_poteze):
            poteza = mozne_poteze[izbira]
            igra.poteza(poteza)
            if poteza.stran == "L":
                print('Igralec je naredil potezo: ', poteza.domino, 'na levo stran.' )
            elif poteza.stran == "D":
                print('Igralec je naredil potezo: ', poteza.domino, 'na desno stran.' )
            racunalnikova_poteza(igra)
            return
        else:
            print('Izberi stevilo med 0 in ' , len(mozne_poteze) )


def igralceva_izbira(igra):
    while True:
        izbira = preberi_stevilo()
        if izbira == 1:
            moznosti_meni(igra)
            return
        elif izbira == 2:
            igra.igralec1.dodaj_domino(igra.nakljucna_iz_nerazdeljenih())
            print('Dodana domina: ', igra.igralec1.zadnje_domino())
            return
            
def igralcev_meni(igra):
    aktivni_podatki(igra)
    print('Izberi:')
    print('1) Igraj')
    print('2) Dodaj')
    igralceva_izbira(igra)

def nova_igra(serija):
    serija.nova_igra()
    igra = serija.aktivna_igra
    igra.razdeli()
    prva_poteza(igra)
    while not igra.je_konec_igre():
        igralcev_meni(igra)



def drugi_meni(serija):
    print('Izberi:')
    print('1) Nova Igra')
    print('2) Informacije')
    while True:
        izbira = preberi_stevilo()
        if izbira == 1:
            nova_igra(serija)
            return
        elif izbira == 2:
            informacije(serija)
            return

def osnovni_meni():
    serija = Serija_Iger(Igralec("Jaz"),Igralec())
    while serija.vodilni().skupne_tocke < serija.tocke_za_zmago:
        drugi_meni(serija)

def main():
    print('Dobrodošli v igri Domino!')
    print('Za začetek nove serije vpiši 1!')
    while True:
        if preberi_stevilo() == 1:
            osnovni_meni()
            return
        else: print("Za začetek nove serije vpiši 1!")

    
main()