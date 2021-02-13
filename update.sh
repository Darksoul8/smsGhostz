#!/bin/bash
rm -rf *.py
git clone https://github.com/Darksoul8/smsGhostz
mv ./smsGhostz/* ./
rm -rf smsGhostz 
chmod +x *