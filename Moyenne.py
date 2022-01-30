note = open("alain_marc.txt","r")   #Ouverture du fichier contenant les moyennes pour chaque matières d'Alain et Marc
NOTE = note.readlines()

for k in range (len(NOTE)): #Traitement du fichier
    NOTE[k]=NOTE[k].strip()
    NOTE[k]=NOTE[k].split("\t")  
    
MoyenneAlain=0
A=0
MoyenneMarc=0
M=0

for i in range (len(NOTE)):
    if NOTE[i][1] == 'Alain':
        MoyenneAlain = MoyenneAlain + int(NOTE[i][2])   #Somme des notes
        A=A+1   #Comptage du nb de notes
    elif NOTE[i][1] == 'Marc' :
        MoyenneMarc = MoyenneMarc + int(NOTE[i][2]) #Somme des notes
        M=M+1   #Comptage du nb de notes
print(MoyenneMarc/M, MoyenneAlain/A)    #Affichage des moyennes
            