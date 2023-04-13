import os
texte=str("####################################################"+
        "\n##       NOTATION DE LOCATION DE SMARTPHONES      ##"+
        "\n##              Créé par Nathan BOSY              ##"+
        "\n####################################################\n\n\n\n")


#             NOM DU           APPORT  PRIX   PRIX     CAPACITE
#            TELEPHONE        INITIAL  /MOIS  DE BASE  DE STOCKAGE
liste = {   'Iphone 14' :       [54.1, 44.9, 1019],     #128
            'Iphone 13' :       [62.1, 36.9, 909],      #128
            'Iphone 14 +':      [99,   49.9, 1299],     #256
            'Iphone 14 Pro Max':[139,  64.9, 1479],     #128
            'Iphone 14 Pro':    [129,  57.9, 1329],     #128
            'Samsung S23' :     [99,   39.9, 959],      #256
            'Samsung S23 Ultra':[129,  59.9, 1419],     #512
            'Iphone 12' :       [79,   29.9, 809],      #64
            'Samsung S22':      [-20,  32.9, 699],      #128
            'Iphone 11' :       [69,   25.9, 529],      #64
            'Samsung zFlip 4':  [129,  47.9, 594],      #128
            'Samsung zFold 4':  [180,  79.9, 1089]      #256
   }


'''
Fonction pour créer un fichier texte
'''
def txt(texte, n=0) :
    
    if os.path.isfile('smartphones '+str(n)+'.txt'):
        txt(texte, n+1)
    
    with open('smartphones '+str(n)+'.txt', 'w') as fichier:
        fichier.write(texte)


'''
Calculs
'''
rentabilite = {}
prix_annuel = {}

# Création de suites arithmétiques
for i in liste :
    x = round(liste[i][0] + 12*liste[i][1])
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
    prix_annuel[i] = x

# On trie les disctionnaires
rentabilite = sorted(rentabilite.items(), key=lambda x:x[1], reverse=True)
prix_annuel = sorted(prix_annuel.items(), key=lambda x:x[1])



'''
Affichage de la rentabilité
'''
texte+='RENTABILITE :\n'
classement = 1
for i in rentabilite:
    
    texte+=str(classement)+str((3-len(str(classement)))*' ')+str('  -   ')+str(i[0]+ (20-len(i[0]))*' '+f'({i[1]} mois)\n')
    classement += 1
   
    

'''
Affichage du prix par an
'''
texte+='\n\n\nPRIX 1 AN :\n'
    
for i in prix_annuel:
    
    texte+=str(i[0])+str((20-len(i[0]))*' ')+str(f'({i[1]}€)\n')



'''
Affichage du score total (classement prix et rentabilité)
'''
texte+='\n\n\nTOTAL PRIX/RENTABILITE :\n'
    
total = {}
for i in range(len(rentabilite)) :
    temp = i+1
    for k in range(len(prix_annuel)) :
        if rentabilite[i][0] == prix_annuel[k][0] :
            temp += k+1
    total[rentabilite[i][0]] = temp
    
total = sorted(total.items(), key=lambda x:x[1])

for i in total:
    
    texte+=str(i[0])+str((20-len(i[0]))*' ')+str(f'(coût de {i[1]})\n')
    
texte+='\n\n\n\nMa page Github : https://github.com/bosy0'
print(texte)
txt(texte)