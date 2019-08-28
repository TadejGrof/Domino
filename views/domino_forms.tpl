%if serija.je_konec():
    <form class="sredina" action="/konec_serije/" method="get">
            <input type="submit" value="Nazaj">
    </form>
%else:
    %if igra.je_konec_igre():
        <form class="sredina" action="/domino/konec_partije/" method="post">
            <input type="submit" value="konec igre">
        </form>
    %else:
        %if len(igra.poteze) == 0:
            %if len(serija.koncane_igre) == 0:
                <form class="sredina" action="/domino/zacetna_poteza/" method="post">
                    <input type="submit" value="začni igro">
                </form>
            %else:
                %if serija.koncane_igre[-1].zmagovalec == serija.igralec2:
                    <form class="sredina" action="/domino/racunalnikova_poteza/" method="post">
                        <input type="submit" value="Računalnikova poteza">
                    </form>
                %else:
                    %if index == None:
                        <div class="besedilo" align="center">
                            Izberi domino za začetek igre!
                        </div>
                    %else:
                        <form class="sredina" action="/domino/igralec_poteza/S" method="post">
                            <input type="submit" value="Začni igro">
                        </form>
                    %end
                %end
            %end
        %else:    
            %if igra.igralec_na_potezi == igra.igralec2:
                <form class="sredina" action="/domino/racunalnikova_poteza/" method="post">
                    <input type="submit" value="računalnikova poteza">
                </form>
            %else:
                %if len(igra.igralec1.mozne_poteze(igra.igrane_domine)) == 0:
                    %if len(igra.nerazdeljene_domine) == 0:
                        <form class="sredina" action="/domino/igralec_poteza/potrkaj" method="post">
                            <input type="submit" value="potrkaj">
                        </form>  
                    %else:
                        <form class="sredina" action="/domino/igralec_poteza/dodaj" method="post">
                            <input type="submit" value="dodaj">
                        </form>                 
                    %end
                %else:
                    %if index == None:
                        <div class="besedilo" align="center">
                            "Izberi veljavno domino!"
                        </div>
                    %else:
                        %if igra.igrane_domine.je_prava_domina(igra.igralec1.domine[index]):
                            %if igra.igrane_domine.se_lahko_doda_na_obeh(igra.igralec1.domine[index]):
                                <form class="sredina_levo" action="/domino/igralec_poteza/L" method="post">
                                    <input type="submit" value="{{"igraj na " + str(igra.igrane_domine.leva_stran)}}">
                                </form> 
                                <form class="sredina_desno" action="/domino/igralec_poteza/D" method="post">
                                    <input type="submit" value="{{"igraj na " + str(igra.igrane_domine.desna_stran)}}">
                                </form>
                            %elif igra.igrane_domine.se_lahko_doda_na_stran(igra.igralec1.domine[index],"L"):
                                <form class="sredina" action="/domino/igralec_poteza/L" method="post">
                                    <input type="submit" value="{{"igraj na " + str(igra.igrane_domine.leva_stran)}}">
                                </form> 
                            %elif igra.igrane_domine.se_lahko_doda_na_stran(igra.igralec1.domine[index],"D"):
                                <form class="sredina" action="/domino/igralec_poteza/D" method="post">
                                    <input type="submit" value="{{"igraj na " + str(igra.igrane_domine.desna_stran)}}">
                                </form>
                            %end
                        %else:
                            <div class="besedilo" align="center">
                                Izberi veljavno domino!
                            </div>
                        %end
                    %end
                %end 
            %end
        %end
    %end