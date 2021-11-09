#!/usr/bin/python3
#Ce script permet de rediriger la zone dns vers une autre adresse IP
#Ce script est un morceau de projet en vue d'une haute disponibilité 
#Il prend une variable utilisateur mais il est possible de la changer pour qu'elle soit toujours la meme
#besoin d'un pip install ovh

import ovh
import json

#shreks optionnel mais quand même le bienvenu
var1="⣿⣿⣿⣿⠋⢩⢹⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"
var2="⣿⣿⣿⡧⣦⠄⢧⡙⢿⣟⢁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⢿"
var3="⣿⣿⣿⣷⣶⣶⣦⡈⠂⠄⠸⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠉⠰⢠⣼"
var4="⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⢒⣂⠄⠙⢿⣿⣿⡿⠛⢛⣻⣿⣿⡟⢁⣠⣴⣶⣶"
var5="⣿⣿⣿⣿⣿⣿⣿⠇⢇⡄⣆⣤⣀⣦⡄⢈⣉⣛⣭⡀⠙⠭⡛⠿⣿⣻⣿⣿⣿⣿"
var6="⣿⣿⣿⣿⣿⣿⣿⠄⠄⣿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⣶⣷⡾⣼⣿⠈⠉⠄⠄⠈"
var7="⣿⣿⣿⣿⣿⣿⡇⠄⠄⢿⣿⣿⣿⣥⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠄⠄⠄⠄"
var8="⣿⣿⣿⣿⡿⠋⠄⠄⠄⢸⣿⡿⠿⠄⠈⠛⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠄⠄⠄"
var9="⣿⣿⣿⠟⠁⠄⠄⠄⠄⠄⢠⣄⣀⡲⢦⣤⣼⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⠄"
var10="⠛⠋⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣟⠻⠿⣿⣿⣿⣷⣾⣿⣿⣿⣿⢿⣿⣿⡇⠄⠄"
var11="⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠻⣷⣶⣾⣿⣿⣿⣿⣿⣿⠟⢡⣿⣿⣿⡟⠄⠄"
var12="⣦⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣉⣹⣿⣿⣿⣿⠟⠁⣰⣿⣿⣿⣿⡇⠄⠄"
var13="⣿⣧⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠉⠙⠛⠉⠁⢀⣼⣿⣿⣿⣿⡟⠄⠄⠄"

shrex=[var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13]

for i in shrex:
    print(i)
# FIN DU SHREKS

#pour la situation c'est l'IP publique de l'entreprise
dstip=input("\n \nSHREKS VOUS DEMANDE UNE NOUVELLE IP CIBLE>>> ")




#clé API
client = ovh.Client(
    endpoint='ovh-eu',
    application_key='xxx',
    application_secret='xxxx',
    consumer_key='xxxxxx',
)

#liste les domaines à mon actif -------- debut de boucle qui tourne pour chaque domain
for domain in client.get('/domain'):


    iddomain = client.get('/domain/zone/'+domain+'/record',
                          fieldType='A',
                          subDomain='',
                          )
    # donne l'ID du domaine renseigné dans un tab

    #  sortir en str
    iddomain = map(str, iddomain)
    iddomain=list(iddomain)




    result = client.put('/domain/zone/'+domain+'/record/'+iddomain[0],
                        target=dstip,
                       )

    refresh = client.post('/domain/zone/'+domain+'/refresh/')





    print("\n Zone DNS changée pour "+domain+" \n")












