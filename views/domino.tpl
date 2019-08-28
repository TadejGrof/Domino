<html>
    <head>
        <title>Igra stran</title>
        <link rel="stylesheet" type="text/css" href="design/domino.css">
    </head>
    <body>
        <div class="leva_nerazdeljene">
            %include('domino_nerazdeljene.tpl', serija = serija, igra = igra, stran = "L")
        </div>

        <div class="desna_nerazdeljene">
            %include('domino_nerazdeljene.tpl', serija = serija, igra = igra, stran = "D")
        </div>

        <div class="polje">
            %for poteza in igra.poteze:
                <figure style="position:absolute;width:{{str(poteza.design.width) + "%"}};height:{{str(poteza.design.height) + "%"}};left:{{str(poteza.design.left) + "%"}};top:{{str(poteza.design.top) + "%"}};transform:{{"rotate(" + str(poteza.design.rotate) + "deg)"}}">
                    <img src={{"design/" + poteza.design.slika}} width="100%" height="100%" >
                </figure>
            %end
        </div>
        <div class="racunalnik">
            %if False:
            <figure style="position:absolute;width:100%;height:100%;top:0%;left:0%">
                <img src="design/okvir-h.jpg" width="100%" height="100%">
            </figure>
            %end
            %for n in range(len(igra.igralec2.domine)):
                <figure style="position:absolute;width:5%;height:90%;left:{{str(3+ 5.1 * (9 + n - len(igra.igralec2.domine) // 2))+"%"}};top:5%">
                    %if not igra.koncana:
                        <img src="design/v-(0,0).jpg" width="100%" height="100%" >
                    %else:
                        <img src={{"design/v-" + str(igra.igralec2.domine[n]) + ".jpg"}} width="100%" height="100%" >
                    %end
                </figure>
            %end
        </div>

        <div class="igralec">
        %if False:
            <figure style="position:absolute;width:100%;height:100%;top:0%;left:0%">
                <img src="design/okvir-h.jpg" width="100%" height="100%">
            </figure>
        %end
            %if igra.igralec_na_potezi == igra.igralec1 and len(igra.igralec1.mozne_poteze(igra.igrane_domine)) > 0:
                %if index == None:
                    %n = -1
                    %for domino in igra.igralec1.domine:
                    %n = n + 1
                    <figure style="position:absolute;width:5%;height:90%;left:{{str(3+ 5.1 * (9 + n - len(igra.igralec1.domine) // 2))+"%"}};top:5%">
                        <a href={{"/klik_domine/" + str(n)}}>
                            <img src={{"design/v-" + str(domino) + ".jpg"}} width="100%" height="100%" >
                        </a>
                    </figure>
                    %end
                %else:
                    %n = -1
                    %for domino in igra.igralec1.domine:
                    %n = n + 1
                        %if n == index:
                            <figure style="position:absolute;width:5%;height:90%;left:{{str(3+ 5.1 * (9 + n - len(igra.igralec1.domine) // 2))+"%"}};top:-25%">
                                <a href={{"/klik_domine/" + str(n)}}>
                                    <img src={{"design/v-" + str(domino) + ".jpg"}} width="100%" height="100%" >
                                </a>
                            </figure>
                        %else:
                            <figure style="position:absolute;width:5%;height:90%;left:{{str(3+ 5.1 * (9 + n - len(igra.igralec1.domine) // 2))+"%"}};top:5%">
                                <a href={{"/klik_domine/" + str(n)}}>
                                    <img src={{"design/v-" + str(domino) + ".jpg"}} width="100%" height="100%" >
                                </a>
                            </figure>
                        %end
                    %end
                %end
            %else:
                %n = -1
                %for domino in igra.igralec1.domine:
                    %n = n + 1
                    <figure style="position:absolute;width:5%;height:90%;left:{{str(3+ 5.1 * (9 + n - len(igra.igralec1.domine) // 2))+"%"}};top:5%">
                            <img src={{"design/v-" + str(domino) + ".jpg"}} width="100%" height="100%" >
                    </figure>
                %end
            %end
        </div>

        %if not igra.koncana:
            %if len(igra.poteze) == 0:
                <form action="/domino/poteza/" method="post">
                    <input type="submit" value="začni igro">
                </form>
            %elif igra.je_konec_igre():
                <form action="/domino/poteza/" method="post">
                        <input type="submit" value="konec igre">
                </form>
            %else:    
                %if igra.igralec_na_potezi == igra.igralec2:
                    <form action="/domino/poteza/" method="post">
                        <input type="submit" value="računalnikova poteza">
                    </form>
                %else:
                    %if len(igra.igralec1.mozne_poteze(igra.igrane_domine)) == 0:
                            %if len(igra.nerazdeljene_domine) == 0:
                                <form action="/domino/poteza/" method="post">
                                    <input type="submit" value="potrkaj">
                                </form>  
                            %else:
                                <form action="/domino/poteza/" method="post">
                                    <input type="submit" value="dodaj">
                                </form> 
                                
                            %end
                    %else:
                        %if index == None:
                            <div class="besedilo" align="center">
                                izberi veljavno domino
                            </div>
                        %else:
                            %if igra.igrane_domine.je_prava_domina(igra.igralec1.domine[index]):
                                %if igra.igrane_domine.se_lahko_doda_na_obeh(igra.igralec1.domine[index]):
                                    <form style="positon:absolute;left:32%;top:92%" action="/igralec_poteza/L" method="post">
                                        <input type="submit" value="{{"igraj na" + str(igra.igrane_domine.leva_stran)}}">
                                    </form> 
                                    <form style="positon:absolute;left:52%;top:92%" action="/igralec_poteza/D" method="post">
                                        <input type="submit" value="{{"igraj na" + str(igra.igrane_domine.desna_stran)}}">
                                    </form>
                                %elif igra.igrane_domine.se_lahko_doda_na_levi(igra.igralec1.domine[index]):
                                    <form style="positon:absolute;left:42%;top:92%" action="/igralec_poteza/L" method="post">
                                        <input type="submit" value="{{"igraj na" + str(igra.igrane_domine.leva_stran)}}">
                                    </form> 
                                %elif igra.igrane_domine.se_lahko_doda_na_desni(igra.igralec1.domine[index]):
                                    <form style="positon:absolute;left:42%;top:92%" action="/igralec_poteza/D" method="post">
                                        <input type="submit" value="{{"igraj na" + str(igra.igrane_domine.desna_stran)}}">
                                    </form>
                                %end
                            %else:
                            <div class="besedilo" align="center">
                                izberi veljavno domino
                            </div>
                            %end
                        %end
                    %end 
                %end
            %end
        %else:
            %if serija.je_konec():
                <form action="/konec_serije/" method="get">
                    <input type="submit" value="nova_igra">
                </form>
            %else:
                <form action="/nova_partija/" method="get">
                    <input type="submit" value="nova_igra">
                </form>
            %end
        %end
    </body>
</html>