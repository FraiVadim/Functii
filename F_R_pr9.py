from random import choice,randint
matematica=['Câte laturi are un decagon?',
'Cu cât este egală rădăcina pătrată din 121?',
'Care este următorul număr prim după 11?',
'Cu cât este egal 7 la pătrat?',
'Câte fețe pătrate are un cub?',
'Cum se află aria cubului?',
'Cum se numeşte o formă 3D perfect rotundă care arată că o minge?',
'Ce formă 2D are 5 laturi?',
'Cu cat va fi egal un numar ridicat la puterea 0?',
'Cum se afla aria unui triunghi dreptunghic?']
biologia=['Câte gene are omul?',
'Ce este gena?',
'Cum se mai numește diviziunea indirecta la celule?',
'Câte oase are omul?',
'Care sunt cele 3 cele mai mici oase?',
'Care țesuturi sunt formate din celule striate?',
'Care este structura primara a proteinei?',
'Din câte catene este format ADN-ul?',
'Care este rolul mitocondriilor în celulă?',
'Ce sintetizează ribozomii?']
istoria=['În ce an a fost anexată Basarabia?',
'Câte cetăți a ctitorit Ștefan-Cel-Mare?',
'În ce an început primul razboi mondial?',
'Cât a durat al doilea razboi mondial?',
'Cât timp a domnit Napoleon?',
'Cine a fost Decebal?',
'Cine a fost Winston Churcel?',
'Când a avut loc Marea Unire?',
'Cine a fost ales domnitor în Muntenia și Moldova?',
'Care sunt 2 state totalitare din secolul XX?',
'În ce an Republica Moldova a obținut independență?']
chimia=['Din ce este format Atomul?',
'Din ce este format nucleul atomului?',
'Care este sarcina electronului',
'Care este masa moleculara a clorului?',
'Care sunt elementele cu periada II?',
'Care este ozidul superior al azotului?',
'Care este formula glucozei?',
'Care sunt reagenții reacției de saponificare?',
'Câte straturi de electroni are magneziul?',
'Din ce se formează acetilena?']
fizica=['Ce studiază termodinamica?',
'Ce studiază mecatica?',
'Cu cât va fi egal 1 grad celsius în kelvin?',
'Care este formula Intensității?',
'Cum se calculează rezistența totală în legătura în paralel?',
'Cum se calculează intensitatea totală în legătura în paralel?',
'Care este formula accelerației centripete?',
'În ce se măsoară Lucrul?',
'În ce se măsoară Forța?',
'În ce se măsoară Inducția magnetică?']
n=randint(1,5)
if n==1:
    print('domeniul:matematica')
    print(choice(matematica))
if n==2:
    print('domeniul:biologia')
    print(choice(biologia))
if n==3:
    print('domeniul:istoria')
    print(choice(istoria))
if n==4:
    print('domeniul:chimia')
    print(choice(chimia))
if n==5:
    print('domeniul:fizica')
    print(choice(fizica))