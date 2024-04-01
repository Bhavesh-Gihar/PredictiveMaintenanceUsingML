#!/bin/bash
##### Start Service app

cd /home/app/Client/
#####      Creating a service call doorSensor
sudo forever-service install client -r app
##### start a service called doorSensor
sudo service client start