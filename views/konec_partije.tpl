<html>
    <head>
        <title>Igra stran</title>
        <link rel="stylesheet" type="text/css" href="design/konec_partije.css">
    </head>
    <body>
        <div class="konec_igre">
            %if igra.kapikua:
                KAPIKUA +25
            %else:
                Konec igre
            %end
        </div>
        <div class="zmagovalec">
                {{"Zmagovalec:     " + igra.zmagovalec.ime}}
        </div>
        <div class="točke">
                {{"Dobljene točke: " + str(igra.koncne_tocke)}}
        </div>

        <div class="rezultat">
            Skupen rezultat:
        </div>

        %include('rezultat_table.tpl',serija = serija)

        <form class="desno" action="/konec_partije/ogled_partije/" method="get">
            <input type="submit" value="OGLED">
        </form>

        %if serija.aktivna_igra == None:
            <form class="levo" action="/nova_partija/" method="post">
                <input type="submit" value="NOVA IGRA">
            </form>
        %else:
            <form class="levo" action="/domino/" method="get">
                <input type="submit" value="Nazaj na partijo">
            </form>
        %end
    </body>
</html>