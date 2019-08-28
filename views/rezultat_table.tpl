<table class="rezultat_table" frame=border rules=all>
    <tr class="header">
        <th class="ime">
            Ime:
        </th>
        <th class="točke">
            Točke:
        </th>
        <th class="zmagane_partije">
            Zmagane partije:
        </th>   
    </tr>
    <tr class="igralec1">
        <td class="ime">
            {{serija.igralec1.ime}}
        </td>
        <td class="točke">
            {{str(serija.igralec1.skupne_tocke) + " / " + str(serija.tocke_za_zmago)}}
        </td>
        <td class="zmagane_partije">
            %zmagane_partije = 0
            %for koncana_igra in serija.koncane_igre:
                %if koncana_igra.zmagovalec == serija.igralec1:
                    %zmagane_partije += 1
                %end
            %end
            {{str(zmagane_partije) + " / " + str(len(serija.koncane_igre))}}
        </td>
    </tr>
    <tr class="igralec2">
        <td class="ime">
            {{serija.igralec2.ime}}
        </td>
        <td class="točke">
            {{str(serija.igralec2.skupne_tocke) + " / " + str(serija.tocke_za_zmago)}}
        </td>
        <td class="zmagane_partije">
            %zmagane_partije = 0
            %for koncana_igra in serija.koncane_igre:
                %if koncana_igra.zmagovalec == serija.igralec2:
                    %zmagane_partije += 1
                %end
            %end
            {{str(zmagane_partije) + " / " + str(len(serija.koncane_igre))}}
        </td>
    </tr>
</table>