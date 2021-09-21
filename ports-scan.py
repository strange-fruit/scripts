#!/usr/bin/python3
#Auteur: Nicolas Masure

from scapy.all import *

print("Les ports indiqués sont les ports ouverts, si un port n'y figure pas, c'est qu'il est fermé. \n")

host_target=input("Entrez l'IP de la machine à scanner \n")
ports_target=input("Plage de port, exemple : 0,1024")

req=Ether()/IP(dst=host_target)/TCP(dport=(ports_target))
res= srp(req, timeout=1)




for rep in res[0]:
	if (rep[1].getlayer(TCP).flags == 18):
		if(rep[1].getlayer(TCP).sport == 21 or rep[1].getlayer(TCP).sport == 22 or rep[1].getlayer(TCP).sport == 443 or rep[1].getlayer(TCP).sport == 80):
			if (rep[1].getlayer(TCP).sport == 80):
				print(" ><(((°>  Open HTTP",  rep[1].getlayer(TCP).sport, "   ><(((°> ")

			if (rep[1].getlayer(TCP).sport == 443):
				print(" ><(((°>  Open HTTPS",  rep[1].getlayer(TCP).sport, "   ><(((°> ")

			if(rep[1].getlayer(TCP).sport == 22):
				print(" ><(((°>  Open SSH",  rep[1].getlayer(TCP).sport, "   ><(((°> ")

			if (rep[1].getlayer(TCP).sport == 21):
				print(" ><(((°>  Open FTP",  rep[1].getlayer(TCP).sport, "   ><(((°> ")

		else:
			print(" ><(((°>  Open ",  rep[1].getlayer(TCP).sport, "   ><(((°> ")
