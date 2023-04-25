import os
texte=str("####################################################"+
        "\n##       NOTATION DE LOCATION DE SMARTPHONES      ##"+
        "\n##              Créé par Nathan BOSY              ##"+
        "\n####################################################\n\n\n\n")


#             NOM DU           APPORT  PRIX   PRIX     CAPACITE
#            TELEPHONE        INITIAL  /MOIS  DE BASE  DE STOCKAGE
liste = {   'MARS  | Iphone 14' :       [54.1, 44.9, 1019],     #128
            'MARS  | Iphone 13' :       [62.1, 36.9, 909],      #128
            'MARS  | Iphone 14 +':      [99,   49.9, 1299],     #256
            'MARS  | Iphone 14 Pro Max':[139,  64.9, 1479],     #128
            'MARS  | Iphone 14 Pro':    [129,  57.9, 1329],     #128
            '____  | Samsung S23' :     [99,   39.9, 959],      #256
            '____  | Samsung S23 Ultra':[129,  59.9, 1419],     #512
            'MARS  | Iphone 12' :       [79,   29.9, 809],      #64
            '____  | Samsung S22':      [-20,  32.9, 699],      #128
            '____  | Iphone 11' :       [69,   25.9, 529],      #64
            '____  | Samsung zFlip 4':  [129,  47.9, 594],      #128
            '____  | Samsung zFold 4':  [180,  79.9, 1089],     #256
            
            '____  | Iphone 14' :       [56.1, 42.9, 1019],     #128
            '____  | Iphone 13' :       [59.1, 39.9, 1019],     #128
            '____  | Iphone 14 Pro Max':[76.1, 62.9, 1019],     #128
            '____  | Iphone 14 Pro':    [74.1, 54.9, 1329],     #128
            '____  | Iphone 14 +':      [49.1, 49.9, 1299],     #256
            '____  | Iphone 12' :       [47.1, 31.9, 809]       #64
   }
# ____ = Prix actuel

'''
Fonction pour créer un fichier texte
'''
def txt(texte, n=0) :
    
    nom = 'smartphones '+str(n)+'.txt'
    dir = os.path.join(os.path.dirname(__file__), nom)
    
    if not os.path.isfile(dir) :
        with open(dir, 'w') as fichier:
            fichier.write(texte)
    
    else : txt(texte, n+1)


'''
Calculs
'''
rentabilite = {}
prix_annee_1 = {}
prix_annuel = {}

# Création de suites arithmétiques
for i in liste :
    x1 = round(liste[i][0] + 12*liste[i][1])
    x2 = round(12*liste[i][1])
    u = liste[i][0]
    n = 0 # Nombre de mois
    
    # On calcule le seuil
    while u <= liste[i][2] :
        u += liste[i][1]
        n+= 1
    #print('Téléphone :', i)
    #print('  - Mois : ', n)
    #print('  - Prix : ', x)
    
    rentabilite[i] = n
    prix_annee_1[i] = x1
    prix_annuel[i] = x2

# On trie les disctionnaires
rentabilite  = sorted(rentabilite.items(), key=lambda x:x[1], reverse=True)
prix_annee_1 = sorted(prix_annee_1.items(), key=lambda x:x[1])
prix_annuel  = sorted(prix_annuel.items(), key=lambda x:x[1])



'''
Affichage de la rentabilité
'''
texte+='RENTABILITE :\n'
classement = 1
for i in rentabilite:
    
    texte+=str(classement)+str((3-len(str(classement)))*' ')+str('  -   ')+str(i[0]+ (40-len(i[0]))*' '+f'({i[1]} mois)\n')
    classement += 1
   
    

'''
Affichage du prix la première année
'''
texte+='\n\n\nPRIX PREMIERE ANNEE :\n'
classement = 1
for i in prix_annee_1:
    
    texte+=str(classement)+str((3-len(str(classement)))*' ')+str('  -   ')+str(i[0])+str((40-len(i[0]))*' ')+str(f'({i[1]}€)\n')
    classement += 1
    
    
    
'''
Affichage du prix par an
'''
texte+='\n\n\nPRIX SUR 1 AN :\n'
classement = 1
for i in prix_annuel:
    
    texte+=str(classement)+str((3-len(str(classement)))*' ')+str('  -   ')+str(i[0])+str((40-len(i[0]))*' ')+str(f'({i[1]}€)\n')
    classement += 1



'''
Affichage du score total (classement prix et rentabilité)
'''
texte+='\n\n\nTOTAL PRIX/RENTABILITE :\n(plus le coût est faible, plus le deal est intéressant sur 1 an)\n'

total = {}
for i in range(len(rentabilite)) :
    temp = i+1
    for k in range(len(prix_annee_1)) :
        if rentabilite[i][0] == prix_annee_1[k][0] :
            temp += k+1
    total[rentabilite[i][0]] = temp
    
total = sorted(total.items(), key=lambda x:x[1])
classement = 1
for i in total:
    
    texte+=str(classement)+str((3-len(str(classement)))*' ')+str('  -   ')+str(i[0])+str((40-len(i[0]))*' ')+str(f'(coût de {i[1]})\n')
    classement += 1
    
texte+='\n\n\n\n"____" signifie le prix actuel.\n\nMa page Github : https://github.com/bosy0'
print(texte)
txt(texte)
