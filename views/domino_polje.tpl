%if False:
    <figure style="position:absolute;width:100%;height:100%;top:0%;left:0%">
        <img src="design/podlaga-les.jpg" width="100%" height="100%">
    </figure>
%end

%for poteza in igra.poteze:
    <figure style="position:absolute;width:{{str(poteza.design.width) + "%"}};height:{{str(poteza.design.height) + "%"}};left:{{str(poteza.design.left) + "%"}};top:{{str(poteza.design.top) + "%"}};transform:{{"rotate(" + str(poteza.design.rotate) + "deg)"}}">
        <img src={{"design/" + poteza.design.slika}} width="100%" height="100%" >
    </figure>
%end