@echo off
echo Retrieving connected devices...
arp -a > connected_devices.txt
echo Devices connected to the network are listed in connected_devices.txt
pause
