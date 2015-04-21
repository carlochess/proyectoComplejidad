#!/bin/bash

python escritor.py
python primeraParte.py
python segundaParte.py
archivo=`find entrada/ -type f -printf '%T@ %f\n' | sort -n | tail -1 | cut -f2- -d" "`

gedit entrada/$archivo
gedit salida/$archivo
