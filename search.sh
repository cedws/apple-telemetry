#!/bin/sh
sort root-domains.txt -n -o root-domains.txt

mkdir -p amass
touch amass/amass.txt
cat amass/amass.txt >> amass/known-domains.txt

amass enum -config config.ini -nf amass/known-domains.txt -df root-domains.txt
