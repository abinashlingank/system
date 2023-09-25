#!/bin/bash
sudo apt remove nano
sudo apt purge nano
sudo apt remove gedit
sudo apt purge gedit
sudo apt remove libreoffice*
sudo apt purge libreoffice*
sudo apt autoremove
chmod +x app.sh
chmod +x launch.sh
mv blinde.desktop /home/talos/Desktop
cd
cd Desktop
chmod +x blinde.desktop
mv blinde.desktop ~/.local/share/applications 



