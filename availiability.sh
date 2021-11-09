#!/bin/bash

function DOWN()
{
	while true
	do
		ping -c 10 193.70.0.91 > /dev/null

		if [ $? != 0 ]
		then
			echo "DOWN"
			python3 /home/save/exportdns.py 109.220.21.135
			break
		fi
	done
}

function UP()
{
	while true
        do
                ping -c 10 193.70.0.91 > /dev/null

                if [ $? == 0 ]
                then
                        echo "UP"
                        python3 /home/save/exportdns.py 193.70.0.91
			break
                fi
        done
}

while true
do
	DOWN
	UP
done
