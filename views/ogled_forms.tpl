%if not serija.je_konec():
    <form class="sredina_levo" action="/konec_partije/" method="get">
        <input type="submit" value="Nazaj">
    </form>
    %if serija.aktivna_igra == None:
        <form class="sredina_desno" action="/nova_partija/" method="post">
            <input type="submit" value="Nova igra">
        </form>
    %else:
        <form class="sredina_desno" action="/domino/" method="get">
            <input type="submit" value="Nazaj na partijo">
        </form>
    %end


    <form class="levo" action="/konec_partije/ogled_partije/" method="get">
        <input type="submit" value="Prejšnja poteza">
    </form>

    <form class="desno" action="/konec_partije/ogled_partije/" method="get">
        <input type="submit" value="Naslednja poteza">
    </form>
%else:
    <form class="sredina" action="/konec_serije/" method="get">
            <input type="submit" value="Nazaj">
    </form>
%end
