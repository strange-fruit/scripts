#!/usr/bin/python3
#!Auteur: Nicolas Masure
from scapy.all import *

print("Enter a network you want to scan with CIDR \n")
target_newtork=input("Example : 192.168.10.0/24 \n")
how_fast_i_am=int(input("Speed ?  For example 0.5 is fast, 5 is really slow \n"))

req=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target_newtork)/IP()
rslt=srp(req, timeout=how_fast_i_am)

#TTL pour OS

for rep in rslt[0]:
	if(rep[0]):

		if(rep[1].getlayer(IP).ttl > 64):
			print("HOST ::  ", rep[1].getlayer(TCP).psrc, "  MAC  ", rep[1].getlayer(Ether).src, "  OS  Windows" )
		else
			print("HOST ::  ", rep[1].getlayer(TCP).psrc, "  MAC  ", rep[1].getlayer(Ether).src, "  OS  Linux" )
			#TTL = 255 pour Cisco
