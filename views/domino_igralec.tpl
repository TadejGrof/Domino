%if False:
    <figure style="position:absolute;width:100%;height:100%;top:0%;left:0%">
        <img src="design/okvir-h.jpg" width="100%" height="100%">
    </figure>
%end

%if igralec == serija.igralec2:
    %if serija.je_konec():
        %n = -1
        %for domino in igralec.domine_koncanih_iger[-int(index)]:
            %n = n + 1
            <figure style="position:absolute;width:5%;height:90%;left:{{str(3+ 5.1 * (9 + n - len(igralec.domine) // 2))+"%"}};top:5%">
                <img src={{"design/v-" + str(domino) + ".jpg"}} width="100%" height="100%" >
            </figure>
        %end
    %elif igra == serija.aktivna_igra:
        %for n in range(len(igralec.domine)):
            <figure style="position:absolute;width:5%;height:90%;left:{{str(3+ 5.1 * (9 + n - len(igralec.domine) // 2))+"%"}};top:5%">
                %if not igra.koncana:
                    <img src="design/v-(0,0).jpg" width="100%" height="100%" >
                %else:
                    <img src={{"design/v-" + str(igralec.domine[n]) + ".jpg"}} width="100%" height="100%" >
                %end
            </figure>
        %end
    %elif not serija.je_konec():
        %n = -1
        %for domino in igralec.domine_koncanih_iger[-1]:
            %n = n + 1
            <figure style="position:absolute;width:5%;height:90%;left:{{str(3+ 5.1 * (9 + n - len(igralec.domine) // 2))+"%"}};top:5%">
                <img src={{"design/v-" + str(domino) + ".jpg"}} width="100%" height="100%" >
            </figure>
        %end
    %end
%elif igralec == serija.igralec1:
    %n = -1
    %if serija.je_konec():
        %for domino in igralec.domine_koncanih_iger[-int(index)]:
            %n = n + 1
            <figure style="position:absolute;width:5%;height:90%;left:{{str(3+ 5.1 * (9 + n - len(igralec.domine) // 2))+"%"}};top:5%">
                <img src={{"design/v-" + str(domino) + ".jpg"}} width="100%" height="100%" >
            </figure>
        %end
    %elif igra == serija.aktivna_igra:
        %for domino in igralec.domine:
            %n = n + 1
            %if n == index:
                <figure style="position:absolute;width:5%;height:90%;left:{{str(3+ 5.1 * (9 + n - len(igralec.domine) // 2))+"%"}};top:-25%">
                        <a href={{"/domino/klik_domine/" + str(n)}}>
                            <img src={{"design/v-" + str(domino) + ".jpg"}} width="100%" height="100%" >
                        </a>
                </figure>
            %else:
                <figure style="position:absolute;width:5%;height:90%;left:{{str(3+ 5.1 * (9 + n - len(igralec.domine) // 2))+"%"}};top:5%">
                    %if serija.aktivna_igra.igralec_na_potezi == igralec and len(igralec.mozne_poteze(igra.igrane_domine)) > 0:
                        <a href={{"/domino/klik_domine/" + str(n)}}>
                            <img src={{"design/v-" + str(domino) + ".jpg"}} width="100%" height="100%" >
                        </a>
                    %elif serija.aktivna_igra.igralec_na_potezi == igralec and len(igra.poteze) == 0:
                        <a href={{"/domino/klik_domine/" + str(n)}}>
                            <img src={{"design/v-" + str(domino) + ".jpg"}} width="100%" height="100%" >
                        </a>
                    %else:
                        <img src={{"design/v-" + str(domino) + ".jpg"}} width="100%" height="100%" >
                    %end
                </figure>
            %end
        %end
    %elif not serija.je_konec():
        %for domino in igralec.domine_koncanih_iger[-1]:
            %n = n + 1
            <figure style="position:absolute;width:5%;height:90%;left:{{str(3+ 5.1 * (9 + n - len(igralec.domine) // 2))+"%"}};top:5%">
                <img src={{"design/v-" + str(domino) + ".jpg"}} width="100%" height="100%" >
            </figure>
        %end
    %end
%end