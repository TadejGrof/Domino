%if False:
    <figure style="position:absolute;width:100%;height:100%;top:0%;left:0%">
        <img src="design/okvir-v.jpg" width="100%" height="100%">
    </figure>
%end

%if stran == "L":
    %if len(igra.nerazdeljene_domine) > 7:
        %for n in range(len(igra.nerazdeljene_domine)-7):
            <figure style="position:absolute;width:90%;height:7%;left:5%;top:{{str(25+ n * 7.2 ) + "%"}}">
                %if not igra.koncana:
                    <img src="design/(0,0).jpg" width="100%" height="100%" >
                %else:
                    <img src={{"design/" + str(igra.nerazdeljene_domine[n+7])+".jpg"}} width="100%" height="100%" >
                %end
            </figure>
        %end
    %end
%elif stran == "D":
    %if len(igra.nerazdeljene_domine) > 7:
        %for n in range(7):
            <figure style="position:absolute;width:90%;height:7%;left:5%;top:{{str(25+ n * 7.2 ) + "%"}}">
                %if not igra.koncana:
                    <img src="design/(0,0).jpg" width="100%" height="100%" >
                %else:
                    <img src={{"design/" + str(igra.nerazdeljene_domine[n])+".jpg"}} width="100%" height="100%" >
                %end
            </figure>
        %end
    %elif len(igra.nerazdeljene_domine) <= 7:
        %for n in range(len(igra.nerazdeljene_domine)):
            <figure style="position:absolute;width:90%;height:7%;left:5%;top:{{str(25+ n * 7.2 ) + "%"}}">
                %if not igra.koncana:
                    <img src="design/(0,0).jpg" width="100%" height="100%" >
                %else:
                    <img src={{"design/" + str(igra.nerazdeljene_domine[n])+".jpg"}} width="100%" height="100%" >
                %end
            </figure>
        %end  
    %end  
%end        