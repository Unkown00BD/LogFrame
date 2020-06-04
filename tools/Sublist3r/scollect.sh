#!/bin/bash
python3 tools/Sublist3r/sublist3r.py -d $1 -o subdomains.txt
echo "Scanning For Vulnerabilty"
python tools/Sublist3r/itsover.py -l subdomains.txt
