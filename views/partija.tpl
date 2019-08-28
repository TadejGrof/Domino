<html>
    <head>
        <title>Partija2</title>
        <link rel="stylesheet" type="text/css" href="partija.css">
    </head>
    <body>
        <div class="racunalnik">
            Računalnikove domine: 
            %for domina in igra.igralec2.domine:
                {{str(domina)}}
            %end
        </div>
        <div class="polje">
            Polje: {{igra.igrane_domine}}
        </div>
        <div class="igralec">
            {{igra.igralec1.ime}} domine:
            %for domina in igra.igralec1.domine:
                {{str(domina)}}
            %end
        </div>
        <form action="" method="POST">
            <input type="submit" value="Igraj">
        </form>
        <br>
        {{besedilo}}
    </body>
</html>