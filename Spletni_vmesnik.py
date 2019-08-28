from Model import Serija_Iger, Igra, Igralec, Igrane_domine, Domino, Poteza, Igra_design, Poteza_design
import bottle

serija = None
oznacena_domina = None
gledana_igra = None

@bottle.route('/naslovna_stran/design/<filepath:path>')
def server_static1(filepath):
    return bottle.static_file(filepath, root = "./static/")

@bottle.route('/domino/design/<filepath:path>')
def server_static2(filepath):
    return bottle.static_file(filepath, root = "./static/")

@bottle.route('/konec_serije/design/<filepath:path>')
def server_static3(filepath):
    return bottle.static_file(filepath, root = "./static/")


@bottle.get('/klik_domine/<stevilka>')
def klik_domine(stevilka):
    global oznacena_domina
    oznacena_domina = int(stevilka)
    bottle.redirect("/domino/")

@bottle.get('/ogled_partije/<index>')
def ogled_partije(index):
    global serija
    global gledana_igra
    gledana_igra = serija.koncane_igre[-int(index)]
    bottle.redirect('/domino/')

@bottle.post('/serija_reset/')
def serija_reset():
    global serija
    global gledana_igra
    gledana_igra = None
    serija = None
    bottle.redirect('/')

@bottle.get('/')
def redirect():
    bottle.redirect('/naslovna_stran/')


@bottle.get('/naslovna_stran/')
def osnovna_stran():
    global serija
    if serija == None:
        return bottle.template('osnovna_stran.tpl')
    else:
        bottle.redirect('/domino/')

@bottle.post("/nova_serija/")
def nova_serija():
    global serija
    ime = bottle.request.forms["ime"]
    serija = Serija_Iger(Igralec(ime),Igralec(),30)
    bottle.redirect("/nova_partija/")
        

@bottle.post('/igralec_poteza/<stran>')
def poteza_igralec(stran):
    global serija
    global oznacena_domina
    igra = serija.aktivna_igra
    domino = igra.igralec1.domine[oznacena_domina]
    poteza = Poteza(domino,stran,igra.igralec1)
    igra.poteza(poteza)
    poteza.doloci_design(igra)
    oznacena_domina = None
    bottle.redirect("/domino/")

@bottle.get("/nova_partija/")
def nova_partija():
    global serija
    serija.nova_igra()
    igra = serija.aktivna_igra
    igra.doloci_design()
    igra.razdeli()
    bottle.redirect("/domino/")

@bottle.get('/domino/')
def domino():
    global serija
    global oznacena_domina
    global gledana_igra
    if gledana_igra == None:
        igra = serija.aktivna_igra
    else:
        igra = gledana_igra
    return bottle.template('domino.tpl',serija = serija,igra=igra, index = oznacena_domina)

@bottle.post('/domino/poteza/')
def poteza2():
    global serija
    igra = serija.aktivna_igra
    if len(igra.poteze) == 0:
        zacetna_poteza(igra)
        bottle.redirect("/domino/")
    elif len(igra.poteze)>0:
        if not igra.je_konec_igre():
            poteza(igra)
            bottle.redirect("/domino/")
        else:
            konec_partije(serija)

def konec_partije(serija):
    igra = serija.aktivna_igra
    igra.konec_igre(serija)
    igra.zmagovalec.tocke_po_zmagi(igra.koncne_tocke)

    if not serija.je_konec():
        bottle.redirect("/domino/konec_partije/")
    else:
        bottle.redirect("/konec_serije/")

@bottle.get("/konec_serije/")
def konec_serije():
    global serija
    serija.vrni_zmagovalca()
    return bottle.template('konec_serije.tpl',serija = serija)

@bottle.get("/domino/konec_partije/")
def konec_igre():
    global serija
    igra = serija.koncane_igre[-1]
    return bottle.template('konec_partije.tpl',igra=igra)

def zacetna_poteza(igra):
    poteza = igra.zacetna_poteza()
    igra.doloci_igralca_na_potezi(poteza.igralec)
    igra.poteza(poteza)
    igra.zadnja_poteza().doloci_design(igra)

def dodaj_domino(igra):
    nakljucna = igra.nakljucna_iz_nerazdeljenih()
    igra.igralec_na_potezi.dodaj_domino(nakljucna)
    besedilo = igra.igralec_na_potezi.ime + ' doda ' + str(nakljucna)
    return besedilo

def brez_poteze(igra):
    besedilo = igra.igralec_na_potezi.ime + ' ne more narediti poteze in ne more dodati domine. <br> Na potezi je: ' + str(igra.igralec_na_potezi.nasprotnik(igra))
    igra.naslednji_na_potezi()
    return besedilo

def igralceva_poteza(igra):
    poteza = igra.nakljucna_poteza()
    poteza.doloci_design(igra)
    if poteza.stran == "L":
        besedilo = poteza.igralec.ime + ' igra ' + str(poteza.domino) + ' na levo stran polja.'
    elif poteza.stran == "D":
        besedilo = poteza.igralec.ime + ' igra ' + str(poteza.domino) + ' na desno stran polja.'
    return besedilo

def poteza(igra):
    mozne_poteze = igra.igralec_na_potezi.stevilo_moznih_potez(igra.igrane_domine)
    if mozne_poteze == 0:
        if len(igra.nerazdeljene_domine) > 0:
            besedilo = dodaj_domino(igra)
        elif len(igra.nerazdeljene_domine) == 0:
            besedilo = brez_poteze(igra)
    elif mozne_poteze > 0:
        besedilo = igralceva_poteza(igra)
    return besedilo

bottle.run(debug=True, reloader=True)