from upemtk import *
from time import sleep
from random import *

def case_vers_pixel(case):
    '''
    prend un couple de coordonnée associée à la case et renvoie le pixel central de cette case.
    '''
    i, j = case
    return (i + .5) * taille_case, (j + .5) * taille_case

def trace_puzzle(taille,taille_case,puzzle,mode):
    '''
    à partir de la taille du puzzle, cette fonction va permettre la structuration du plateau, en gros la fonction va parcourir la liste puzzle et ( par l'intermediaire des fonctions trace_mode ) dessiner chaque case en se decalant a chaque fois sur la droite et en "revenant à la ligne" toute les "taille" fois.
    cette fonction s'occupe aussi de l'interface de jeu (grille,bouton de changement de mode et de retour)"
    '''
    rectangle(taille*taille_case,0,(taille+4)*taille_case,(taille+2)*taille_case,couleur='grey',remplissage='grey')
    rectangle(0,taille*taille_case,taille*taille_case,(taille+2)*taille_case,couleur='grey',remplissage='grey')
    rectangle(taille_case*taille,0,taille_case*(taille+4),taille_case*2,couleur='grey',remplissage='darkgrey',epaisseur=3)
    rectangle(taille_case*taille,taille_case*2,taille_case*(taille+4),taille_case*4,couleur='grey',remplissage='darkgrey',epaisseur=3)
    rectangle(taille_case*taille,taille_case*4,taille_case*(taille+4),taille_case*6,couleur='grey',remplissage='darkgrey',epaisseur=3)
    rectangle(0,taille_case*taille,taille_case*(4),taille_case*(taille+1),couleur='grey',remplissage='darkgrey',epaisseur=3)
    rectangle(0,taille_case*(taille+1),taille_case*(4),taille_case*(taille+2),couleur='grey',remplissage='darkgrey',epaisseur=3)
    texte( taille_case*2 , taille_case*(taille+0.5) , "retour" ,ancrage='center', taille= 15)
    texte( taille_case*2 , taille_case*(taille+1.5) , "indice" ,ancrage='center', taille= 15)

    cercle( taille_case*(taille+1) , taille_case , taille_case/2-2 , couleur = 'black', remplissage = 'red')
    cercle( taille_case*(taille+3) , taille_case , taille_case/2-2 , couleur = 'black', remplissage = 'green')
    ligne(taille_case*(taille+1.7),0.5*taille_case,taille_case*(taille+2.3),1.5*taille_case)
    texte( taille_case*(taille+1) , taille_case*3 , 1 , ancrage='center' , taille=11)
    cercle( taille_case*(taille+1) , taille_case*3 , taille_case/2-2 , couleur = 'black', epaisseur=2)
    texte( taille_case*(taille+3) , taille_case*3 , 0 , ancrage='center' , taille=11)
    cercle( taille_case*(taille+3) , taille_case*3 , taille_case/2-2 , couleur = 'black', epaisseur=2)
    ligne(taille_case*(taille+1.7),2.5*taille_case,taille_case*(taille+2.3),3.5*taille_case)
    ligne(taille_case*(taille+1)-10,(taille_case*5)-10,taille_case*(taille+1)+10,(taille_case*5)+10, epaisseur=3)
    ligne(taille_case*(taille+1)-10,(taille_case*5)+10,taille_case*(taille+1)+10,(taille_case*5)-10, epaisseur=3)
    cercle( taille_case*(taille+3) , (taille_case*5) , taille_case/2-3 , couleur = 'black' , epaisseur=2)
    ligne(taille_case*(taille+1.7),4.5*taille_case,taille_case*(taille+2.3),5.5*taille_case)
    for rang in range(taille+1):
        #rectangle(0,0,taille*taille_case,taille*taille_case, couleur = 'grey', remplissage = 'grey')
        ligne(rang*taille_case,0,rang*taille_case,taille*taille_case, couleur='blue')
        ligne(0,rang*taille_case,taille*taille_case,rang*taille_case, couleur='blue')
        if mode == 1:
            for lignes in range(taille):
                for collones in range(taille):
                    trace_mode1((puzzle[(taille*lignes)+collones]),collones,lignes)
        if mode == 2:
            for lignes in range(taille):
                for collones in range(taille):
                    trace_mode2((puzzle[(taille*lignes)+collones]),collones,lignes)
        if mode == 3:
            for lignes in range(taille):
                for collones in range(taille):
                    trace_mode3((puzzle[(taille*lignes)+collones]),collones,lignes)
    return

def trace_mode1(case,collones,lignes):
    '''
    les 3 differentes fonctions trace mode s'occupent seulement de dessiner le puzzle aux coordonnées "transmises" par trace_puzzle, les cases "2" et "3" sont tracées differement des cases "0" et "1" pour que l'ont puissent les differencier ( 2,3 => case permanentes qui ne changent pas si l'on clique dessus et qui sont de base dans le puzzle / 0,1 => cases que l'ont peut modifier en cliquant dessus et qui sont initialement des None c'est à dire des cases blanches. )
    '''
    (x,y)=case_vers_pixel((collones,lignes))
    if case == None:
        cercle( x , y , taille_case/2-2 , couleur = 'white', remplissage = 'white')
    elif case == 1:
        cercle( x , y , taille_case/2-2 , couleur = 'green', remplissage = 'green')
    elif case == 0:
        cercle( x , y , taille_case/2-2 , couleur = 'red', remplissage = 'red')
    elif case == 3:
        cercle( x , y , taille_case/2-2 , couleur = 'black', remplissage = 'green' , epaisseur=2)
    elif case == 2:
        cercle( x , y , taille_case/2-2 , couleur = 'black', remplissage = 'red', epaisseur=2)
    elif case == 4:
        rectangle(x-15,x+15,x+15,x-15, couleur='black' , remplissage='black')
        #animation de fin
    return

def trace_mode2(case,collones,lignes):
    (x,y)=case_vers_pixel((collones,lignes))
    if case == None:
        cercle( x , y , taille_case/2-2 , couleur = 'white', remplissage = 'white')
    elif case == 1:
        texte( x , y , 1 , ancrage='center' , taille=10)
    elif case == 0:
        texte( x , y , 0 , ancrage='center' , taille=10)
    elif case == 3:
        texte( x , y , 1 , ancrage='center' , taille=10)
        cercle( x , y , taille_case/2-3 , couleur = 'black', epaisseur=2)
    elif case == 2:
        texte( x , y , 0 , ancrage='center' , taille=10)
        cercle( x , y , taille_case/2-3 , couleur = 'black', epaisseur=2)
    return

def trace_mode3(case,collones,lignes):
    (x,y)=case_vers_pixel((collones,lignes))
    if case == None:
        cercle( x , y , taille_case/2-2 , couleur = 'white', remplissage = 'white')
    elif case == 1:
        ligne(x-9,y-9,x+9,y+9, epaisseur=2)
        ligne(x-9,y+9,x+9,y-9, epaisseur=2)
    elif case == 0:
        cercle( x , y , taille_case/2-3 , couleur = 'black' , epaisseur=2)
    elif case == 3:
        ligne(x-10,y-10,x+10,y+10, epaisseur=3)
        ligne(x-10,y+10,x+10,y-10, epaisseur=3)
    elif case == 2:
        cercle( x , y , taille_case/2-2 , couleur = 'black' , epaisseur=3)
    return

def puzzle_reel(puzzle):
    '''
    la liste puzzle est composée de succession de None,0,1,2,3 cela est tres utile pour que le programme differencie les cases "inchangeables" du puzzles de celle que l'on peut modifier, mais pour certaines regles du jeu comme "autant de 0 que de 1" ou "il ne doit pas y avoir 2 lignes ou 2 collones identique" le programme doit lire respectivement 0 et 2, et 1 et 3 comme des valeurs identiques.
    donc cette fonction va simplement creer une liste (que l'on apelera rpuzzle) identique à puzzle, mise à part le fait que les 2 sont devenus des 0 et les 3 des 1.
    '''
    rpuzzle=[]
    for i in range(len(puzzle)):
        if puzzle[i]==2:
            rpuzzle.append(0)
        elif puzzle[i]==3:
            rpuzzle.append(1)
        else:
            rpuzzle.append( puzzle[i] )
    return rpuzzle

def remplie(liste):
    '''
    cette fonction verifie simplement si une liste donnée est remplie ( c'est à dire qu'il n'y a pas de None ) et renvoie True si c'est le cas. Cela peut etre utile pour eviter d'afficher des voyant pour signaler au joueur une faute alors que la ligne n'est meme pas remplie.
    '''
    ok=0
    for i in range(len(liste)):
        if liste[i] != None:
            ok+=1
    if ok == len(liste):
        return True

def ligne_desequilibree(puzzle,taille):
    '''
    ligne/collones_desequilibree vont entre autre decouper rpuzzle en ligne/collones, et verifier ( si cette ligne/collone est remplie ) s'il y'a autant de 0 que de 1, si ce n'est pas le cas la fonction affichera un trait rouge foncé en bas de la collone ou a droite de la ligne pour le signaler au joueur, enfin elle retournera True, et si ce n'est pas le cas, elle retournera False.
    '''
    z=[]
    l=[]
    rpuzzle=puzzle_reel(puzzle)
    for lignes in range(taille):
        zero=[]
        un=[]
        l=rpuzzle[taille*lignes:taille*(lignes+1)]
        if not remplie(l):
            for i in range(len(l)):
                if l[i]==0:
                    zero.append(i)
                elif l[i]==1:
                    un.append(i)
        if (len(un) > taille/2) or (len(zero) > taille/2):
            z.append(lignes)
    if not(z==[]):
        #print(z)
        for j in range(len(z)):
            ligne(30*taille+1,z[j]*30,30*taille+1,(z[j]+1)*30,couleur='darkred', epaisseur = 3)
        return True
    else:
        return False

def collone_desequilibree(puzzle,taille):
    z=[]
    l=[]
    un=[]
    zero=[]
    rpuzzle=puzzle_reel(puzzle)
    for collones in range(taille):
        un=[]
        zero=[]
        l=[]
        for i in range(taille):
            l.append(rpuzzle[(taille*i)+collones])
            #print(l)
        for pos in range(len(l)):
            if l[pos]==0:
                zero.append(pos)
            if l[pos]==1:
                un.append(pos)
        #print(collones,zero)
        if (len(un) > taille/2) or (len(zero) > taille/2) :
            z.append(collones)
    if not(z==[]):
        #print(z)
        for j in range(len(z)):
            ligne(z[j]*30,30*taille+1,(z[j]+1)*30,30*taille+1,couleur='darkred', epaisseur = 3)
        return True
    else:
        return False



def ligne_identique(puzzle,taille):
    '''
    les 2 fonctions ligne/collones_identique decouperont rpuzzle en ligne/collones et ( si elle sont remplies ) verifieront que aucune autre ligne/collones ne leurs sont identiques, si c'est le cas elle renvoie False, mais si la fonction trouve une ligne/colone identique, elle affichera un trait rouge foncé pour le signaler et retournera True.
    '''
    rpuzzle=puzzle_reel(puzzle)
    z=[]
    l=[]
    k=[]
    for lignes in range(taille):
        l=rpuzzle[taille*lignes:taille*(lignes+1)]
        for lignesc in range(taille):
            k=rpuzzle[taille*lignesc:taille*(lignesc+1)]
            if l==k and lignes!=lignesc and remplie(l) and remplie(k):
                z.append(lignes)
                #print(str(lignes))
                #print(str(lignesc))
                #print(l)
                #print(k)
    if not(z==[]):
        #print(z)
        for i in range(len(z)):
            ligne(taille_case*taille+1,(z[i])*taille_case,taille_case*taille+1,(z[i]+1)*taille_case,couleur='darkred', epaisseur = 3)
        return True
    else:
        return False

def collones_identique(puzzle,taille):
    rpuzzle=puzzle_reel(puzzle)
    z=[]
    l=[]
    k=[]
    for collones in range(taille):
        l=[]
        for i in range(taille):
            l.append(rpuzzle[(taille*i)+collones])
        for collonesc in range(taille):
            k=[]
            for j in range(taille):
                k.append(rpuzzle[(taille*j)+collonesc])
            if l==k and collones!=collonesc and remplie(l) and remplie(k):
                z.append(collones)
            #print("k est")
            #print(k)
        #print("l est")
        #print(l)
    if not(z==[]):
        for i in range(len(z)):
            ligne((z[i])*taille_case,taille_case*taille+1,(z[i]+1)*taille_case,taille_case*taille+1,couleur='darkred', epaisseur = 3)
        return True
    else:
        return False



def triple_ligne(puzzle,ligne):
    '''
    ces fonction parcourent les lignes/collones de puzzle pour verifier qu'il n'y a pas 3 case de meme couleurs cote à cote, et si c'est le cas elles renvoient True et encadre les cases en rouge, sinon elle renvoient false.
    '''
    a=0
    for lignes in range(taille+1):
        rpuzzle=puzzle_reel(puzzle)
        for i in range(taille):
            if i<(taille-2):
                c=rpuzzle[taille*(lignes-1)+i]
                c2=rpuzzle[taille*(lignes-1)+i+1]
                c3=rpuzzle[taille*(lignes-1)+i+2]
                if c==c2 and c2==c3 and c!=None:
                    rectangle(i*taille_case,(lignes-1)*taille_case,(i+3)*taille_case,lignes*taille_case,couleur='red',epaisseur=2)
                    a+=1
    if a != 0:
        return True
    return False

def triple_collone(puzzle,taille):
    for collone in range(taille+1):
        rpuzzle=puzzle_reel(puzzle)
        for i in range(taille):
            if i<(taille-2):
                c=rpuzzle[(collone-1)+(i*taille)]
                c2=rpuzzle[(collone-1)+((i+1)*taille)]
                c3=rpuzzle[(collone-1)+((i+2)*taille)]
                if c==c2 and c2==c3 and c!=None:
                    rectangle((collone-1)*taille_case,i*taille_case,collone*taille_case,(i+3)*taille_case,couleur='red',epaisseur=2)
    if a != 0:
        return True
    return False

def win(puzzle,taille):
    '''
    cette fonction va simplement verifier que toute les condition pour la victoire sont remplies, en utilisant toutes les fonction créées precedement.
    '''
    if not(remplie(puzzle)):
        return False
    if triple_collone(puzzle,taille):
        #print("triple collone")
        return False
    if triple_ligne(puzzle,taille):
        #print("triple ligne")
        return False
    if ligne_identique(puzzle,taille):
        #print("ligne identique")
        return False
    if collones_identique(puzzle,taille):
        #print("collones identique")
        return False
    if ligne_desequilibree(puzzle,taille):
        #print("ligne desequilibree")
        return False
    if collone_desequilibree(puzzle,taille):
        #print("collone desequilibree")
        return False
    return True

def trace_menu():
    '''
    cette fonction trace simplement l'interface du menu.
    '''
    rectangle(0,0,430,260,couleur='black',remplissage='darkgrey',epaisseur=7)
    texte(30,20,"Takuzu", police='impact',taille=35)
    texte(30,100,"choisissez la taille du puzzle", taille = 15)
    rectangle(30,150,100,220,couleur='black',remplissage='grey')
    rectangle(130,150,200,220,couleur='black',remplissage='grey')
    rectangle(230,150,300,220,couleur='black',remplissage='grey')
    rectangle(330,150,400,220,couleur='black',remplissage='grey')
    rectangle(220,30,360,75, remplissage='grey')
    texte(57,170,"4",taille=20)
    texte(158,170,"6",taille=20)
    texte(258,170,"8",taille=20)
    texte(350,170,"10",taille=20)
    texte(250,35,"quitter",taille=20)

def trace_menu_fin():
    '''
    cette fonction trace simplement l'interface du menu de fin du jeu.
    '''
    rectangle(0,0,430,260,couleur='black',remplissage='darkgrey',epaisseur=7)
    texte(30,20,"Takuzu", police='impact',taille=35)
    rectangle(220,30,360,75, remplissage='grey')
    texte(250,35,"quitter",taille=20)
    rectangle(150,110,280,153, remplissage='grey')
    texte(215,130,"rejouer",taille=20,ancrage='center')


def retour(puzzle,memoire):
    '''
    à chaque fois que le joueur clique sur une case non permanente et qu'il la change, les coordonnées de cette case sont enregistrer dans une liste appelée mémoire, la fonction retour ( activée lorque le joueur appuie sur le bouton retour de l'interface ) va simplement faire le chemin inverse : elle transforme les None en 1, les 1 en 0 et les 0 en None, et ce sur le dernier element de la liste mémoire ( c'est à dire la derniere case sur laquelle le joueur a cliquer ).
    '''
    if len(memoire) != 0:
        if puzzle[memoire[len(memoire)-1]] == None:
            puzzle[memoire[len(memoire)-1]] = 1
        elif puzzle[memoire[len(memoire)-1]] == 1:
            puzzle[memoire[len(memoire)-1]] = 0
        elif puzzle[memoire[len(memoire)-1]] == 0:
            puzzle[memoire[len(memoire)-1]] = None
        memoire.pop(len(memoire)-1)

def indice(puzzle,taille,mode):
    #for i in range(len(puzzle)):
        #print(puzzle_reel(puzzle)[i],solution[i])
    if not(ligne_desequilibree(puzzle,taille)) and not(collone_desequilibree(puzzle,taille)) and not(ligne_identique(puzzle,taille)) and not(collones_identique(puzzle,taille)) and not(triple_collone(puzzle,taille)) and not(triple_ligne(puzzle,taille)):
        if solution_puzzle(puzzle,solution)[0]:
            l=[]
            rpuzzle=puzzle_reel(puzzle)
            for lignes in range(taille):
                zero=[]
                un=[]
                rien=[]
                l=rpuzzle[taille*lignes:taille*(lignes+1)]
                if not remplie(l):
                    for i in range(len(l)):
                        if l[i]==None:
                            rien.append(i)
                        elif l[i]==0:
                            zero.append(i)
                        elif l[i]==1:
                            un.append(i)
                    if len(zero)==taille/2:
                        for pos in range(len(rien)):
                            clignote(mode,taille,lignes,rien[pos],1)
                            return True
                    elif len(un)==taille/2:
                        for pos in range(len(rien)):
                            clignote(mode,taille,lignes,rien[pos],0)
                            return True
            for collones in range(taille):
                un=[]
                zero=[]
                l=[]
                for i in range(taille):
                    l.append(rpuzzle[(taille*i)+collones])
                    un=[]
                    zero=[]
                    rien=[]
                if not remplie(l):
                    for pos in range(len(l)):
                        if l[pos]==None:
                            rien.append(pos)
                        if l[pos]==0:
                            zero.append(pos)
                        if l[pos]==1:
                            un.append(pos)
                    #print(collones,rien)
                    #print(l)
                    if len(zero)==taille/2:
                        for pos in range(len(rien)):
                            clignote(mode,taille,rien[pos],collones,1)
                            return
                    elif len(un)==taille/2:
                        for pos in range(len(rien)):
                            clignote(mode,taille,rien[pos],collones,0)
                            return
            for lignes in range(taille):
                l=l=rpuzzle[taille*lignes:taille*(lignes+1)]
                for i in range(taille):
                    if i<(taille-1):
                        if l[i]==l[i+1] and l[i]!=None:
                            if i<(taille-2):
                                if l[i+2]==None:
                                    if l[i]==1:
                                        clignote(mode,taille,lignes,i+2,0)
                                        return True
                                    else :
                                        clignote(mode,taille,lignes,i+2,1)
                                        return True
                            if i>0:
                                if l[i-1]==None:
                                    if l[i]==1:
                                        clignote(mode,taille,lignes,i-1,0)
                                        return True
                                    else:
                                        clignote(mode,taille,lignes,i-1,1)
                                        return True
                        if i<(taille-1):
                            if l[i+1]==l[i-1] and l[i]==None and l[i+1]!=None:
                                if l[i+1]==1:
                                    clignote(mode,taille,lignes,i,0)
                                    return True
                                else:
                                    clignote(mode,taille,lignes,i,1)
                                    return True

            for collones in range(taille):
                l=[]
                for pos in range(taille):
                    l.append(rpuzzle[(taille*pos)+collones])
                    #print(l)
                for i in range(taille):
                    if i<(taille-1):
                        if l[i]==l[i+1] and l[i]!=None:
                            if i<(taille-2):
                                if l[i+2]==None:
                                    if l[i]==1:
                                        clignote(mode,taille,i+2,collones,0)
                                        return True
                                    else :
                                        clignote(mode,taille,1+2,collones,1)
                                        return True
                            if i>0:
                                if l[i-1]==None:
                                    if l[i]==1:
                                        clignote(mode,taille,i-1,collones,0)
                                        return True
                                    else:
                                        clignote(mode,taille,i-1,collones,1)
                                        return True
                        if i<(taille-1):
                            if l[i+1]==l[i-1] and l[i]==None and l[i+1]!=None:
                                if l[i+1]==1:
                                    clignote(mode,taille,i,collones,0)
                                    return True
                                else:
                                    clignote(mode,taille,i,collones,1)
                                    return True

            print("pas d'indice pour l'instant, continuez à remplir le puzzle.")
            return False
        else:
            #print("ok")
            lignes=solution_puzzle(puzzle,solution)[1]//taille
            collones=solution_puzzle(puzzle,solution)[1]%taille
            clignote(4,taille,lignes,collones,1)
            return True
    print("corrigez vos erreures avant de demander un indice.")
    return False

def clignote(mode,taille,lignes,collones,case):
    (x,y)=case_vers_pixel((collones,lignes))
    for i in range(2):
        efface("clignotant")
        mise_a_jour()
        sleep(0.1)
        if mode==1:
            if case == 1:
                cercle( x , y , taille_case/2-2 , couleur = 'green', remplissage = 'green', tag="clignotant")
            elif case == 0:
                cercle( x , y , taille_case/2-2 , couleur = 'red', remplissage = 'red', tag="clignotant")
        if mode==2:
            if case == 1:
                texte( x , y , 1 , ancrage='center' , taille=10, tag="clignotant")
            elif case == 0:
                texte( x , y , 0 , ancrage='center' , taille=10, tag="clignotant")
        if mode==3:
            if case == 1:
                ligne(x-9,y-9,x+9,y+9, epaisseur=2, tag="clignotant")
                ligne(x-9,y+9,x+9,y-9, epaisseur=2, tag="clignotant")
            elif case == 0:
                cercle( x , y , taille_case/2-3 , couleur = 'black' , epaisseur=2, tag="clignotant")
        mise_a_jour()
        sleep(0.1)

        if mode==4:
            ligne(x-9,y-9,x+9,y+9, epaisseur=3,couleur='darkred', tag="clignotant")
            ligne(x-9,y+9,x+9,y-9, epaisseur=3,couleur='darkred', tag="clignotant")
            cercle( x , y , taille_case/2-3 , couleur = 'black' , epaisseur=2, tag="clignotant")
        mise_a_jour()
        sleep(0.1)

def solution_puzzle(puzzle,solution):
    rpuzzle=puzzle_reel(puzzle)
    for i in range(len(puzzle)):
        if (rpuzzle[i] != solution[i]) and rpuzzle[i] != None :
            return (False,i)
    return (True,None)

def animation_fin():
    for i in range(len(puzzle)//2):
        efface_tout()
        puzzle[i]=None
        puzzle[len(puzzle)-1-i]=None
        sleep(0.1)
        trace_puzzle(taille,taille_case,puzzle,mode)
        mise_a_jour()
    rectangle(0,0,taille*taille_case,taille*taille_case,couleur='blue',remplissage='white')
    mise_a_jour()
    for i in range(3):
        texte(taille*taille_case/2,taille*taille_case/2,"WIN",ancrage='center',police='impact',taille=20,tag="win")
        mise_a_jour()
        sleep(0.6)
        efface("win")
        mise_a_jour()
        sleep(0.2)
    texte(taille*taille_case/2,taille/2*taille_case/2,"indices utilisés :",ancrage='center',police='impact',taille=12,tag="win")
    texte(taille*taille_case/2,taille*taille_case/2,str(ind),ancrage='center',police='impact',taille=15,tag="win")
    mise_a_jour()
    sleep(2)

#initialisation
ind=0
time=0
mode=1
a=0
puzzle=[]
memoire=[]
retry=True
while retry:
    memoire=[]
    taille=0
    menu=True
    cree_fenetre(430,260)
    while menu:
        trace_menu()
        framerate=100
        ev = donne_ev()
        ty = type_ev(ev)
        if ty == 'Quitte':
            ferme_fenetre()
            menu = False
            retry = False
            jouer = False
        if ty == 'ClicGauche':
            if (abscisse(ev)>30) and (abscisse(ev)<100) and (ordonnee(ev)>150) and (ordonnee(ev)<220):
                taille=4
                menu = False
                jouer=False
            if (abscisse(ev)>130) and (abscisse(ev)<200) and (ordonnee(ev)>150) and (ordonnee(ev)<220):
                taille=6
                menu = False
            if (abscisse(ev)>230) and (abscisse(ev)<300) and (ordonnee(ev)>150) and (ordonnee(ev)<220):
                taille=8
                menu = False
            if (abscisse(ev)>330) and (abscisse(ev)<400) and (ordonnee(ev)>150) and (ordonnee(ev)<220):
                taille=10
                menu = False
            if (abscisse(ev)>220) and (abscisse(ev)<360) and (ordonnee(ev)>30) and (ordonnee(ev)<75):
                menu=False
                retry=False
                jouer=False
                ferme_fenetre()
                bug=1
        mise_a_jour()
        sleep(1/framerate)
    ferme_fenetre()
    if taille==0:
        retry=False
        jouer=False

    if taille==4:
        puzzle=[None ,  3   , None ,  2  ,
                None , None ,  2   ,  None  ,
                None ,  2   , None , None,
                3   ,  3   , None , None]
        solution=[ 0 , 1 , 1 , 0 ,
                   1 , 0 , 0 , 1 ,
                   0,  0 , 1,  1,
                   1,  1,  0,  0]

    if taille==6:
        puzzle=[   3  , None , None , None , None , None ,
                 None ,   2  , None , None , None ,   3  ,
                 None , None ,   3  ,   3  , None , None ,
                 None , None ,   3  , None , None ,   2  ,
                 None , None , None , None ,   3  , None ,
                 None ,   3  ,   3  , None , None , None ,]

        solution=[ 1 , 1 , 0 , 0 , 1 , 0 ,
                   1 , 0 , 0 , 1 , 0 , 1 ,
                   0 , 0 , 1 , 1 , 0 , 1 ,
                   0 , 1 , 1 , 0 , 1 , 0 ,
                   1 , 0 , 0 , 1 , 1 , 0 ,
                   0 , 1 , 1 , 0 , 0 , 1]

    if taille == 8:
        puzzle =[None,None,None,None,3,None,3,2,
                3 , None,None,None,None,None,None,None,
                None,None,None,2,None,2,None,None,
                None,None,None,3,None,None,None,None,
                None,3,None,None,None,None,None,3,
                None,None,2,2,None,None,None,3,
                None,None,None,None,None,None,3,None,
                2,None,2,None,None,2,3,None]
        solution=[1,0,1,0,1,0,1,0,
                  1,0,0,1,0,1,0,1,
                  0,1,1,0,1,0,0,1,
                  1,0,0,1,0,1,1,0,
                  0,1,1,0,0,1,0,1,
                  1,1,0,0,1,0,0,1,
                  0,0,1,1,0,1,1,0,
                  0,1,0,1,1,0,1,0]

    if taille==10:
        puzzle=[ None , None ,   2  , None ,   3  , None , None ,   3  , None , None ,
                   3  , None ,   2  , None ,   3  , None , None , None ,  3   , None ,
                 None ,   2  , None , None , None , None ,   2  , None , None , None ,
                 None , None ,   2  ,   2  , None , None , None ,   3  ,  3   , None ,
                 None , None , None , None , None , None , None , None ,  2   , None ,
                 None , None , None , None , None , None ,   2  , None , None , None ,
                   2  ,   2  , None ,   2  , None , None ,   2  , None , None ,   2  ,
                 None , None ,   3  , None ,   3  , None , None , None , None , None ,
                 None ,   2  , None , None , None , None , None , None ,   2  , None ,
                   3  , None , None , None , None ,   3  , None , None , None , None ]

        solution=[0,1,0,0,1,0,1,1,0,1,
                  1,1,0,0,1,0,1,0,1,0,
                  0,0,1,1,0,1,0,1,0,1,
                  0,1,0,0,1,1,0,1,1,0,
                  1,0,1,1,0,0,1,0,0,1,
                  1,1,0,1,0,1,0,0,1,0,
                  0,0,1,0,1,1,0,1,1,0,
                  0,1,1,0,1,0,1,0,0,1,
                  1,0,0,1,0,0,1,1,0,1,
                  1,0,1,1,0,1,0,0,1,0,]

    taille_case = 30
    cree_fenetre((taille+4)*taille_case , (taille+2)*taille_case)
    jouer=True



    while jouer :
        efface_tout()
        framerate=100
        trace_puzzle(taille,taille_case,puzzle,mode)
        ligne_identique(puzzle,taille)
        collones_identique(puzzle,taille)
        ligne_desequilibree(puzzle,taille)
        collone_desequilibree(puzzle,taille)
        triple_ligne(puzzle,taille)
        triple_collone(puzzle,taille)
        ev = donne_ev()
        ty = type_ev(ev)
        if ty == 'Quitte':
            jouer = False
            retry = False
        if ty == 'ClicGauche':
            for lignes in range(taille):
                for collones in range(taille):
                    if ((abscisse(ev)>(collones*taille_case) and abscisse(ev)<((collones+1)*(taille_case)) and ordonnee(ev)>(lignes*taille_case) and ordonnee(ev)<((lignes+1)*(taille_case)) and puzzle[(lignes*taille)+collones]!=2 and puzzle[(lignes*taille)+collones]!=3)):
                        memoire.append((lignes*taille)+collones)
                        #print(memoire)
                        if puzzle[(lignes*taille)+collones]==None:
                            puzzle[(lignes*taille)+collones]=0
                        elif puzzle[(lignes*taille)+collones]==0:
                            puzzle[(lignes*taille)+collones]=1
                        elif puzzle[(lignes*taille)+collones]==1:
                            puzzle[(lignes*taille)+collones]=None
            if (abscisse(ev)>0) and (abscisse(ev)<taille_case*4) and (ordonnee(ev)>taille_case*taille) and (ordonnee(ev)<taille_case*(taille+1)):
                retour(puzzle,memoire)
            if (abscisse(ev)>0) and (abscisse(ev)<taille_case*4) and (ordonnee(ev)>taille_case*(taille+1)) and (ordonnee(ev)<taille_case*(taille+2)):
                indice(puzzle,taille,mode)
                if indice(puzzle,taille,mode):
                    ind+=1
            if (abscisse(ev)>(taille*taille_case)) and (abscisse(ev)<taille_case*(taille+4)) and (ordonnee(ev)>0) and (ordonnee(ev)<taille_case*2):
                mode=1
                #print("mode1")
            if (abscisse(ev)>(taille*taille_case)) and (abscisse(ev)<taille_case*(taille+4)) and (ordonnee(ev)>taille_case*2) and (ordonnee(ev)<(taille_case*4)):
                mode=2
                #print("mode2")
            if (abscisse(ev)>(taille*taille_case)) and (abscisse(ev)<taille_case*(taille+4)) and (ordonnee(ev)>taille_case*4) and (ordonnee(ev)<(taille_case*6)):
                mode=3
                #print("mode3")
        if win(puzzle,taille):
            animation_fin()
            jouer=False
        mise_a_jour()
        sleep(1/framerate)
    ferme_fenetre()
    menu_fin=True
    if taille!=0:
        cree_fenetre(430,260)
        while menu_fin:
            trace_menu_fin()
            framerate=100
            ev = donne_ev()
            ty = type_ev(ev)
            if ty == 'Quitte':
                menu_fin = False
                retry = False
                jouer = False
            if ty == 'ClicGauche':
                if (abscisse(ev)>220) and (abscisse(ev)<360) and (ordonnee(ev)>30) and (ordonnee(ev)<75):
                    menu_fin=False
                    retry=False
                    jouer=False
                if (abscisse(ev)>150) and (abscisse(ev)<280) and (ordonnee(ev)>110) and (ordonnee(ev)<153):
                    menu_fin=False
                    retry=True
                    jouer=True
            mise_a_jour()
            sleep(1/framerate)
        ferme_fenetre()

    #obligatoire:
        #mode terminal












