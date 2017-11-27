#!/bin/bash

printf "testing /classification/\n"
python3 test_classification.py

printf "testing /exhibit/\n"
python3 test_exhibit.py

printf "testing /habitat/\n"
python3 test_.py

printf "testing /region/\n"
python3 test_.py

printf "testing /reset/\n"
python3 test_reset.py

printf "testing /species/\n"
python3 test_.py

printf "testing /state/\n"
python3 test_.py

printf "testing /status/\n"
python3 test_.py

printf "testing /zoo/\n"
python3 test_.py
