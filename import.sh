#!/bin/bash

#Ceci est un script qui permet d'importer un fichier .ova vers un serveur Proxmox
#Il fonctionne avec un seul argument : $1 qui correspond au fichier .ova
#Il créer une VM et lui ajoute le disque OVA
#A la fin du script, il est nécéssaire d'aller en interface graphique du proxmox pour supprimer le disque0 et attacher le disque1 (ova) en SATA.

tar -xvf $1
echo -ne "Extract done..!\n"
rm ./*.ovf ./*.mf
chown import:import *.vmdk
echo -ne "Convert...\n"
qemu-img convert -f vmdk -O qcow2 *.vmdk target.qcow2
echo -ne "Convert done!"

rm ./*.vmdk
chown import:root target.qcow2
#rm ./*.ova
echo "First step done !!"


echo -ne "Configuration de base : \n" 
echo -ne "Entrez le nom de la VM [string] : "
read vmname
echo -ne "Entrez RAM [4096] : "
read ram
if [[ ! $ram =~ ^[0-9]+$ ]] ; then
	echo "not an integer, exiting"
	exit
fi

echo -ne "Entrez le VMID [int] : "
read vmid
if [[ ! $vmid =~ ^[0-9]+$ ]] ; then
	echo "not an integer"
	exit
fi

echo -ne "Entrez le nombre de CPU [2] : "
read cpu
if [[ ! $cpu =~ ^[0-9]+$ ]] ; then
	echo "not an integer"
	exit
fi


echo -ne "Entrez le nombre de core [2] :"
read core
if [[ ! $core =~ ^[0-9]+$ ]] ; then
	echo "not an integer, exiting"
	exit
fi

pvesh create /nodes/VIRTUALAB1/qemu -name $vmname -vmid $vmid -scsi0 local-lvm:20 -memory $ram -cpu host -socket $cpu -cores $core -net0 virtio,bridge=vmbr0
echo -ne "VM created with : \n Name = $vmname\n VMID = $vmid \n Memory = $ram \n CPU(s) = $cpu \n Core(s) = $core\n"

pvesh set /nodes/VIRTUALAB1/qemu/$vmid/config -delete scsi0
echo -ne "Disque dur originel détaché \n"

qm importdisk $vmid target.qcow2 local-lvm
rm target.qcow2
echo -ne "Disk import done... \n Please remove hardisk and attach the new one with graphical interface and change boot order\n" 

