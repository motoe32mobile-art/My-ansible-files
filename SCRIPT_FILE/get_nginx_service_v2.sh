#!/bin/bash 
service="nginx"
status=$(ps -ef | grep $service | wc -l)
if [[ $status -gt 1 ]];
then
	echo "$service is a runing"
else
	echo "$service is a not running"
fi

