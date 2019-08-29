<html>
    <head>
        <title>Igra stran</title>
        <link rel="stylesheet" type="text/css" href="design/domino.css">
    </head>
    <body>
        <div class="igra">
            <div class="leva_nerazdeljene">
                %if not serija.je_konec():
                    %include('domino_nerazdeljene.tpl', serija = serija, igra = igra, stran = "L")
                %else:
                    %include('domino_nerazdeljene.tpl',serija = serija, igra = serija.koncane_igre[-int(index)],stran="L")
                %end
            </div>

            <div class="desna_nerazdeljene">
                <button style="position:absolute;width:60%;height:10%;left:20%;top:3%" onclick="myFunction()">Info</button>
                <script>
                    function myFunction() {
                    window.alert("Moje točke: " + {{str(serija.igralec1.skupne_tocke)}}
                     + "/" + {{str(serija.tocke_za_zmago)}}  
                    + "\n" + "Računalnikove točke: " + {{str(serija.igralec2.skupne_tocke)}}
                     + "/" + {{str(serija.tocke_za_zmago)}}  );
                    };
                </script>
                %if not serija.je_konec():
                    %include('domino_nerazdeljene.tpl', serija = serija, igra = igra, stran = "D")
                %else:
                    %include('domino_nerazdeljene.tpl',serija = serija, igra = serija.koncane_igre[-int(index)],stran="D")
                %end
            </div>

            <div class="polje">
                %if not serija.je_konec():
                    %include('domino_polje.tpl', igra = igra)
                %else:
                    %include('domino_polje.tpl', igra = serija.koncane_igre[-int(index)])
                %end
            </div>
            <div class="racunalnik">
                %include('domino_igralec.tpl', serija = serija, igralec = serija.igralec2, index = index)
            </div>

            <div class="igralec">
                %include('domino_igralec.tpl', serija = serija, igralec = serija.igralec1, index = index)
            </div>

            <div class="forms">
                %if igra == serija.aktivna_igra:
                    %include('domino_forms.tpl', serija = serija, igra = igra, index = index)
                %else:
                    %include('ogled_forms.tpl', serija = serija, igra = igra, index = index)
            </div>
        </div>
        
    </body>
</html>