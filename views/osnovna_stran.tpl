<html>
    <head>
        <title>Osnovna stran</title>
        <link rel="stylesheet" type="text/css" href="design/naslovna_stran.css">
    </head>
    <body>
        <div class="prijava">
                <div autocomplete="off" style="text-align:center;position:absolute;width:80%;height:15%;top:10%;left:10%">
                    Uporabniško ime:
                </div>
                <div style="position:absolute;width:50%;height:15%;top:55%;left:10%;font-size:3.5vh">
                    Točke za zmago:
                </div>
            <form action="/nova_serija/" method="post"> 
                <input style="font-size:20px;text-align:center;position:absolute;width:80%;height:20%;top:30%;left:10%" type="text" name="ime" required>
                <select style="position:absolute;width:35%;height:12%;top:55%;left:55%;font-size:3vh" name="tocke">
                    <option value="50"> 50 </option>
                    <option value="100" selected> 100 </option>
                    <option value="200"> 200 </option>
                    <option value="300"> 300 </option>
                </select>
                <input style="position:absolute;width:50%;height:20%;top:75%;left:25%" type="submit" value="Začni">
            </form>
        </div>
    </body>
</html>