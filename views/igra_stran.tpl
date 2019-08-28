<html>
    <head>
        <title>Igra stran</title>
    </head>
    <body>
        točke {{serija.igralec1.ime}} = {{serija.igralec1.skupne_tocke}} <br>
        točke {{serija.igralec2.ime}} = {{serija.igralec2.skupne_tocke}}
        
        <form action = "/igra/partija/" method = "post">
            Za začetek nove partije klikni:  <input type="submit" value = "Nova igra">
        </form>
    </body>
</html>