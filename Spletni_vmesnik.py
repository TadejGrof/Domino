from Model import Serija_Iger, Igra, Igralec, Igrane_domine, Domino, Poteza, Igra_design, Poteza_design
import bottle

serija = None
oznacena_domina = None
gledana_igra = None

#######################################################################################################
@bottle.route('/<karkoli>/design/<filepath:path>')
def server_static1(karkoli,filepath):
    return bottle.static_file(filepath, root = "./static/")

@bottle.route('/<karkoli1>/<karkoli2>/design/<filepath:path>')
def server_static4(karkoli1,karkoli2,filepath):
    return bottle.static_file(filepath, root = "./static/")

#########################################################################################################

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
    tocke = int(bottle.request.forms["tocke"])
    serija = Serija_Iger(Igralec(ime),Igralec(),tocke)
    serija.nova_igra()
    igra = serija.aktivna_igra
    igra.doloci_design()
    igra.razdeli()
    bottle.redirect("/domino/")

@bottle.post("/nova_partija/")
def nova_partija():
    global serija
    serija.nova_igra()
    igra = serija.aktivna_igra
    igra.doloci_design()
    igra.razdeli()
    if len(serija.koncane_igre)> 0:
        igra.doloci_igralca_na_potezi(serija.koncane_igre[-1].zmagovalec)
    bottle.redirect("/domino/")

###################################################################################################

@bottle.get('/domino/')
def domino():
    global serija
    global oznacena_domina
    global gledana_igra
    if gledana_igra == None:
        igra = serija.aktivna_igra
    else:
        igra = gledana_igra
    return bottle.template('domino.tpl',serija = serija, igra=igra, index = oznacena_domina)

@bottle.get('/domino/klik_domine/<stevilka>')
def klik_domine(stevilka):
    global oznacena_domina
    oznacena_domina = int(stevilka)
    bottle.redirect("/domino/")

@bottle.post('/domino/zacetna_poteza/')
def zacetna_poteza():
    global serija
    igra = serija.aktivna_igra
    zacetna_poteza_prve_igre(igra)
    bottle.redirect("/domino/")

@bottle.post('/domino/racunalnikova_poteza/')
def poteza2():
    global serija
    igra = serija.aktivna_igra
    if len(igra.poteze) == 0:
        prva_poteza(igra)
    else:
        poteza(igra)
    bottle.redirect("/domino/")

@bottle.post('/domino/igralec_poteza/dodaj')
def poteza_igralec_dodaj():
    global serija
    igra = serija.aktivna_igra
    nakljucna = igra.nakljucna_iz_nerazdeljenih()
    igra.igralec1.dodaj_domino(nakljucna)
    bottle.redirect('/domino/')

@bottle.post('/domino/igralec_poteza/potrkaj')
def poteza_igralec_potrkaj():
    global serija
    igra = serija.aktivna_igra
    igra.naslednji_na_potezi()
    bottle.redirect('/domino/')

@bottle.post('/domino/igralec_poteza/<stran>')
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

@bottle.post('/domino/konec_partije/')
def konec_parije2():
    igra = serija.aktivna_igra
    igra.konec_igre(serija)
    igra.zmagovalec.tocke_po_zmagi(igra.koncne_tocke)
    if not serija.je_konec():
        bottle.redirect("/konec_partije/")
    else:
        bottle.redirect("/konec_serije/")

###########################################################################################################

@bottle.get("/konec_partije/")
def konec_igre():
    global serija
    igra = serija.koncane_igre[-1]
    return bottle.template('konec_partije.tpl', igra = igra, serija = serija)

@bottle.get("/konec_partije/ogled_partije/")
def konec_partije_ogled_partije():
    global serija
    global oznacena_domina
    igra = serija.koncane_igre[-1]
    return bottle.template("domino.tpl",serija = serija, igra = igra, index = oznacena_domina)

@bottle.get("/konec_serije/")
def konec_serije():
    global serija
    serija.vrni_zmagovalca()
    return bottle.template('konec_serije.tpl',serija = serija)

@bottle.get('/konec_serije/ogled_partije/<index>')
def ogled_partije(index):
    global serija
    return bottle.template("domino.tpl",igra = None, serija = serija, index = index)

@bottle.post('/konec_serije/serija_reset/')
def serija_reset():
    global serija
    global gledana_igra
    gledana_igra = None
    serija = None
    bottle.redirect('/')

##############################################################################################################
##############################################################################################################
##############################################################################################################

def zacetna_poteza_prve_igre(igra):
    poteza = igra.zacetna_poteza()
    igra.doloci_igralca_na_potezi(poteza.igralec)
    igra.poteza(poteza)
    igra.zadnja_poteza().doloci_design(igra)

def prva_poteza(igra):
    poteza = igra.igralec_na_potezi.premisljena_prva_poteza()
    igra.poteza(poteza)
    igra.zadnja_poteza().doloci_design(igra)

def poteza(igra):
    mozne_poteze = igra.igralec_na_potezi.stevilo_moznih_potez(igra.igrane_domine)
    if mozne_poteze == 0:
        if len(igra.nerazdeljene_domine) > 0:
            dodaj_domino(igra)
        elif len(igra.nerazdeljene_domine) == 0:
            brez_poteze(igra)
    elif mozne_poteze > 0:
        igralceva_poteza(igra)
    
def igralceva_poteza(igra):
    if len(igra.poteze) <= 8:
        poteza = igra.igralec_na_potezi.zgodnja_premisljena_poteza(igra.igrane_domine)
        igra.poteza(poteza)
    else:
        poteza = igra.igralec_na_potezi.pozna_premisljena_poteza(igra.igrane_domine,igra)
        igra.poteza(poteza)
    poteza.doloci_design(igra)

def dodaj_domino(igra):
    nakljucna = igra.nakljucna_iz_nerazdeljenih()
    igra.igralec_na_potezi.dodaj_domino(nakljucna)

def brez_poteze(igra):
    igra.naslednji_na_potezi()
    

################################################################################################################

bottle.run(debug=True, reloader=True)