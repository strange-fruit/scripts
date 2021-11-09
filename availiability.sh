#!/bin/bash

function DOWN()
{
	while true
	do
		ping -c 10 <IP> > /dev/null

		if [ $? != 0 ]
		then
			echo "DOWN"
			python3 /home/save/dnszoneOVH.py <IP>
			break
		fi
	done
}

function UP()
{
	while true
        do
                ping -c 10 <IP> > /dev/null

                if [ $? == 0 ]
                then
                        echo "UP"
                        python3 /home/save/exportdns.py <IP>
			break
                fi
        done
}

while true
do
	DOWN
	UP
done
