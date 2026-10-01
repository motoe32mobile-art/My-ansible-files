#!/bin/bash 
service_status=$(systemctl is-active sshd)
if [[ "$service_status" == "active" ]];
then 
	echo "sshd is runing"
else
	echo "sshd is not runing"
fi	
