<html>
    <head>
        <title>Konec Serije</title>
        <link rel="stylesheet" type="text/css" href="design/konec_serije.css">
    </head>
    <body>
        <div class="Naslov">
            %if serija.zmagovalec == serija.igralec1:
                ZMAGA
            %else:
                PORAZ
            %end
        </div>

        <div class="rezultat">
            Rezultat:
        </div>

        %include('rezultat_table.tpl', serija = serija)
        
        <div class="zgornja_vrsta">
        <div style="left:0%;width:10%">
        <b>Igra:</b>
        </div>
        <div style="left:10%;width:20%">
        <b>Zmagovalec:</b>
        </div>
        <div style="left:30%;width:20%">
        <b>Način zmage:</b>
        </div>
        <div style="left:50%;width:20%">
        <b>Dobljene točke:</b>
        </div>
        <div style="left:70%;width:15%">
        <b>Čas:</b>
        </div>
        <div style="left:85%;width:15%">
        <b>Ogled:</b>
        </div>
        </div>

        %n = -1
        %i = 0
        %for koncana_igra in serija.koncane_igre[::-1]:
            % n = n + 1
            % i = i - 1
            %if koncana_igra.zmagovalec == serija.igralec1:
            %barva = "green"
            %elif koncana_igra.zmagovalec == serija.igralec2:
            %barva = "red"
            %end
            <div class="koncana_igra" style="background-color:{{barva}};top:{{str(55 + n * 15) + "%"}}">
                <div class="zaporedna_igra">
                    <font color="yellow">{{str(len(serija.koncane_igre)-n)+ "."}}</font>
                </div>
                <div class="zmagovalec">
                    <font color="white">{{koncana_igra.zmagovalec.ime}}</font>
                </div>
                 <div class="dobljene_točke">
                    <font color="white">{{koncana_igra.koncne_tocke}}</font>
                </div>
                 <div class="način_zmage">
                    %if koncana_igra.kapikua:
                        <font color="white">Capicua</font>
                    %elif len(koncana_igra.igralec1.domine_koncanih_iger[i]) == 0 or len(koncana_igra.igralec2.domine_koncanih_iger[i]) == 0:
                        <font color="white">Zadnje domino</font>
                    %else:
                        <font color="white">Manj pik</font>
                    %end
                </div>
                 <div class="čas">
                    %if koncana_igra.cas_konca.minute < 10:
                        <font color="white">{{str(koncana_igra.cas_konca.hour) + ":0" + str(koncana_igra.cas_konca.minute)}}</font>
                    %else:
                         <font color="white">{{str(koncana_igra.cas_konca.hour) + ":" + str(koncana_igra.cas_konca.minute)}}</font>
                    %end
                </div>
                <form class="ogled" action={{"/konec_serije/ogled_partije/" + str(n + 1)}} method="get">
                    <input style="width:100%;height:100%" type="submit" value="ogled">
                </form>
            </div>
            %end
        %end
    
        <form class="nova_igra" action="/konec_serije/serija_reset/" method="Post">
            <input style="width:100%;height:100%" type="submit" value="nova igra">
        </form>
    </body>
</html>