from Model import Serija_Iger, Igra, Igralec, Igrane_domine, Domino, Poteza

def preberi():
    return input('> ')

def preberi_stevilo():
    while True:
        izbira = preberi()
        if izbira.isdigit():
            return int(izbira)
        else:
            print('Vpisi stevilko!')

def informacije(serija):
    print('Skupne tocke:')
    print('-', serija.igralec1.ime, ': ', serija.igralec1.skupne_tocke)
    print('- Racunalnik : ', serija.igralec2.skupne_tocke)
    print('Tocke potrebne za zmago: ', serija.tocke_za_zmago)

def aktivni_podatki(igra):
    print('')
    print('Racunlanikove domine: ', igra.igralec2.skrite_domine())
    print('stevilo nerazdeljenih domin:', len(igra.nerazdeljene_domine))
    print('')
    print('Igrane domine: ', igra.igrane_domine)
    print('')
    print('Moje domine: ', igra.igralec1.domine)

def igralcev_meni(igra):
    aktivni_podatki(igra)
    print('Izberi:')
    print('1) Igraj')
    print('2) Dodaj')
    igralceva_izbira(igra)

def igralec_dodaj(igra):
    if igra.igralec1.stevilo_moznih_potez(igra.igrane_domine) == 0:
        nakljucna_domina = igra.nakljucna_iz_nerazdeljenih()
        igra.igralec1.dodaj_domino(nakljucna_domina)
        print('Dodal si domino: ', nakljucna_domina)
    else:
        print('Dokler je navoljo vsaj ena veljavna poteza, dodajanje ni mogoce!')

def igralec_igraj(igra,poteza):
    igra.poteza(poteza)
    if poteza.stran == "L":
        print('Igral si: ', poteza.domino, 'na levo stran')
    elif poteza.stran == "D":
        print('Igral si: ', poteza.domino, 'na desno stran')

def igralec_izbira_poteze(igra,mozne_poteze):
    while True:
        izbira = preberi_stevilo()
        if izbira >= 0 and izbira < len(mozne_poteze):
            igralec_igraj(igra,mozne_poteze[izbira])
            return
        else:
            print('izberi stevilo med 0 in ', len(mozne_poteze))

def igralec_igraj_meni(igra):
    mozne_poteze = igra.igralec1.mozne_poteze(igra.igrane_domine)
    for i in range(len(mozne_poteze)):
        poteza = mozne_poteze[i]
        if poteza.stran == "L":
            print(i, ') ',  poteza.domino, 'na levo stran.')
        elif poteza.stran == "D":
            print(i, ') ',  poteza.domino, 'na desno stran.')
    igralec_izbira_poteze(igra,mozne_poteze)
    
def igralceva_izbira(igra):
    while True:
        izbira = preberi_stevilo()
        if izbira == 1:
            if igra.igralec1.stevilo_moznih_potez(igra.igrane_domine) > 0:
                igralec_igraj_meni(igra)
            else: 
                print('Brez moznih potez! Dodaj domino.')
            return
        elif izbira == 2:
            if len(igra.nerazdeljene_domine) == 0:
                igra.naslednji_na_potezi
                print('Ni mogoce narediti nobene poteze in ni mogoce dodati domine!')
                print('Na potezi je racunalnik!')
                return
            else:
                igralec_dodaj(igra)
            return

def prva_poteza(igra):
    prva_poteza = igra.zacetna_poteza()
    if prva_poteza != None:
        igra.doloci_igralca_na_potezi(prva_poteza.igralec)
        print('Igro zacne: ', prva_poteza.igralec)
        igra.poteza(prva_poteza)
        print(prva_poteza.igralec, 'je zacel igro z domino:' , prva_poteza.domino)
        print('Na potezi je:', prva_poteza.igralec.nasprotnik(igra))
    else: 
        print('Noben od igralcev nima dvojne domine!')
        print('Igro zacne', igra.igralec1)
        igra.doloci_igralca_na_potezi(igra.igralec1)

def racunalnikova_poteza(igra):
    poteza = igra.nakljucna_poteza()
    if poteza.stran == "L":
        print('Racunalnik je naredil potezo:', poteza.domino , ' na levo stran!')
    elif poteza.stran == "D":
        print('Racunalnik je naredil potezo:', poteza.domino , ' na desno stran!')

def poteza(igra):
    if igra.igralec_na_potezi == igra.igralec2:
        stevilo_moznih_potez = igra.igralec2.stevilo_moznih_potez(igra.igrane_domine)
        while stevilo_moznih_potez == 0:
            if len(igra.nerazdeljene_domine) == 0:
                igra.naslednji_na_potezi()
                print('Racunalnik nima poteze in ne more dodati domine!')
                print('Na potezi je: ', igra.igralec_na_potezi)
                return
            else:
                igra.igralec2.dodaj_domino(igra.nakljucna_iz_nerazdeljenih())
                print('Racunalnik doda domino!')
                stevilo_moznih_potez = igra.igralec2.stevilo_moznih_potez(igra.igrane_domine)
        racunalnikova_poteza(igra)
    elif igra.igralec_na_potezi == igra.igralec1:
        igralcev_meni(igra)

def nova_igra(serija):
    serija.nova_igra()
    igra = serija.aktivna_igra
    igra.razdeli()
    print('Domine so bile razdeljene!')

    prva_poteza(igra)
    while not igra.je_konec_igre():
        poteza(igra)
    igra.konec_igre(serija)
    igra.zmagovalec.tocke_po_zmagi(igra.koncne_tocke)
    print(len(serija.koncane_igre),'. igro je zmagal: ', igra.zmagovalec,)
    print('Za zmago je dobil ', igra.koncne_tocke, ' tock.')
    print('')

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

def prvi_meni(ime):
    serija = Serija_Iger(Igralec(ime),Igralec())
    while not serija.je_konec():
        drugi_meni(serija)
    return serija
def main():
    print('Dobrodosli v igri Domino!')
    print('Za zacetek nove serije vpisi ime')
    ime = preberi()
    serija = prvi_meni(ime)
    print('KONEC IGRE!')
    print('Zmagovalec: ', serija.vrni_zmagovalca())
    print('')
    print('Za zacetek nove igre resetiraj program!')
main()