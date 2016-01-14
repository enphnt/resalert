#!/bin/bash
 
#omxplayer /home/pi/AlertSystem/sews.mp3 &
midori -e Fullscreen &
sudo python /home/pi/AlertSystem/blinkbutton.py
