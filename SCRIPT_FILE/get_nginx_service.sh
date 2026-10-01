#!/bin/bash 
service_status=$(systemctl is-active nginx)
if [[ "$service_status" == "active" ]];
then 
	echo "nginx is runing"
else
	echo "nginx is not runing"
fi	
