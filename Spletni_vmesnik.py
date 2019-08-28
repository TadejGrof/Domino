from Model import Serija_Iger, Igra, Igralec, Igrane_domine, Domino, Poteza
import bottle

serija = None

@bottle.route('/igra/partija/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root = "./static/")

@bottle.route('/domino/<filepath:path>')
def server_static2(filepath):
    return bottle.static_file(filepath, root = "./static/")
    
@bottle.get('/')
def osnovna_stran():
    global serija
    if serija == None:
        return bottle.template('osnovna_stran.tpl')
    else:
        return 'igra že poteka'

@bottle.post('/igra/')
def igra_stran():
    global serija
    if serija == None:
        ime = bottle.request.forms['ime']
        serija = Serija_Iger(Igralec(ime),Igralec())
        serija.nova_igra()
        return bottle.template('igra_stran.tpl', serija = serija)
    else: 
        return 'igra že poteka'

def začetna_poteza(igra):
    igra.razdeli()
    poteza = igra.zacetna_poteza()
    igra.določi_igralca_na_potezi(poteza.igralec)
    igra.poteza(poteza)
    if igra.igralec_na_potezi == igra.igralec2:
        while igra.igralec2.število_moznih_potez(igra.igrane_domine) == 0:
            while len(igra.nerazdeljene_domine) > 0:
                igra.igralec2.dodaj_domino(igra.nakljucna_iz_nerazdeljenih())
        igra.nakljucna_poteza()
def dodaj_domino(igra):
    nakljucna = igra.nakljucna_iz_nerazdeljenih()
    igra.igralec_na_potezi.dodaj_domino(nakljucna)
    besedilo = igra.igralec_na_potezi.ime + ' doda ' + str(nakljucna)
    return besedilo

def brez_poteze(igra):
    besedilo = igra.igralec_na_potezi.ime + ' ne more narediti poteze in ne more dodati domine. <br> Na potezi je: ' + igra.igralec_na_potezi.nasprotnik()
    igra.naslednji_na_potezi()
    return besedilo

def igralceva_poteza(igra):
    poteza = igra.nakljucna_poteza()
    if poteza.stran == "L":
        besedilo = poteza.igralec.ime + ' igra ' + str(poteza.domino) + ' na levo stran polja.'
    elif poteza.stran == "D":
        besedilo = poteza.igralec.ime + ' igra ' + str(poteza.domino) + ' na desno stran polja.'
    return besedilo

def poteza(igra):
    možne_poteze = igra.igralec_na_potezi.število_moznih_potez(igra.igrane_domine)
    if možne_poteze == 0:
        if len(igra.nerazdeljene_domine) > 0:
            besedilo = dodaj_domino(igra)
        elif len(igra.nerazdeljene_domine) == 0:
            besedilo = brez_poteze(igra)
    elif možne_poteze > 0:
        besedilo = igralceva_poteza(igra)
    return besedilo

@bottle.post('/igra/partija/')
def nova_igra_stran():
    global serija
    igra = serija.aktivna_igra
    if len(igra.poteze) == 0:
        začetna_poteza(igra)
        return bottle.template('partija.tpl',igra = igra, besedilo = '')
    else:
        if not igra.je_konec_igre():
            besedilo = poteza(igra)
            return bottle.template('partija.tpl',igra = igra, besedilo = besedilo)
        else:
            igra.konec_igre(serija)
            #return bottle.template('partija_konec.tpl',igra = igra)
            return 'konec igre'


    return "nova igra"

bottle.run(debug=True, reloader=True)